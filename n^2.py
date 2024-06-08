import numpy as np
import matplotlib.pyplot as plt
def f(n):
    return 7*n**2+n+5
c1=6
c2=8
def plot_func(n_values):
    plt.figure(figsize=(10,6))
    plt.plot(n_values,f(n_values),label='f(n)=7n^2+n+5',color='blue')
    plt.plot(n_values,c1*n_values**2,label='c1*n^2',linestyle='--',color='red')
    plt.plot(n_values,c2*n_values**2,label='c2*n^2',linestyle='--',color='green')
    plt.xlabel('n')
    plt.ylabel('func value')
    plt.legend()
    plt.show()
def drawtable():
    for i in range(1,11):
        print(i , 7*i**2+i+5,6*i**2,8*i**2)    
def find_n0():
    n=1
    
    while True:
        if c1*n**2<=f(n)<=c2*n**2:
            return n
        n+=1
n_values=np.arange(0,4)
plot_func(n_values)
drawtable()
n0=find_n0()
print("n0 :",n0)            