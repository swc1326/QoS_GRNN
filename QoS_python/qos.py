from grnn import *
from shell import *

import os, sys, time


########################################################################################################################

 # Total Service Response Level = 12
 # Qos Level = 1
 # Service Response Level = 7  ( Service Response = 5 )

########################################################################################################################

def qos(name,experiment):

    train_x = [[3, 5], [3, 11], [8, 6], [0, 34], [13, 3], [2, 17], [23, 2], [37, 1], [1, 40], [21, 30], [30, 24],
               [24, 64], [43, 46], [31, 51]]
    train_y = [[-3.75], [5], [-2.5], [15], [-5], [-5], [-2.5], [15], [15], [15], [15], [15], [15], [15]]
    sigma = 20.0
    pkt_loss, allocated_BW = 0.0, 0.0
    total_RAB, total_DLR = 0.0, 0.0
    AVG_RAB, AVG_DLR = 0.0, 0.0
    max_x, max_y =30, 50
    bw_rec = []
    tx_rec = []
    diff_value = [999] * 150
    flag = 1
    matrix = [-12.5, -10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10, 12.5, 15]
    response = 0
    replace = 120
    each_test_bw_value = []
    each_test_response_value = []

    start = time.time()
    for current_run in experiment:
        # Initialization
        print (name, "flag now is ", flag)
        p, q = 0, 0
        x = [[] for i in range(len(matrix))]
        y = [[] for i in range(len(matrix))]

        while p <= max_x:
            while q <= max_y:
                if (response >= 2.5 and (p + q < allocated_BW)) or (response < 2.5 and (p + q >= allocated_BW)):
                    output = grnn([p, q], train_x, train_y, sigma)[0]
                    #print("[p,q] ",[p,q])
                   # print("grnn", grnn([p, q], train_x, train_y, sigma))
                   #print("output", output)
                    compare = [(output - i) ** 2 for i in matrix]
                    #print(name, "compare output", compare)
                    qos_level = compare.index(min(compare))
                    x[qos_level].append(p)
                    y[qos_level].append(q)
                q += 0.25
            q = 0
            p += 0.25

        #print(name, "grnn output", output)

        x_1, y_1, x_7, y_7 = [], [], [], []
        for i in range(6):
            x_1 += x[i]
            y_1 += y[i]
            x_7 += x[i + 6]
            y_7 += y[i + 6]

        exp_x, exp_y = 0, 0
        if len(x_7) != 0:
            z = [x_7[i] + y_7[i] for i in range(len(x_7))]
            #print(z)
            ind = z.index(min(z))
            exp_x, exp_y = x_7[ind], y_7[ind]
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

        if allocated_BW > experiment[flag-1]:
            pkt_loss = experiment[flag-1] - allocated_BW
        # elif tx - rx > 1.5:
           # pkt_loss = tx - rx
        else:
            pkt_loss = experiment[flag-1] - allocated_BW


        response = 0

        if pkt_loss < -12.5:
            response = 15.0
        elif -12.5 <= pkt_loss < -10:
            response = 12.5
        elif -10 <= pkt_loss < -7.5:
            response = 10
        elif -7.5 <= pkt_loss < -5:
            response = 7.5
        elif -5 <= pkt_loss < -2.5:
            response = 5
        elif -2.5 <= pkt_loss < 0:
            response = 2.5
        elif 0 <= pkt_loss < 2.5:
            response = 0
        elif 2.5 <= pkt_loss < 5:
            response = -2.5
        elif 5 <= pkt_loss < 7.5:
            response = -5
        elif 7.5 <= pkt_loss < 10:
            response = -7.5
        elif 10 <= pkt_loss < 12.5:
            response = -10
        else:
            response = -12.5

        if pkt_loss < 0 and flag > 1:
            total_RAB = total_RAB + abs(pkt_loss)
        elif pkt_loss >= 0 and flag > 1:
            total_DLR = total_DLR + pkt_loss
        print ("response :",response)
        if (flag <= replace):
            train_x.append([exp_x, exp_y])
            train_y.append([response])
        elif (flag > replace):
            for i in range(len(train_x)):
                diff_value[i] = abs((sum(train_x[i]) - allocated_BW))
            for i in range(len(train_x)):
                if (sum(train_y[i]) >= 2.5 and response >= 2.5 ):
                    diff_value[i] = 999
                elif (sum(train_y[i]) < 2.5 and response < 2.5):
                    diff_value[i] = 999

            min_index = diff_value.index(min(diff_value))
            train_x[min_index] = [exp_x, exp_y]
            train_y[min_index] = [response]
            each_test_bw_value.append(train_x)
            each_test_response_value.append(train_y)
        end = time.time()
        bw_rec.append(allocated_BW)
        cost = end - start
        flag = flag + 1
    print("time :",  cost)
    print(name, "Allocated bandwidth :", bw_rec,)