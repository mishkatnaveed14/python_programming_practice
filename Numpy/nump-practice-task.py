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
# task ==> 4
marks = np.random.randint(40,100,10)
average = marks.mean()
higest_marks = marks.max()
lowest_marks = marks.min()
print(f"Marks: {marks}")
print(f"Average : {average}")
print(f"Higest Marks : {higest_marks}")
print(f"lowest Marks : {lowest_marks}")

# task ===> 5 
