
def find_min_max(arr):
    """
    Finds the minimum and maximum elements in an array using the 'divide and conquer' approach.
    
    :param arr: List of numbers
    :return: Tuple (min_value, max_value)
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    
    return _find_min_max_recursive(arr, 0, len(arr) - 1)

def _find_min_max_recursive(arr, left, right):
    # Base case: one element
    if left == right:
        return arr[left], arr[left]

    # Base case: two elements
    if right - left == 1:
        return (min(arr[left], arr[right]), max(arr[left], arr[right]))

    # Divide the array in half
    mid = (left + right) // 2
    left_min, left_max = _find_min_max_recursive(arr, left, mid)
    right_min, right_max = _find_min_max_recursive(arr, mid + 1, right)

    # We return the minimum and maximum of two halves
    return min(left_min, right_min), max(left_max, right_max)