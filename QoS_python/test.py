# def hello(input):
#     output = "Hello " + input + "!!"
#     print (output)

# if __name__ == '__main__':
#     raw_input()
#     hello("Shang")

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,360)
y = np.sin(x * np.pi / 180.0)
z = np.sin(x * np.pi / 90.0)

plt.plot(x,y)
plt.plot(x,z)
plt.xlim(-30, 390)
plt.ylim(-1.5, 1.5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("The Title")

# plots = plt.plot(x, y)
# plt.legend(plots, ('Apple', 'Facebook', 'Google'), loc='best', framealpha=0.5, prop={'size': 'large', 'family': 'monospace'})
plt.grid(True)
plt.show()