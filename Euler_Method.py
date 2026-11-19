import numpy as np
import matplotlib.pyplot as plt

# Intialize variables
start_t = 0
end_t = 50
step = 1
initial_cond = 1000
k = 6000
r = 0.15

class LogisticDiffEq:
    def __init__(self, k, r):
        self.k = k
        self.r = r
    def __call__(self, x):
        return x * (1 - x / self.k) * self.r

class ExponentialDiffEq:
    def __init__(self, r):
        self.r = r
    def __call__(self, x):
        return x * self.r

df = LogisticDiffEq(k=k, r=r)

y_vals = list([initial_cond])
t_vals = np.arange(start_t, end_t+1, step=step)

for i, t in enumerate(t_vals[1:]):
    new_y = y_vals[i] + df(y_vals[i]) * step
    y_vals.append(new_y)

plt.plot(t_vals, y_vals)
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.title("Euler's Method Approximation")
plt.show()

print(f"Last Value: {y_vals[len(y_vals)-1]}")