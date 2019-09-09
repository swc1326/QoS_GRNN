import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from numpy import ma
import numpy as np
#
# length 為 source data 的長度(即有幾筆資料)
# bw_rec 為所有分配頻寬的紀錄[list]
# experiment 為 source data[list]
# flag 為總共執行data傳送的次數加1(所以要記得減掉)
#
def plot_diagram(length, bw_rec, experiment, flag):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x_array = np.arange(0, length)
    y_array = np.array(bw_rec)[x_array]
    z_array = np.array(experiment)[x_array]

    plt.step(x_array, y_array, where='post', label='Allocated Bandwidth')
    plt.step(x_array, z_array, where='post', label='Source Data')

    plt.xlim(0, flag-1)
    plt.ylim(45, 85)
    plt.xlabel("Flags")
    plt.ylabel("Bandwidth")
    plt.title("QoS_Simulation")

    x_locator = ticker.MultipleLocator(5.0)
    y_locator = ticker.MultipleLocator(5.0)
    ax.xaxis.set_major_locator(x_locator)
    ax.yaxis.set_major_locator(y_locator)

    plt.legend()
    plt.grid(True)
    plt.show()

# x = np.arange(1, 7, 0.5)
# y = np.sin(x)
# z = np.cos(x)
# # y = y0.copy() + 2.5

# plt.step(x, y, label='pre (default)')

# plt.step(x, y, where='mid', label='mid')

# # y = ma.masked_where((y0 > -0.15) & (y0 < 0.15), y - 0.5)
# # plt.step(x, y, label='masked (pre)')

# plt.legend() #曲線資訊標示

# plt.xlim(0, 7) #x軸的數值
# plt.ylim(-2, 2) #y軸的數值
# plt.grid(True)
# plt.show()