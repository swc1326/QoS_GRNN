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

# import math

# while True:
#     output = float(input("Please enter your output: "))

#     if (output - (-12.5)) <= 0:
#         qos_level = 0
#     elif (output - (-12.5)) > 25:
#         qos_level = 11
#     else:
#         qos_level = math.ceil((output - (-12.5))/2.5)

#     print("QoS Level = ", qos_level + 1)

# while True:
#     output = float(input("Please enter your output: "))
#     matrix = [-12.5, -10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10, 12.5, 15]
#     compare = [(output - i) ** 2 for i in matrix]                    
#     qos_level = compare.index(min(compare))
#     print("QoS Level = ", qos_level + 1)
import os

max_x, max_y = 15, 25

response = float(input("Please enter your response: "))
allocated_BW = float(input("Please enter your allocated_BW: "))

if (response >= 0): #給太多，所以這次的搜尋範圍就不超過上次的allocated_BW
    print("Too Much !")
    p, q = 0, 0
    while p <= max_x:
        while q <= max_y:
            #if (response >= 7.5 and (p + q < allocated_BW)) or (response < 7.5 and (p + q >= allocated_BW)):
            print("p =", p, ", q =", q)
            os.system("pause")
            if (q < allocated_BW and p + q < allocated_BW):
                q += 0.25
            else:
                break
        q = 0
        if (p < allocated_BW):
            p += 0.25

else: #給太少，所以這次的搜尋範圍就從上次的allocated_BW開始找起
    print("Too Less !")
    if (max_y < allocated_BW): #q_max < allocated_BW
        p = allocated_BW - max_y
        q = max_y
        q_pointer = max_y
    else: #q_max > allocated_BW
        p = 0
        q = allocated_BW
        q_pointer = allocated_BW

    while p <= max_x:
        while q <= max_y:
            #if (response >= 7.5 and (p + q < allocated_BW)) or (response < 7.5 and (p + q >= allocated_BW)):
            print("p =", p, ", q =", q)
            os.system("pause")
            q += 0.25
        q = q_pointer
        p += 0.25