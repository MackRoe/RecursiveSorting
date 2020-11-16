#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n log(n)) under all conditions (same as merge_sort)
    Memory usage: O(n) under worst case condition"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    left_pointer = 0
    right_pointer = 0
    arr = []
    left_arr = items1
    right_arr = items2

    while left_pointer < len(left_arr) and right_pointer < len(right_arr):
        if left_arr[left_pointer] < right_arr[right_pointer]:
            arr.append(left_arr[left_pointer])
            left_pointer += 1
        elif right_arr[right_pointer] < left_arr[left_pointer]:
            arr.append(right_arr[right_pointer])
            right_pointer += 1
        elif left_arr[left_pointer] == right_arr[right_pointer]:
            arr.append(left_arr[left_pointer])
            arr.append(right_arr[right_pointer])
            left_pointer += 1
            right_pointer += 1

    for i in range(left_pointer, len(left_arr)):
        arr.append(left_arr[i])
    for i in range(right_pointer, len(right_arr)):
        arr.append(right_arr[i])
    print('Merged array: ', arr)
    return arr


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time & Memory usage: Depend on the sort used
    """
    # TODO: Split items list into approximately equal halves
    left, right = split(items)
    # TODO: Sort each half using any other sorting algorithm
    merge_sort(left)
    merge_sort(right)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n log(n)) under all conditions
    Memory usage: O(n) under worst case condition
    """
    # Check if list is so small it's already sorted (base case)
    if is_sorted(items):
        return items

    # initialize variables
    pointer1 = 0
    pointer2 = 0

    # base case
    if len(items) == 1:  # a list of 1 is already sorted
        return array

    # split the array with helper function
    left, right = split(items)

    # recursive case
    resultleft = merge_sort(left)
    print('Result left: ', resultleft)
    resultright = merge_sort(right)
    print('Result right: ', resultright)
    return merge(resultleft, resultright)


def partition(items, start, end):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (midpoint method) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(n*m) Has while loops
    """
    # TODO: Choose a pivot any way and document your method in docstring above
    # p is partition boundary
    pivot = midpoint(items)
    pivot_value = items[pivot]
    # TODO: Loop through all items in range [low...high]
    low_index = start + 1
    high_index = end

    while low_index <= high_index and items[high_index] >= pivot:
        high_index = high_index - 1

    while low_index <= high_index and items[low_index] <= pivot:
        low_index = low_index + 1

    while high_index >= low_index:
        for value in range(len(items)):
            # TODO: Move items less than pivot into front of range [low...p-1]
            not_ready_to_swap = True
            if items[low_index] >= pivot_value:
                not_ready_to_swap = True
            else:
                low_index += 1
            # Move items greater than pivot into back of range [p+1...high]
            if items[high_index] <= pivot_value:
                if not not_ready_to_swap:
                    items[low_index], items[high_index] = items[high_index], items[low_index]
            else:
                high_index -= 1
    items[start], items[high_index] = items[high_index], items[start]
    return high_index
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: Θ(n log(n))
    Worst case running time: O(n^2)
    Memory usage: O(log(n))
    https://www.bigocheatsheet.com
    """
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)

    if not is_sorted(items):
        return items

    if low >= high:
        return

    while not is_sorted(items):
        # Partition items in-place around a pivot and get index of pivot
        # low and high
        partition_boundary = partition(items, low, high)
        p = partition_boundary
        # TODO: Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, p-1)
        quick_sort(items, p+1, high)
    return items


def split(array):
    """ Helper function: Splits an array into two arrays of approximately
    equal lenght """
    middle = midpoint(array)
    # gimmie the left chunk and the right chunk
    left_arr = left = array[0:middle + 1]
    print('Left array: ', left_arr)
    right_arr = array[middle + 1:]
    print('Right array: ', right_arr)
    return left_arr, right_arr


def midpoint(array):
    """ Helper function: Gets midpoint of an array """
    midpoint = len(array)//2
    return midpoint


def is_sorted(items):
    """Helper function: Returns a boolean indicating whether given items are in
    sorted order.
         Running time:
            O(n): All conditions - function contains only one loop"""
    if items == [] or len(items) == 1:
        return True
    for i in range(len(items)-1):
        if items[i] <= items[i+1]:
            continue
        else:
            return False
    return True


some_items = [11, 37, 47, 5, 33, 59, 15, 14, 26, 60, 28, 24]
print('Results of quick_sort:', quick_sort(some_items, 0, len(some_items) - 1))
