import scipy.stats as stats
import matplotlib.pyplot as plt
import math

def calc_p_value(n, value, p_null=0.5):
    binomial = stats.binom(n=n, p=p_null)
    return 1 - binomial.cdf(value-1)

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

def determine_n(max_iter, p_val):
    x = 1
    while x < max_iter:
        p = calc_p_value(x, x*0.52)
        if p < p_val:
            print(f'The number of test required to get a p value < {p_val} is {x}')
            break
        x += 1
            





if __name__ == '__main__':

    print(calc_p_value(137, 72))
    right = [calc_p_value(n, round(n*0.52)) for n in range(1,10000)]
    fig, ax = plt.subplots()
    ax.bar(range(1,10000), right, align="center", color='grey')
    # plt.show()
    #3
    lst = [0.2, 0.1, .05]
    max_iter = 2500
    for val in lst:
        determine_n(max_iter, val)