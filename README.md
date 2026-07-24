# ieeSimu

Trivial engineering/physics simulations. Each lives in its own flat directory with a venv, Python code, and output plots. Major simulations get their own repositories.

## License

MIT

---

## Simulations

### [`cop_simu/`](cop_simu/) — Heat Pump COP

Computes and plots the Coefficient of Performance (COP) of a heat pump across a grid of indoor/outdoor temperatures using the ideal Carnot cycle, scaled by an efficiency factor.

**Model:**

- COP = T_cold / (T_hot − T_cold), temperatures in Kelvin
- Applied efficiency factor η = 0.4 (approximate real-world correction from ideal Carnot)
- Singularity at T_hot = T_cold handled with a small epsilon offset

**Parameters (hardcoded in `main.py`):**

| Parameter | Value    | Description                                         |
| --------- | -------- | --------------------------------------------------- |
| `T_hot`   | 20–40 °C | Outside (heat source/sink) temperature range        |
| `T_cold`  | 22–32 °C | Inside (conditioned space) temperature range        |
| `η`       | 0.4      | Carnot efficiency correction factor                 |
| `BTU`     | 12000    | Nominal rating (BTU/h) for effective output scaling |

**Output:** `cop_plot.png` — filled contour plot of COP over the temperature grid.

**Dependencies:** numpy, matplotlib (see `requirements.txt`)

### [`nbody_simu/`](nbody_simu/) — 2D N-Body Gravity Simulation

Simulates and animates the gravitational interaction of N bodies in 2D using Newtonian mechanics, rendered live with pygame.

**Model:**

- Pairwise Newtonian gravity: F = G·m₁·m₂ / (r² + ε), softened with a small epsilon to avoid singularities at close range
- Semi-implicit Euler integration: velocity updated from acceleration, then position updated from velocity
- Bodies are randomly generated with masses, positions, velocities, and colors

**Files:**

| File                 | Description                                                             |
| -------------------- | ------------------------------------------------------------------------ |
| `nbodysim_cpu.py`    | Reference implementation using numpy (runs anywhere)                     |
| `nbodysim_cuda.py`   | GPU-accelerated variant using cupy for vectorized pairwise force calculation |

**Parameters (hardcoded):** gravitational constant `gamma`, timestep `dt`, softening `eps`, body count (default 100)

**Dependencies:** numpy, pygame (see `requirements.txt`). The cuda variant additionally requires `cupy`, matched to your local CUDA driver version — not pinned in `requirements.txt` since it's hardware-specific.

### [`plane_generator/`](plane_generator/) — 3D Plane Generator & Visualizer

Generates a random plane through three random points in 3D and visualizes it as a surface.

**Model:**

- Three random points P0, P1, P2 sampled with integer coordinates in [1, 10)
- Plane normal computed via the cross product of edge vectors (P1−P0) × (P2−P0)
- Surface plotted over a grid by solving the plane equation for Z (or a flat Z=0 plane if the normal has no Z-component)

**Output:** Interactive 3D matplotlib plot showing the plane surface and the three defining points.

**Dependencies:** numpy, matplotlib (see `requirements.txt`)
