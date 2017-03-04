from random import choice 
from numpy import array, dot

unit_step = lambda x: 1 if x > 0.5 else 0

training_data = [ (array([0,0,1]), 1), 
                 (array([0,1,1]), 1), 
                 (array([1,0,1]), 1), 
                 (array([1,1,1]), 0),]

w = [1,0,0]
print(w)
errors = [] 
eta = 0.1 
n = 100

for i in range(n): 
    x, expected = choice(training_data) 
    result = dot(w, x) 
    error = expected - unit_step(result) 
    errors.append(error) 
    w += eta * error * x
    
for x, _ in training_data:
    result = dot(x, w) 
    print(w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))