import numpy as np
import matplotlib.pyplot as plt

#read input signal from csv
csv = np.genfromtxt('signal_input.csv', delimiter=',')
signal_size = len(csv[:, 1])

true_val = csv[:, 0] 

#state variables and transitions matrices
z = csv[:, 1]
x = [0 for k in range(0, signal_size)]

A = 1
H = 1

G = 0

P = [0 for k in range(0, signal_size)]
Q = 0.5
R = 200

I = 1

#kalman filter
x[0] = z[0]

for k in range(1, signal_size):
    #predict
    x[k] = x[k-1] + 5
    P[k] = P[k-1] + Q 

    #update
    G = (P[k] * H) / (H * P[k] * H + R)
    x[k] = x[k] + G * (z[k] - H * x[k])
    P[k] = (I - G * H) * P[k]

#plot
plt.figure()
plt.plot(true_val)
plt.plot(z)
plt.plot(x)
plt.legend(['true value', 'raw value', 'filtered value'], loc='upper left')
plt.show()
