import numpy as np
import matplotlib.pyplot as plt

p_tunnel = np.loadtxt('../data_files/pressure_trades/p_tunnel.txt', delimiter = '\t')
Re = np.loadtxt('../data_files/pressure_trades/Re.txt', delimiter = '\t')
A_tube = np.loadtxt('../data_files/pressure_trades/A_tube.txt', delimiter = '\t')
T_tunnel = np.loadtxt('../data_files/pressure_trades/T_tunnel.txt', delimiter = '\t')
L_pod = np.loadtxt('../data_files/pressure_trades/L_pod.txt', delimiter = '\t')
power = np.loadtxt('../data_files/pressure_trades/comp_power.txt', delimiter = '\t')
steady_vac = np.loadtxt('../data_files/pressure_trades/vac_power.txt', delimiter = '\t')
total_energy = np.loadtxt('../data_files/pressure_trades/total_energy.txt', delimiter = '\t')

fig = plt.figure(figsize = (3.25,3.5), tight_layout = True)
ax = plt.axes()
plt.setp(ax.get_xticklabels(), fontsize=8)
plt.setp(ax.get_yticklabels(), fontsize=8)
plt.plot(p_tunnel, A_tube, 'b-', linewidth = 2.0)
plt.xlabel('Tube Pressure (Pa)', fontsize = 10, fontweight = 'bold')
plt.ylabel('Tube Area (m^2)', fontsize = 10, fontweight = 'bold')
plt.savefig('../graphs/pressure_trades/pressure_vs_Area.png', format = 'png', dpi = 300)
plt.show()

fig = plt.figure(figsize = (3.25,3.5), tight_layout = True)
ax = plt.axes()
plt.hold(True)
plt.subplot(211)
line1, = plt.plot(p_tunnel, steady_vac, 'g-', linewidth = 2.0, label = 'Vaccum Power')
line2, = plt.plot(p_tunnel, power, 'b-', linewidth = 2.0, label = 'Compressor Power')
plt.ylabel('Power (hp)', fontsize = 10, fontweight = 'bold')
plt.legend(handles = [line1, line2], loc = 1, fontsize = 8)
plt.subplot(212)
plt.plot(p_tunnel, total_energy/(1.0e6), 'r-', linewidth = 2.0)
plt.xlabel('Tube Pressure (Pa)', fontsize = 10, fontweight = 'bold')
plt.ylabel('Total Energy Cost \n per Year (Million USD)', fontsize = 10, fontweight = 'bold')
plt.savefig('../graphs/pressure_trades/pressure_vs_power.png', format = 'png', dpi = 300)
plt.show()