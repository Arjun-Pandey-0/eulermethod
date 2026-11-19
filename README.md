## Euler's Method 
An implementation of Euler's Method for numerically approximating solution to Ordinary Differential Equations 

# Features
*Euler's Method Solver: approximates $y(t)$ using linear approximations
*`LogisticDiffEq`: Models Logistic growth with a growth rate $r$ and carrying capacity $k$
*`ExponentialDiffEq`: Models exponential growth with growth rate $r$
*New state-of-the-art plot of the approximation over the time interval 

# How to use
In the "initialize variables" section, set the interval bymodifying `start_t` and `end_t`, change the step by editing `step`, set the initial condition by modifying `initial_cond`, and set the growth rate `r` and carrying capacity `k`
By default, it runs a logistic model. To change it to exponential, swap `LogisticDiffEq(k=k, r=r)` to `df = ExponentialDiffEq(r=r)`

# What this repository contains
1. Euler_Method.py (the actual code)
2. requirements.txt (packages needed to run this code)
3. README.md (the file you're reading right now!)
