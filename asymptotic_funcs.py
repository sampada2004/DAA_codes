import math
import matplotlib.pyplot as plt
r1=[i for i in range (1,101,10)]
r2=[i for i in range(1,200,10)]
log_arr=[math.log(i,2) for i in r1]
lin_arr=[i for i in r1]
lin_logarr=[i*math.log(i,2) for i in r1]
quad_arr=[i**2 for i in r1]
cubic_arr=[i**3 for i in r1]
exp_arr=[math.pow(2,i) for i in r1]
fac=[math.factorial(i) for i in r1]
plt.plot(r1,log_arr)
plt.plot(r1,lin_arr)
plt.plot(r1,lin_logarr)
plt.plot(r1,quad_arr)
plt.plot(r1,cubic_arr)
plt.plot(r1,exp_arr)
plt.plot(r1,fac)
plt.ylim(0,1000)
plt.show()