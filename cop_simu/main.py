import numpy as np
import matplotlib.pyplot as plt

T_hot = np.linspace(20,40,500)
T_cold = np.linspace(22,32,500)

eps = 0.1 #handle singularity at 0,0 and where T_hot = T_cold
η = 0.4 #Efficiency, can be left out, reported BTU in units is likely to be efficiency corrected from idealized carnot-cycle


BTU = 12000 #hardcoded BTU can be tweaked in code to generate per rating

T_IN, T_OUT = np.meshgrid(T_cold,T_hot)
print(f"T diff: {T_OUT-T_IN}")
# ideal carnot cycle
COP = (T_IN+273.15)/(T_OUT-T_IN+eps)

COP_eff = COP*η
COP_eff = np.clip(COP_eff, 0, 20)

eff_BTU = COP_eff * BTU

#°C pasted here so I don't have to look for it again
plt.contourf(T_OUT, T_IN, COP_eff, levels=20, cmap='RdYlGn')
plt.colorbar(label='COP')
plt.xlabel('Outside temp (°C)')
plt.ylabel('Inside temp (°C)')
plt.title('Heat pump COP')
plt.savefig('cop_plot.png', dpi=150, bbox_inches='tight')