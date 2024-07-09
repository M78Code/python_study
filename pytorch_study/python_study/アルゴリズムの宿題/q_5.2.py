import scipy.stats as stats

# 总共掷骰子的次数
n = 3

# 每次掷骰子出现1的概率
p = 1 / 6

# 定义二项分布
binom_dist = stats.binom(n, p)

# P(X = 0): 出现0次1的概率
P_X_0 = binom_dist.pmf(0)

# P(X <= 2): 出现0次，1次或2次1的概率之和
P_X_le_2 = binom_dist.cdf(2)

# P(X 是奇数): 出现1次或3次1的概率之和
P_X_odd = binom_dist.pmf(1) + binom_dist.pmf(3)

# 输出结果
print(P_X_0)
print(P_X_le_2)
print(P_X_odd)

