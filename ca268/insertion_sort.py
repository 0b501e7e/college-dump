def insertion_sort(lst):
    # At each pass ensure that that section is sorted.
    count = 0
    swapCount = 0
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        i = todo
        while i > 0 and lst[i] < lst[i-1]:
            count += 1
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            swapCount += 1
            i -= 1
    return(count + 1, swapCount)