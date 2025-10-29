# Sorting And Searching

class solution:

    def bubbleSort(self, arr):
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if arr[i] == arr[j] or arr[i] < arr[j]:
                    continue
                else:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr
    
    def selectionSort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr
    
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            current = arr[i]
            j = i-1
            while j >= 0 and current < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = current
        return arr
                
    def binarySearch(self, arr, target):
        start, end = 0, len(arr)-1
        while start <= end:
            mid = (start+end)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return -1

    def firstOccurance(self, arr, val):
        for i in range(len(arr)-1):
            if arr[i] == val:
                return i
            
    def lastOccurance(self, arr, val):
        ans = 0
        for i in range(len(arr)-1):
            if arr[i] == val:
                ans = i
                continue
        return ans

    def peakElement(self, arr):
        peak = arr[0]
        for i in range(len(arr)):
            if arr[i] > peak:
                peak = arr[i]
        return peak


def main():
    my_obj = solution()
    arr = [5, 3, 1, 9, 2, 4]
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    arr2 = [1, 2, 2, 2, 2, 3, 4, 4, 5]

    print(my_obj.bubbleSort(arr))
    print(my_obj.selectionSort(arr))
    print(my_obj.insertionSort(arr))

    print(my_obj.binarySearch(arr1, 3))
    print(my_obj.firstOccurance(arr2, 4))
    print(my_obj.lastOccurance(arr2, 2))
    print(my_obj.peakElement(arr))


if __name__ == "__main__":
    main()