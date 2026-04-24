import numpy as np
import matplotlib.pyplot as plt

def ou_forecast(x0,mu,theta,sigma,N):
    pred = []
    x = x0

    for i in range(N):

        noise = np.random.normal()
        x += theta*(mu-x) + sigma*noise
        pred.append(x)
    
    return np.array(pred)


data = np.loadtxt(r'data.dat')

x = data[:,1]

mu = np.mean(x)
x_t = x[:-1]
x_next = x[1:]

a = np.sum(x_t*x_next)/np.sum(x_t**2)
b = np.mean(x_next - a*x_t)
res = x_next-(a*x_t+b)

sigma = np.std(res)
theta = 1-a
mu = b/theta

x0 = x[-1]

pred = ou_forecast(x0,mu,theta,sigma,len(x))

plt.plot(np.arange(len(x)), x, color='k', label='Original Data')
plt.plot(np.arange(len(x), len(x)+len(pred)), pred,color='r', label='Predict')

plt.xlabel('t')
plt.ylabel(r'$\phi$')
plt.legend()
plt.show()
