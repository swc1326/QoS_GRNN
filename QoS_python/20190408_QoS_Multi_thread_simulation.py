from grnn import *
from shell import *
from qos import *
import os, sys, time

if __name__ == '__main__':

    #experiment = [8.572942708333334, 11.820104166666667, 6.179583333333333, 11.6615625, 6.565442708333333, 11.162135416666667, 10.816484375, 11.587447916666667, 11.043020833333335, 11.858437499999999, 8.111484375, 7.220078125, 7.182291666666667, 7.919973958333333, 7.2616927083333325, 4.674270833333334, 5.792682291666668, 6.876041666666666, 8.340286458333333, 7.454557291666667, 8.189427083333333, 9.116249999999999, 11.627395833333333, 11.660729166666668, 9.037942708333333, 10.467994791666667, 8.225859375, 10.390885416666668, 7.416796875, 8.617421875, 7.1078906250000005, 11.665885416666667, 10.854322916666668, 9.460807291666667, 8.652682291666666, 9.501223958333334, 7.416432291666666, 11.002395833333333, 10.73765625, 8.228229166666667, 10.661171874999999, 6.875703125, 6.606458333333333, 6.257942708333334, 11.511510416666667, 7.487239583333334, 10.042083333333332, 8.072604166666666, 7.106901041666667, 11.133828124999999, 11.666067708333335, 11.471770833333332, 8.844348958333333, 9.386744791666667, 10.620234375, 8.653046875000001, 11.510260416666668, 11.355208333333332, 9.500026041666667, 8.574322916666668]
    #experiment = [11.615807291666664, 7.246510416666666, 8.973463541666668, 7.248229166666666, 11.542239583333334, 10.890026041666665, 8.932864583333334, 4.716458333333334, 8.933359375, 11.540625, 7.935286458333334, 4.562135416666667, 7.16921875, 7.822369791666667, 7.1342968749999995, 4.676953125, 5.712213541666666, 4.638723958333333, 8.166536458333333, 4.6020312500000005, 7.246588541666667, 4.677864583333334, 11.544010416666666, 11.464609375, 9.009453125, 10.236901041666668, 11.577682291666667, 4.600911458333333, 7.361744791666666, 4.715729166666667, 6.901510416666667, 11.500677083333334, 10.620703125, 9.315911458333332, 8.550130208333334, 9.199557291666666, 7.400104166666666, 10.968645833333333, 10.659322916666667, 8.164375, 10.35328125, 6.861562499999999, 6.557369791666666, 6.095078125000001, 11.462005208333332, 7.285052083333333, 9.892760416666667, 8.053125, 7.0160156250000005, 11.042838541666667, 11.502734375000001, 11.271041666666667, 8.743098958333334, 9.317864583333332, 10.580546875, 8.548489583333334, 11.390677083333335, 11.1196875, 9.431875, 8.471041666666666]
    #experiment = [54.132734375000005, 54.10684895833333, 54.143541666666664, 58.758098958333335, 54.110963541666671, 54.147343749999997, 58.905833333333334, 54.184791666666662, 58.846536458333333, 58.826171875, 64.036640625000004, 64.11908854166667, 68.639427083333331, 73.961197916666663, 73.877369791666666, 49.042005208333336, 49.038619791666662, 49.058463541666669, 54.112031250000001, 54.171822916666663, 54.122447916666665, 54.152187499999997, 54.138697916666672, 54.171145833333334, 54.124843749999997, 54.168776041666668, 58.909348958333332, 54.092994791666662, 54.140130208333325, 54.203151041666665, 54.158307291666667, 54.158125000000005, 54.149479166666673, 54.189270833333332, 54.150729166666657, 54.120130208333336, 54.132734375000005, 54.112786458333325, 54.120859375000002, 54.132760416666663]
    experiment = [54.132734375000005, 54.10684895833333 ]

    train_x = [[3, 5], [3, 11], [8, 6], [0, 34], [13, 3], [2, 17], [23, 2], [37, 1], [1, 40], [21, 30], [30, 24],
               [24, 64], [43, 46], [31, 51]]
    train_y = [[-3.75], [5], [-2.5], [15], [-5], [-5], [-2.5], [15], [15], [15], [15], [15], [15], [15]]
    sigma = 20.0
    pkt_loss, allocated_BW = 0.0, 0.0
    total_RAB, total_DLR = 0.0, 0.0
    AVG_RAB, AVG_DLR = 0.0, 0.0
    max_x, max_y =20, 40
    
    bw_rec = []
    tx_rec = []

    diff_value = [999] * 150 #還是不太懂為啥這樣設定diff_value = [999, 999, ..., 999]
    flag = 1
    matrix = [-12.5, -10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10, 12.5, 15]
    response = 0
    replace = 30 #profile size
    each_test_bw_value = []
    each_test_response_value = []

    for current_run in experiment: #len(experiment) = 40
        # Initialization
        print ("flag now is ", flag)
        p, q = 0, 0
        x = [ [] for i in range(len(matrix)) ] #link 1 的頻寬, p #len(matrix) = 12
        y = [ [] for i in range(len(matrix)) ] #link 2 的頻寬, q

        while p <= max_x:
            while q <= max_y:
                #從
                if (response >= 7.5 and (p + q < allocated_BW)) or (response < 7.5 and (p + q >= allocated_BW)):
                    output = grnn([p, q], train_x, train_y, sigma)[0] #output = [y*], 單位為Mbps
                    compare = [(output - i) ** 2 for i in matrix]                    
                    qos_level = compare.index(min(compare)) #這裡的qos_level是指Service Response Level 1 -> 12
                    
                    x[qos_level].append(p)
                    y[qos_level].append(q)
                q += 0.25
            q = 0
            p += 0.25

        # print("x[] = ", x)
        # print("y[] = ", y)
        # os.system("pause")
        x_1, y_1, x_9, y_9 = [], [], [], []


        for i in range(0, 8): #這部分會判斷為Bad
            x_1 += x[i] #分配給Link 1且被判斷為Service Response Level 1~8的所有頻寬
            y_1 += y[i] #分配給Link 2且被判斷為Service Response Level 1~8的所有頻寬

        for i in range(8, 12): #這部分會判斷為Excellent
            x_9 += x[i] #分配給Link 1且被判斷為Service Response Level 9~12的所有頻寬 #9~12為QoS Level 2
            y_9 += y[i] #分配給Link 2且被判斷為Service Response Level 9~12的所有頻寬

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

        pkt_loss = experiment[flag-1] - allocated_BW #好像不用if判斷式
        # pkt_loss > 0 表示給得頻寬不夠
        # pkt_loss < 0 表示給得頻寬太多        
        
        # if allocated_BW > experiment[flag-1]:
        #     pkt_loss = experiment[flag-1] - allocated_BW
        # # elif tx - rx > 1.5:
        #    # pkt_loss = tx - rx
        # else:
        #     pkt_loss = experiment[flag-1] - allocated_BW

        response = 0 #用來判斷這次的頻寬分配好與壞

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
        print ("response :", response)

        if (flag <= replace): #profile放滿之前都可以直接放到profile中
            train_x.append([exp_x, exp_y])
            train_y.append([response])

        elif (flag > replace): #profile放滿之後，
            for i in range(len(train_x)): #len(train_x) = 14
                diff_value[i] = abs((sum(train_x[i]) - allocated_BW)) #diff_value = [999, 999, ..., 999] #((p + q) - allocated_BW)的絕對值
            
            for i in range(len(train_x)):
                if (sum(train_y[i]) >= 7.5 and response >= 7.5 ):
                    diff_value[i] = 999                    
                elif (sum(train_y[i]) < 7.5 and response < 7.5):
                    diff_value[i] = 999

            min_index = diff_value.index(min(diff_value))
            train_x[min_index] = [exp_x, exp_y]
            train_y[min_index] = [response]
            each_test_bw_value.append(train_x)
            each_test_response_value.append(train_y)
        bw_rec.append(allocated_BW)
        flag = flag + 1
    
    print("Done");
    print("Source Data Rate",experiment) ;
    print("Allocated Bandwidth",bw_rec) ;
