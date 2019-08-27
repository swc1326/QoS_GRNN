# # def hello(input):
# #     output = "Hello " + input + "!!"
# #     print (output)

# # if __name__ == '__main__':
# #     raw_input()
# #     hello("Shang")

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(0,360)
# y = np.sin(x * np.pi / 180.0)
# z = np.sin(x * np.pi / 90.0)

# plt.plot(x,y)
# plt.plot(x,z)
# plt.xlim(-30, 390)
# plt.ylim(-1.5, 1.5)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("The Title")

# # plots = plt.plot(x, y)
# # plt.legend(plots, ('Apple', 'Facebook', 'Google'), loc='best', framealpha=0.5, prop={'size': 'large', 'family': 'monospace'})
# plt.grid(True)
# plt.show()

import math

while True:
    output = float(input("Please enter your output: "))

    if (output - (-12.5)) <= 0:
        qos_level = 0
    elif (output - (-12.5)) > 25:
        qos_level = 11
    else:
        qos_level = math.ceil((output - (-12.5))/2.5)

    print("QoS Level = ", qos_level + 1)

# while True:
#     output = float(input("Please enter your output: "))
#     matrix = [-12.5, -10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10, 12.5, 15]
#     compare = [(output - i) ** 2 for i in matrix]                    
#     qos_level = compare.index(min(compare))
#     print("QoS Level = ", qos_level + 1)