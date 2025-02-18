def merge_sort(arr):

    if len(arr) < 2:
        return arr

    m = len(arr)//2

    larr = merge_sort(arr[:m])
    rarr = merge_sort(arr[m:])

    merge_arr = []

    l = r = 0

    while l < len(larr) and r < len(rarr):
        if larr[l] < rarr[r]:
            merge_arr.append(larr[l])
            l += 1
        else:
            merge_arr.append(rarr[r])
            r += 1
    
    merge_arr += larr[l:]
    merge_arr += rarr[r:]

    return merge_arr




if __name__ == '__main__':
    arr = [10,15,3,4,5,6,21,1,2]
    print(merge_sort(arr))