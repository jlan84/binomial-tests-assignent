import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
#1

# Null Hypothesis is that Muriel cannot distinguish between tea poured before milk or milk poured first

#Distribution in binomial and null P<= 0.5


# n = 137
# p = 0.5
# binomTea = stats.binom(n, p)
# pVal = 1 - binomTea.cdf(71)


# fig, ax = plt.subplots()
# ax.bar(range(72), [binomTea.pmf(i) for i in range(72)], color='red')
# ax.bar(range(72,n), [binomTea.pmf(i) for i in range(72,n)], color='blue')
# plt.show()

# print(f'The p value is {pVal:.3f}')
# print(f'Given an alpha of 0.5 we choosed to reject the null hypothesis')

#2

#Null hypothesis is that I'm not as good as i want to be
#Distribution is binomial with a null P<=50

# binomHeelFlips = stats.binom(122, p=0.5)
# pVal = 1 - binomHeelFlips.cdf(71)

# fig, ax = plt.subplots()

# ax.bar(range(72), [binomHeelFlips.pmf(i) for i in range (72)], color='red')
# ax.bar(range(72, 122), [binomHeelFlips.pmf(i) for i in range (72, 122)], color='blue')

# plt.show()

# print(pVal)
# print(f'The pVal is {pVal:.3f} and is less than the confidence level of 0.05 so we will reject the null hypothesis')

#Null hypothesis is that buses are not late 90% of the time

#Distribution is binomial and the null prob is 90%

# n = 53
# p = 0.9
# k = 49
# binomial = stats.binom(n, p)
# pVal = 1 - binomial.cdf(k-1)


# fig, ax = plt.subplots()
# ax.bar(range(k), [binomial.pmf(i) for i in range(k)], color='red')
# ax.bar(range(k,n), [binomial.pmf(i) for i in range(k,n)], color='blue')
# ax.set_xlim(30,60)
# plt.show()

# print(f'The p value is {pVal:.3f} and is less than the confidence level of 0.5 so we reject the null hypo.')


#Null hypothesis is that our programs run the first time <=5% of the time

#Distribution is binomial and the null prob is 5%

n = 6
p = 0.05
k = 1
binomial = stats.binom(n, p)
pVal = 1 - binomial.cdf(k-1)


fig, ax = plt.subplots()
ax.bar(range(k), [binomial.pmf(i) for i in range(k)], color='red')
ax.bar(range(k,n), [binomial.pmf(i) for i in range(k,n)], color='blue')
ax.set_xlim(-2,10)
plt.show()

print(f'The p value is {pVal:.3f} and is greater than the confidence level of 0.5 so we fail to reject the null.')