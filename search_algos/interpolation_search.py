"""
Interpolation Search Algorithm

# All algorithm is depend on this formula

Formula = low + ((skey-lst[low])*(high-low) / (lst[high]-lst[low]))

Time Complexity: O(n)
"""

def interpolationSearch(lst, skey):
    low = 0
    high = len(lst) - 1
    while low<=high and skey>=lst[low]:
        index = int(low + ((skey-lst[low])*(high-low) / (lst[high]-lst[low])))
        print((low + ((skey-lst[low])*(high-low) / (lst[high]-lst[low]))))
        if lst[index] == skey:
            return index
        else:
            low += 1

*arr, = range(500)
print(arr)

while True:
    num = int(input("Enter number:"))
    if num == 0:
        break

    startTime = time.time()

    print(interpolationSearch(arr, num))
    
    endTime = time.time() - startTime
    
    print("/--------Interpolation Search Algorithm------------/", endTime)
