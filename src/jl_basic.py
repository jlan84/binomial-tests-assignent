import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

"""
#1 Binomially distributed because each of the die are equivalent to a roll in 
the bucket and each number has an equal chance of being rolled n= 1256, p=1/6
k=4

#2 Not binomially distributed because not all of the die have the same probability
 this is conditional distribution where the probability of rolling a 4 depends
 on the number of each die.  Utilize Bayes Theorem

#3 Binomiall distributed n=100, p= 17/40

#4 Hypergeometric N=40, K=17, n=7

#5 p = 1/6*0.9 n = 1256

#6 p = (.8*17 + 0.1*16 + 0.1*18)/40 n = 100

"""

def calc_p_value(model, value):
    print(f'The p values is: {1 - model.cdf(value-1):.4f}')
    
    return 1 - model.cdf(value-1)

def plot_model(ax, model, n, lo, value):
    bars = ax.bar(range(n+1), [model.pmf(i) for i in range(n+1)], align="center",
                  color='grey')
    ax.set_xlim(lo, n +10)
    for i in range(value, n+1):
        bars[i].set_color('red')

def pipeline(ax, model, n, lo, value, threshold):
    plot_model(ax, model, n, lo, value)
    p = calc_p_value(model, value)
    if p < threshold:
        print('Reject Null Hypothesis')
    else:
        print('Fail to Reject Null Hypothesis')


if __name__ == "__main__":
    # Part 2

    #1  Null hypothesis is that Muriel cannot tell if the water was poured before of
    # after the milk.  Binomial. Faled to reject null p = 30.4%

    binomial = stats.binom(n=137, p=0.5)
    
    fig, ax = plt.subplots()
    pipeline(ax, binomial, 137, 40, 72, 0.05)
    
    #2 Null hypothesis is that we  haven't progressed on our heelflip capability
    # Rejected null p = 2.8%

    n = 122
    value = 72
    p = 0.5
    threshold = .05

    binomial = stats.binom(n=n, p=p)
    
    fig, ax = plt.subplots()
    pipeline(ax, binomial, n, 40, value, threshold)
    

    #3 Null hypothesis is that the buses are late 90% of the time alternative
    # hypthesis is that the buses are late less than 90% of the time. Failed to
    # Reject p = 37.8%

    n = 53
    value = 49
    p = 0.9
    threshold = .05
    binomial = stats.binom(n=n, p=p)
    
    fig, ax = plt.subplots()
    pipeline(ax, binomial, n, 11, value, threshold)
    

    #4 Null hypothesis is that more than 5% of your programs run the first time
    # alternative hypo is that less than 5% of your programs run the first time
    # p value = 26.5% Reject Null

    n = 6
    value = 1
    p = .05
    threshold = .05
    binomial = stats.binom(n=n, p=p)

    fig, ax = plt.subplots()
    pipeline(ax, binomial, n, -5, value, threshold)
    plt.show()


    
    


