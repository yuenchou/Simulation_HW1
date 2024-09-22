import numpy as np

def monte_carlo_integration(f, a, b, num_samples, round):
    """
    使用蒙特卡羅方法估算定積分 ∫_a^b f(x) dx
    param f: 被積分的函數
    param a: 積分區間下界
    param b: 積分區間上界
    param num_samples: 隨機樣本數量
    return: 積分值的近似
    """
    # 生成 num_samples 個隨機樣本點
    x_samples = np.random.uniform(a, b, num_samples)
    # 計算這些樣本點上的函數值
    f_samples = f(x_samples)
    # 計算樣本點的平均值
    average_value = np.mean(f_samples)
    # 積分近似值
    integral_estimate = (b - a) * average_value
    print(f"EST{round + 1} : {integral_estimate}")
    return integral_estimate

# 積分函數
def f(x):
    return (1/(2*np.pi)**0.5)*np.e**((-x**2)/2)

# 設置參數
a = 1
b = 2
num_samples = 10
repeat_time = 5
integral_value = []


# 估算積分

# 重複做5組積分
for i in range(repeat_time):
    temp = monte_carlo_integration(f, a, b, num_samples, i)
    integral_value.append(temp)


average_I = sum(integral_value)/repeat_time
print(f"AVG : {average_I}")

variance_I = 0

for j in integral_value:
    variance_I += (j - average_I)**2

variance_I = variance_I/repeat_time

print(f"variance of I : {variance_I}")