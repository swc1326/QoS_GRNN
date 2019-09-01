import matplotlib.pyplot as plt
import numpy as np

def plot_diagram(length, bw_rec, experiment, flag):
    x_array = np.arange(0, length)
    y_array = bw_rec
    z_array = experiment

    plt.plot(x_array, y_array, z_array)
    plt.xlim(0, flag-1)
    plt.ylim(0, 100)
    plt.xlabel("Flags")
    plt.ylabel("Allocated_BW")
    plt.title("QoS_Simulation")

    plots = plt.plot(x_array, y_array, z_array)
    plt.legend(plots, ('bw_rec', 'experiment'), loc='best', framealpha=0.5, prop={'size': 'large', 'family': 'monospace'})
    plt.grid(True)
    plt.show()