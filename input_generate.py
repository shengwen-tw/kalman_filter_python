import numpy as np
import matplotlib.pyplot as plt

input_size = 500
step_size = 5
noise_mean = 0
noise_var = 100

#generate input signal for kalman filter
x_input_true = np.zeros(input_size)
x_input_noise = np.zeros(input_size)
csv = []
for x in range(0, input_size):
    #true value, no noise
    x_input_true[x] = (step_size * x)
    #generated signal, with noise
    x_input_noise[x] = x_input_true[x] + np.random.normal(noise_mean, noise_var)

    csv.append([x_input_true[x], x_input_noise[x]])

#save input signal as csv file
np.savetxt('signal_input.csv', csv, delimiter=",", fmt='%.3f')

plt.figure()
plt.plot(x_input_true)
plt.plot(x_input_noise)
plt.legend(['w/o noise', 'w/ noise'], loc='upper left')
plt.show()
