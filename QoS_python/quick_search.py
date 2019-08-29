from grnn import *
from shell import *
from qos import *
import os, sys, time

import numpy as np
import math
#import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    #experiment = [8.572942708333334, 11.820104166666667, 6.179583333333333, 11.6615625, 6.565442708333333, 11.162135416666667, 10.816484375, 11.587447916666667, 11.043020833333335, 11.858437499999999, 8.111484375, 7.220078125, 7.182291666666667, 7.919973958333333, 7.2616927083333325, 4.674270833333334, 5.792682291666668, 6.876041666666666, 8.340286458333333, 7.454557291666667, 8.189427083333333, 9.116249999999999, 11.627395833333333, 11.660729166666668, 9.037942708333333, 10.467994791666667, 8.225859375, 10.390885416666668, 7.416796875, 8.617421875, 7.1078906250000005, 11.665885416666667, 10.854322916666668, 9.460807291666667, 8.652682291666666, 9.501223958333334, 7.416432291666666, 11.002395833333333, 10.73765625, 8.228229166666667, 10.661171874999999, 6.875703125, 6.606458333333333, 6.257942708333334, 11.511510416666667, 7.487239583333334, 10.042083333333332, 8.072604166666666, 7.106901041666667, 11.133828124999999, 11.666067708333335, 11.471770833333332, 8.844348958333333, 9.386744791666667, 10.620234375, 8.653046875000001, 11.510260416666668, 11.355208333333332, 9.500026041666667, 8.574322916666668]
    #experiment = [11.615807291666664, 7.246510416666666, 8.973463541666668, 7.248229166666666, 11.542239583333334, 10.890026041666665, 8.932864583333334, 4.716458333333334, 8.933359375, 11.540625, 7.935286458333334, 4.562135416666667, 7.16921875, 7.822369791666667, 7.1342968749999995, 4.676953125, 5.712213541666666, 4.638723958333333, 8.166536458333333, 4.6020312500000005, 7.246588541666667, 4.677864583333334, 11.544010416666666, 11.464609375, 9.009453125, 10.236901041666668, 11.577682291666667, 4.600911458333333, 7.361744791666666, 4.715729166666667, 6.901510416666667, 11.500677083333334, 10.620703125, 9.315911458333332, 8.550130208333334, 9.199557291666666, 7.400104166666666, 10.968645833333333, 10.659322916666667, 8.164375, 10.35328125, 6.861562499999999, 6.557369791666666, 6.095078125000001, 11.462005208333332, 7.285052083333333, 9.892760416666667, 8.053125, 7.0160156250000005, 11.042838541666667, 11.502734375000001, 11.271041666666667, 8.743098958333334, 9.317864583333332, 10.580546875, 8.548489583333334, 11.390677083333335, 11.1196875, 9.431875, 8.471041666666666]
    experiment = [54.132734375000005, 54.10684895833333, 54.143541666666664, 58.758098958333335, 54.110963541666671, 54.147343749999997, 58.905833333333334, 54.184791666666662, 58.846536458333333, 58.826171875, 64.036640625000004, 64.11908854166667, 68.639427083333331, 73.961197916666663, 73.877369791666666, 49.042005208333336, 49.038619791666662, 49.058463541666669, 54.112031250000001, 54.171822916666663, 54.122447916666665, 54.152187499999997, 54.138697916666672, 54.171145833333334, 54.124843749999997, 54.168776041666668, 58.909348958333332, 54.092994791666662, 54.140130208333325, 54.203151041666665, 54.158307291666667, 54.158125000000005, 54.149479166666673, 54.189270833333332, 54.150729166666657, 54.120130208333336, 54.132734375000005, 54.112786458333325, 54.120859375000002, 54.132760416666663]

    train_x = [[3, 5], [3, 11], [8, 6], [0, 34], [13, 3], [2, 17], [23, 2], [37, 1], [1, 40], [21, 30], [30, 24],
               [24, 64], [43, 46], [31, 51]]
    train_y = [[-3.75], [5], [-2.5], [15], [-5], [-5], [-2.5], [15], [15], [15], [15], [15], [15], [15]]
    sigma = 20.0
    max_x, max_y =30, 50
    pkt_loss, allocated_BW = 0.0, 0.0
    
    bw_rec = []

    diff_value = [999] * 150 #還是不太懂為啥這樣設定diff_value = [999, 999, ..., 999]
    flag = 1
    num_of_level = 12
    response = 0
    replace = 30 #profile size

    for current_run in experiment: #len(experiment) = 40
        # Initialization
        print ("flag now is ", flag)
        print ("data is ", current_run)
        
        L1 = [ [] for i in range(num_of_level) ] #link 1 的頻寬, p
        L2 = [ [] for i in range(num_of_level) ] #link 2 的頻寬, q

        # p, q = 0, 0
        # while p <= max_x:
        #     while q <= max_y:
        #         if (response >= 7.5 and (p + q < allocated_BW)) or (response < 7.5 and (p + q >= allocated_BW)):
        #             output = grnn([p, q], train_x, train_y, sigma)[0] #output = [y*], 單位為Mbps

        #             if (output - (-12.5)) <= 0:
        #                 qos_level = 0
        #             elif (output - (-12.5)) > 25:
        #                 qos_level = 11
        #             else:
        #                 qos_level = math.ceil((output - (-12.5))/2.5)
                    
        #             L1[qos_level].append(p)
        #             L2[qos_level].append(q)
        #         q += 0.25
        #     q = 0
        #     p += 0.25

        if (response > 7.5): #給太多，所以這次的搜尋範圍就不超過上次的allocated_BW - 5
            print("Response Over 7.5!")
            os.system("pause")
            p, q = 0, 0 #這個起始值還可以再調整!!!!!
            while p <= max_x:
                while q <= max_y:
                    print("p =", p, ", q =", q)
                    output = grnn([p, q], train_x, train_y, sigma)[0] #output = [y*], 單位為Mbps
                    if (output - (-12.5)) <= 0:
                        qos_level = 0
                    elif (output - (-12.5)) > 25:
                        qos_level = 11
                    else:
                        qos_level = math.ceil((output - (-12.5))/2.5)
                    L1[qos_level].append(p)
                    L2[qos_level].append(q)

                    if ((q < allocated_BW and p + q < allocated_BW) or (allocated_BW == 0.0)):
                        # print("q += 0.25 !")
                        q += 0.25
                    else:
                        # print("break !")
                        break
                q = 0
                if ((p < allocated_BW) or (allocated_BW == 0.0)):
                    p += 0.25
                # os.system("pause")

        elif (response < 5): #給太少，所以這次的搜尋範圍就從上次的allocated_BW + 7.5開始找起
            print("Response less than 5!")
            os.system("pause")
            if (max_y < allocated_BW): #q_max < allocated_BW
                p = allocated_BW - max_y + 7.5
                q = max_y
                q_pointer = max_y
            else: #q_max > allocated_BW
                p = 0
                q = allocated_BW + 7.5
                q_pointer = allocated_BW + 7.5

            while p <= max_x:
                while q <= max_y:
                    print("p =", p, ", q =", q)
                    output = grnn([p, q], train_x, train_y, sigma)[0] #output = [y*], 單位為Mbps
                    if (output - (-12.5)) <= 0:
                        qos_level = 0
                    elif (output - (-12.5)) > 25:
                        qos_level = 11
                    else:
                        qos_level = math.ceil((output - (-12.5))/2.5)
                    L1[qos_level].append(p)
                    L2[qos_level].append(q)

                    q += 0.25
                q = q_pointer
                p += 0.25
                # os.system("pause")

        else:
            print("5 <= Response <= 7.5!")
            os.system("pause")
            if (max_y < allocated_BW - 5): #q_max < allocated_BW
                p = allocated_BW - 5 - max_y
                q = max_y
                q_pointer = max_y
            else: #q_max >= allocated_BW
                p = 0
                q = allocated_BW - 5
                q_pointer = allocated_BW -5

            while p <= max_x:
                while q <= max_y:
                    print("p =", p, ", q =", q)
                    output = grnn([p, q], train_x, train_y, sigma)[0] #output = [y*], 單位為Mbps
                    if (output - (-12.5)) <= 0:
                        qos_level = 0
                    elif (output - (-12.5)) > 25:
                        qos_level = 11
                    else:
                        qos_level = math.ceil((output - (-12.5))/2.5)
                    L1[qos_level].append(p)
                    L2[qos_level].append(q)

                    if (p + q < allocated_BW + 7.5):
                        q += 0.25
                    else:
                        break

                q = q_pointer
                if (p + q < allocated_BW + 7.5):
                    p += 0.25
                else:
                    break
                # os.system("pause")

        x_1, y_1, x_9, y_9 = [], [], [], [] #這邊訂x_9為QoS Level 2的設定。 

        for i in range(0, 8): #這部分會判斷為Bad
            x_1 += L1[i] #分配給Link 1且被判斷為Service Response Level 1~8的所有頻寬
            y_1 += L2[i] #分配給Link 2且被判斷為Service Response Level 1~8的所有頻寬

        for i in range(8, 12): #這部分會判斷為Excellent
            x_9 += L1[i] #分配給Link 1且被判斷為Service Response Level 9~12的所有頻寬 #9~12為QoS Level 2
            y_9 += L2[i] #分配給Link 2且被判斷為Service Response Level 9~12的所有頻寬

        exp_x, exp_y = 0, 0

        if len(x_9) != 0:
            z = [x_9[i] + y_9[i] for i in range(len(x_9))] #x_9[i] + y_9[i]為Link 1與Link 2的頻寬總和
            #print(z)
            ind = z.index(min(z)) #找出頻寬總和最小的組合
            exp_x, exp_y = x_9[ind], y_9[ind]
            print("Link 1 :", exp_x, " Link 2 :", exp_y)
            print ("Excellent")

        else:
            z = [x_1[i] + y_1[i] for i in range(len(x_1))]
            #print(z)
            ind = z.index(max(z))
            exp_x, exp_y = x_1[ind], y_1[ind]
            print (" Link 1 :",exp_x," Link 2 :", exp_y)
            print ("Bad")

        allocated_BW = exp_x + exp_y
        print ("allocated_BW :", allocated_BW)

        pkt_loss = experiment[flag-1] - allocated_BW
        response = -(pkt_loss)
        print ("response :", response)

        if (len(train_x) < replace): #profile放滿之前都可以直接放到profile中
            train_x.append([exp_x, exp_y])
            train_y.append([response])

        else: #profile放滿之後，
            for i in range(len(train_x)):
                diff_value[i] = abs((sum(train_x[i]) - allocated_BW))
                #diff_value = [999, 999, ..., 999] #((p + q) - allocated_BW)的絕對值
                #目的是找出train_x[]中所存的頻寬分配與最新的allocated_BW的差值
            
            for i in range(len(train_x)):
                if (sum(train_y[i]) >= 7.5 and response >= 7.5 ):
                    diff_value[i] = 999
                elif (sum(train_y[i]) < 7.5 and response < 7.5):
                    diff_value[i] = 999

            #找diff_value最小的index，將新值存入該index的位子做替換
            min_index = diff_value.index(min(diff_value))
            train_x[min_index] = [exp_x, exp_y]
            train_y[min_index] = [response]

        print("Data in Profile :", len(train_x))
        print()
        os.system("pause")

        bw_rec.append(allocated_BW)
        flag = flag + 1
    
    print("Done")
    print("Source Data Rate", experiment)
    print("Allocated Bandwidth", bw_rec)

    x_array = np.arange(0, len(experiment))
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