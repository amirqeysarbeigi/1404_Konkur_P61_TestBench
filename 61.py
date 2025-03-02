# Python Program to find maximum sum with no two adjacent using memorization

def maxSum(arr):
    n = len(arr)
  
    # Initialize memo array with -1
    memo = [-1] * (n + 1)
    return maxSumRec(arr, n, memo)


def maxSumRec(arr, n, memo):
    if n <= 0:
        return 0
    if n == 1:
        return arr[0]

    # Check if the result is already computed
    if memo[n] != -1:
        return memo[n]

    pick = arr[n - 1] + maxSumRec(arr, n - 2, memo)
    notPick = maxSumRec(arr, n - 1, memo)

    # Store the max of two choices in the memo array and return it
    memo[n] = max(pick, notPick)
    return memo[n]


def test_max_sum_recursive():
    # Test Case 1: Empty array
    nums = []
    assert maxSum(nums) == 0, "Test Case 1 Failed"
    print("Test Case 1 Passed")

    # Test Case 2: Single element
    nums = [5]
    assert maxSum(nums) == 5, "Test Case 2 Failed"
    print("Test Case 2 Passed")

    # Test Case 3: Two elements
    nums = [2, 7]
    assert maxSum(nums) == 7, "Test Case 3 Failed"
    print("Test Case 3 Passed")

    # Test Case 4: Three elements (optimal solution involves skipping one element)
    nums = [2, 7, 9]
    assert maxSum(nums) == 11, "Test Case 4 Failed"
    print("Test Case 4 Passed")

    # Test Case 5: Multiple elements (optimal solution involves skipping some elements)
    nums = [2, 7, 9, 3, 1]
    assert maxSum(nums) == 12, "Test Case 5 Failed"
    print("Test Case 5 Passed")

    # Test Case 6: All elements are the same
    nums = [4, 4, 4, 4, 4]
    assert maxSum(nums) == 12, "Test Case 6 Failed"
    print("Test Case 6 Passed")

    # Test Case 7: Optimal solution involves selecting alternating elements
    nums = [5, 1, 1, 5]
    assert maxSum(nums) == 10, "Test Case 7 Failed"
    print("Test Case 7 Passed")

    # Test Case 8: Larger array
    nums = [6, 7, 1, 3, 8, 2, 4, 9, 21, 12, 6, 10]
    assert maxSum(nums,) == 50, "Test Case 8 Failed"
    print("Test Case 8 Passed")

    # Test Case 9: Array with increasing values
    nums = [1, 2, 3, 4, 5, 6]
    assert maxSum(nums) == 12, "Test Case 9 Failed"
    print("Test Case 9 Passed")

    # Test Case 10: Array with decreasing values
    nums = [6, 5, 4, 3, 2, 1]
    assert maxSum(nums) == 12, "Test Case 10 Failed"
    print("Test Case 10 Passed")

    print("All Test Cases Passed!")

# Run the test bench
test_max_sum_recursive()