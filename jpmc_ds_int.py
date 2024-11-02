"""
Given an array of numbers, find the index of the smallest array element(the pivot), 
for which the sum of all elements to the left and to the right are equal. 
The array may not be reordered. 
Ex. arr=[1,2,3,4,6] 
The sum of the first 3 elements, 1+2+3=6. 

The value of the last element is 6. Using zero based indexing, arr[3]=4 is the pivot between two subarrays. 
The index of the pivot is 3. 

Function description 
Complete the function balancedSum in the editor below. 
balancedSum has the following parameters: int arr[n]: an array of integers Returns: int: an integer representing the index of the pivot. 

Constraints: 
3<= n <= 10^5, 1<=arr[i]<=2 * 10^4, where 0 <=i<n, it is guaranteed a solution always exists
"""
def balancedSum(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]

"""
Given a range of integers, determine how many numbers have no repeating digits. 
example: n=80, m=120. 
The lower and upper bounds are inclusive so there are 120-79=41 values in the range. 
Numbers without repeating characters are normal weight and others are bold. 
The two columns to the right are the valid number counts per row(normal weight) and invalid number counts(bold). 
80, 81, 82, 83, 84, 85, 86, 87, 88(bold), 89, 1(bold) 
90, 91, 92, 93, 94, 95, 96, 97, 98, 99(bold), 9, 1(bold) 
100(bold), 101(bold), 102, 103, 104, 105, 106, 107, 108, 109, 8, 2(bold) 
110(bold), 111(bold), 112(bold),113(bold), 114(bold), 115(bold), 116(bold), 117(bold), 118(bold), 119(bold), 0, 10bold 
120, 1, 0(bold) 

There are 27 numbers with no repeating digits, and 14 other numbers in the range. 
Print 27 
Function description 
Complete the function countNumbers in the editor below. 
countNumbers has the following parameters: 
- int arr[q][2]: integer pairs representing inclusive lower (n) and upper (m) range limits 
- Print for each pair arr[i], print the number of integers in the inclusive range that qualify. 
- There is no value to return from the function 
Constraints 
- 1<=q<=10^5 1<=n<=m<=10^6

"""

def has_no_repeating_digits(num):
    num_str = str(num)
    return len(num_str) == len(set(num_str))

def precompute_counts(limit):
    counts = [0] * (limit + 1)
    for num in range(1, limit + 1):
        counts[num] = counts[num - 1] + (1 if has_no_repeating_digits(num) else 0)
    return counts

def countNumbers(arr):
    limit = 1000000
    counts = precompute_counts(limit)
    
    results = []
    for n, m in arr:
        if n == 0:
            results.append(counts[m])
        else:
            results.append(counts[m] - counts[n - 1])
    
    for result in results:
        print(result)

if __name__ == '__main__':
    arr_rows = int(input().strip())
    arr_columns = int(input().strip())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    countNumbers(arr)