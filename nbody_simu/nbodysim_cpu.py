import pygame
import math
import random
import numpy as np

gamma = 6.6743*10**(-11)
dt = 0.01
eps = 0.005

class Body:
    def __init__(self,mass,velocity,position,radius,color):
        
        self.pos = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass
        self.radius = radius
        self.color = color
        self.force = np.zeros(2)
    def UpdateForce(self, other_bodies, gamma):
        self.force = np.zeros(2)
        for other in other_bodies:
            if other is self:
                continue
            r_vec = other.pos - self.pos
            dist = np.linalg.norm(r_vec)
            if dist > 0:
                F_mag = gamma * self.mass * other.mass / (dist**2 + eps)
                self.force += F_mag * r_vec / dist

    def Update(self,dt):
        acc = self.force/self.mass #F=ma
        self.velocity += acc*dt #From the ODE for motion v' = a*dt
        self.pos += self.velocity*dt #From the ODE for motion x' = v*dt


def create_random_bodies(n=5):
    bodies = []
    for i in range(n):
        m = random.uniform(1e20, 1e26)
        # spread positions visually (meters)
        pos = (random.uniform(-5e6, 5e6), random.uniform(-5e6, 5e6))
        vel = (random.uniform(-1e5, 1e5), random.uniform(-1e5, 1e5))
        col = (random.randint(100,255), random.randint(100,255), random.randint(100,255))
        radius = max(3, int(4 + np.log10(m) - 22))
        bodies.append(Body(mass=m, position=pos, velocity=vel, radius=radius, color=col))
    return bodies


def main():   
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    screen.fill((0, 0, 0))
    bodies = create_random_bodies(100)

    pygame.display.flip()  # update the display
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for b in bodies:
            b.UpdateForce(bodies, gamma)
        for b in bodies:
            b.Update(dt)

        screen.fill((0, 0, 0))
        for b in bodies:
            pygame.draw.circle(
                screen,
                b.color,
                (int(b.pos[0]/1e4 + 640), int(b.pos[1]/1e4 + 360)),
                b.radius
            )
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
    