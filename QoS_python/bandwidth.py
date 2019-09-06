#
#def bandwidth(L1, L2)  #L1與L2為兩個Link的頻寬預測值
#   return result       #result[0]為最終決定的預測值，result[1]為最終預測值的總和allocated_BW
#

def bandwidth(L1, L2, d):
    x_1, y_1, x_9, y_9 = [], [], [], [] #這邊訂x_9為QoS Level 2的設定。
    result = []

    for i in range(0, 8): #這部分會判斷為Bad
        x_1 += L1[i] #分配給Link 1且被判斷為Service Response Level 1~8的所有頻寬
        y_1 += L2[i] #分配給Link 2且被判斷為Service Response Level 1~8的所有頻寬

    for i in range(8, 12): #這部分會判斷為Excellent
        x_9 += L1[i] #分配給Link 1且被判斷為Service Response Level 9~12的所有頻寬 #9~12為QoS Level 2
        y_9 += L2[i] #分配給Link 2且被判斷為Service Response Level 9~12的所有頻寬 
    # print("len(x_1) :", len(x_1), " len(x_9) :", len(x_9))        

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
        print ("Link 1 :", exp_x," Link 2 :", exp_y)
        print ("Bad")

    result.append([exp_x, exp_y])
    allocated_BW = exp_x + exp_y
    print ("allocated_BW :", allocated_BW)

    result.append(allocated_BW)
    return result