import numpy as np
def zero_padding(arr, index, num_zeros):
    current_length = len(arr)
    if index < 0 or index > current_length:
        print("Invalid index.")
        return arr
    padded_arr = np.concatenate((arr[:index],np.zeros(num_zeros),arr[index:]))
    return padded_arr

# Example usage:
original_array = [1, 2, 3, 4, 5]
padded_array = zero_padding(original_array, 1, 10)
print("Original Array:", original_array)
print("Padded Array:", padded_array)