import unidecode

def mergeSort(arr):
    sorted_list = arr
    if len(sorted_list) > 1:
        mid = len(sorted_list) // 2
        left = sorted_list[:mid]
        right = sorted_list[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if unidecode.unidecode(left[i]['name']) < unidecode.unidecode(right[j]['name']):
              sorted_list[k] = left[i]
              i += 1
            else:
                sorted_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            sorted_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            sorted_list[k]=right[j]
            j += 1
            k += 1

    return sorted_list