import math

def activator(data, train_x, sigma): #data = [p, q]  #train_x = [3, 5]
    distance = 0
    for i in range(len(data)): #0 -> 1
        distance += math.pow(data[i] - train_x[i], 2) # 計算 D() 函式
    return math.exp(-distance / (math.pow(sigma, 2))) # 最後返回 W() 函式


def grnn(data, train_x, train_y, sigma): #data = [p, q] #train_x = [[3, 5], [3, 11], ...]
    result = []
    out_dim = len(train_y[0]) # 檢查 train_y 的維度
    for dim in range(out_dim):
        factor, divide = 0, 0
        for i in range(len(train_x)): #0 -> 13
            cache = activator(data, train_x[i], sigma) # cache 儲存 W() 函式
            factor += train_y[i][dim] * cache # train_y * W() 函式累加，公式中的分子
            divide += cache # W() 函式累加，公式中的分母
        result.append(factor / divide) # 最終的預測值[list]
    return result # 返回預測值[list]，result = [y*]