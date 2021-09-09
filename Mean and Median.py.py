import numpy as np 
data = [23,45,67,54,66,77,323,11,32,18]

print("mean:", np.mean(data))
print("median:", np.median(data))
print("25th percentile is..", np.percentile(data,25))
print("50 th percentile is...", np.percentile(data,50))