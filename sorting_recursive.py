#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    left_pointer = 0
    right_pointer = 0
    arr = []

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
    return arr


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    left, right = split(items)
    # TODO: Sort each half using any other sorting algorithm

    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

    # initialize variables
    pointer1 = 0
    pointer2 = 0

    # base case
    if len(array) == 1:  # a list of 1 is already sorted
        return array

    # split the array with helper function
    left, right = split(items)

    # recursive case
    resultleft = merge_sort(left)
    resultright = merge_sort(right)
    return merge(resultleft, resultright)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    pivot = midpoint(items)
    pivot_value = items[pivot]
    # TODO: Loop through all items in range [low...high]
    low_range = range(pivot - 1)
    high_range = range(pivot +1, len(items))
    left_pointer = 0
    right_pointer = len(items)-1
    for value in range(len(items)):
        # TODO: Move items less than pivot into front of range [low...p-1]
        if items[left_pointer] >= pivot_value:
            prepare_to_swap = True
        else:
            left_pointer += 1
        # TODO: Move items greater than pivot into back of range [p+1...high]
        if items[right_pointer] <= pivot_value:
            if prepare_to_swap:
                items[left_pointer], items[right_pointer] = items[right_pointer], items[left_pointer]
        else:
            right_pointer -= 1
    return pivot
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    if len(items) <= 1:
        sorted = True
        return items
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


def split(array):
    middle = midpoint(array)
    # gimmie the left chunk and the right chunk
    left_arr = left = array[0:middle + 1]
    right_arr = array[middle + 1:]
    return left_arr, right_arr


def midpoint(array):
    midpoint = len(array)//2
    return midpoint
