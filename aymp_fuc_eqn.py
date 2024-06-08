import numpy as np
import matplotlib.pyplot as plt

def f(n):
    return 7 * n + 5

def g(n):
    return n

def plot_graph(n0):
    n_values = np.arange(1, 20)
    f_values = f(n_values)
    c_times_g = 8 * g(n_values)

    plt.plot(n_values, f_values, label='f(n) = 7n + 5')
    plt.plot(n_values, c_times_g, label='c * g(n)')

    plt.axvline(x=n0, color='r', linestyle='--', label='n0')

    plt.xlabel('n')
    plt.ylabel('f(n)')
    plt.title('Plot of f(n) and c * g(n)')
    plt.legend()
    plt.grid(True)
    plt.show()
def drawtable():
    for i in range(1,11):
        print(i , 7*i+5 ,8*i)
def find_n0():
    n0 = 1
    
    while True:
        if f(n0) <= 8 * g(n0):
            return n0
        n0 += 1
        

n0 = find_n0()
drawtable()
print("n0 value:", n0)
plot_graph(n0)
