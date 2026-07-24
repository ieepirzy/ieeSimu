import pygame
import math
import random
import cupy as cp  #If trying this out, make sure you install the cupy version compatible with your specific drivers.

gamma = 6.6743*10**(-11)
dt = 0.01
eps = 1e4

class Body:
    def __init__(self,mass,velocity,position,radius,color):
        self.pos = cp.array(position, dtype=cp.float32)
        self.velocity = cp.array(velocity, dtype=cp.float32)
        self.mass = mass
        self.radius = radius
        self.color = color
        self.force = cp.zeros(2, dtype=cp.float32)

def create_random_bodies(n=5):
    bodies = []
    for _ in range(n):
        m = random.uniform(1e20, 1e26)
        pos = (random.uniform(-5e6, 5e6), random.uniform(-5e6, 5e6))
        vel = (random.uniform(-1e5, 1e5), random.uniform(-1e5, 1e5))
        col = (random.randint(100,255), random.randint(100,255), random.randint(100,255))
        radius = max(3, int(4 + math.log10(m) - 22))
        bodies.append(Body(mass=m, position=pos, velocity=vel, radius=radius, color=col))
    return bodies

def update_forces(bodies):
    n = len(bodies)
    pos = cp.stack([b.pos for b in bodies], dtype=cp.float64)
    mass = cp.array([b.mass for b in bodies], dtype=cp.float64).reshape(n,1)
    forces = cp.zeros((n,2), dtype=cp.float64)

    # compute all pairwise forces
    r_vec = pos[:,None,:] - pos[None,:,:]  # shape (n,n,2)
    dist = cp.linalg.norm(r_vec, axis=2) + eps
    cp.fill_diagonal(dist, 1.0)  # avoid self-force division
    F_mag = gamma * mass * mass.T / (dist**2)
    F_dir = r_vec / dist[:,:,None]
    forces = cp.sum(F_mag[:,:,None] * F_dir, axis=1)

    # assign forces back to bodies
    for i, b in enumerate(bodies):
        b.force = forces[i]

def update_positions(bodies):
    for b in bodies:
        acc = b.force / b.mass
        b.velocity += acc * dt
        b.pos += b.velocity * dt

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    bodies = create_random_bodies(200)

    sun = random.choice(bodies)
    sun.mass = 1e30
    sun.radius = 15
    sun.color = (255, 255, 100)
    sun.pos = cp.array([0.0, 0.0])
    sun.velocity = cp.array([0.0, 0.0])

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_forces(bodies)
        update_positions(bodies)

        screen.fill((0,0,0))
        for b in bodies:
            x = int(cp.asnumpy(b.pos[0]/1e4 + 640))
            y = int(cp.asnumpy(b.pos[1]/1e4 + 360))
            pygame.draw.circle(screen, b.color, (x,y), b.radius)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
