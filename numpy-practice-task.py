import numpy as np
# task ===> 1
array = np.array([10,20,30,40,50])
print(array.sum())
print(array.mean())
print(array.max())
print(array.min())  

# task ===> 2
array2 = np.array([45,80,30,90,55,20])
print(array2[array2 >= 50])
# task ==>  3
array3 = np.array([1,2,3,4,5,6])
new_array = array3.reshape(2,3)
print(new_array)
