import numpy as np

print("NumPy Array Transformer\n")

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original 2D Array: \n {arr}\n")
print(f"Shape of the array: \n {arr.shape}\n")

Arr_1D = np.array([10, 20, 30, 40, 50, 60])
reshape_arr = Arr_1D.reshape(3, 2)
print(f"Reshaped Array (1D -> 2D): \n {reshape_arr}\n")

print("Iterating through Reshaped Array:")
for x in reshape_arr:
    for y in x:
        print(y, "\n")

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
join_arr = np.concatenate((arr1, arr2))
print(f"Joined Array: \n {join_arr}\n")

split_arr = np.array_split(join_arr, 4)
print(f"Splitted Arrays: \n {split_arr}\n")
