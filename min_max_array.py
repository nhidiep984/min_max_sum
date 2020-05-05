def min_max_sum(arr):
    if len(arr) == 5:
        for i, num in enumerate(arr):
            current_value = arr[i]
            position = i - 1
            while position >= 0 and arr[position] > current_value:
                arr[position+1] = arr[position]
                position -= 1
            arr[position + 1] = current_value
        sorted_array = arr
        min_array = arr[0:-1] 
        max_array = arr[1:]
        min_sum = sum(min_array)
        max_sum = sum(max_array)
        print(min_sum, max_sum)
    else:
        print("Array length is not equal to 5.")

""" 
Since the instructions said the function must include for/while loops, I sorted the array with an
insertion sort, instead of using Python's sorted method. After that, I sliced the sorted array, so that
the subarray(max_array) didn't include the min value of the sorted array and vice versa. I then found 
the sum of both the min_array and max_array. Since the function is supposed to be given an array of 5 numbers,
I made if/else statements so that if the input array didn't have 5 elements, the function would not run. 


Possible test cases for this function:
1. Assert that if the length of the input array is not 5, then the print statement in else-statement
will print out to the console.
2. Verify that the array length of both min_array and max_array are 4. 
3. Verify that the length of the sorted_array is still 5.
4. Verify that the max value of the sorted_array is at index 4 and the min value is at index 0
5. Verify that sum(sorted_array) - min_sum == max(sorted_array)
6. Verify that sum(sorted_array) - max_sum == min(sorted_array)
7. Test with negative values and zero. """

nums = [3, 1, 7, 5, 9]
min_max_sum(nums)
