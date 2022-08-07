# Enter your code here. Read input from STDIN. Print output to STDOUT
# true population distribution
pop_mean, pop_std = 500, 80

# sample mean distribution
sample_mean, sample_std = pop_mean, pop_std/(100**0.5)

# confidence intervals of sample mean dist
A = pop_mean - (1.96*sample_std)
B = pop_mean + (1.96*sample_std)

print(round(A,2))
print(round(B,2))