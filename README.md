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
