def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        merge_sort(left)
        merge_sort(right)
        
        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1

if __name__ == "__main__":
    """
    [3,5,6,1,2,7,9,8]

    left = [3,5,6,1]
    i, j, k = 0, 0, 0
        left = [3,5]
        i, j, k = 0, 0, 0
        
        right = [6,1]
        i, j, k = 0, 0, 0
    
    right = [2,7,9,8]
    i, j, k = 0, 0, 0
        left = [2,7]
        i, j, k = 0, 0, 0

        right = [9,8]
        i, j, k = 0, 0, 0

    """
    lst = [3,5,6,1,2,7,9,8]
    merge_sort(lst)
    print(lst)