# Basic Array Problems

class Solution:
    #constructor
    # def __init__(self):
    #     pass
    
    def maxAndMin(self, arr):
        max = 0
        min = arr[0]
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
            elif arr[i] < min:
                min = arr[i]
        return {min, max}

    def reverseArray(self, arr):
        i, j = 0, len(arr)-1
        while i<j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr

    def missingInArray(self, arr):
        seen = set(arr)
        for i in range(1, len(arr)+1):
            if i not in seen:
                return i
        return -1

    def countCharFreq(self, s, c):
        freq = 0
        for i in range(len(s)):
            if s[i] == c:
                freq += 1
        return freq

    def removeDuplicatesSorted(self, arr):
        i = 0
        n = len(arr)-1
        while i < n:
            if arr[i] == arr[i+1]:
                arr.remove(arr[i])
                n -= 1
            i += 1
        return arr
    
    def removeDuplicates(self, arr):
        ans = set()
        for i in range(len(arr)):
            ans.add(arr[i])
        return ans
    
    def removeDuplicates1(self, arr):
        ans = []
        for num in arr:
            if num not in ans:
                ans.append(num)
        return ans[::-1]

    # Time and space o(n)
    def rotateArrayLeftByk(self, arr, k):
        n = len(arr)
        if n == 0: return arr
        k = k % n #if n > k then always k % n = k
        ans = arr[k:] + arr[:k]
        return ans

    # Inplace rotation: Time O(n) and space O(1)
    def rotateArray(self, arr, k):
        n = len(arr)
        if n == 0: return
        k = k % n
        
        # Helper function to Reverse
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        reverse(0, k-1) # Reverse first k elements      
        reverse(k, n-1) # Reverse remaining elements
        reverse(0, n-1) # Reverse entire array
        return arr

    def mergeTwoArray(self, arr1, arr2):
        return sorted(arr1+arr2)

    def mergeTwoSortedArray(self, arr1, arr2):
        ans = []
        n, m = len(arr1), len(arr2)
        i = j = 0

        while i < n and j < m:
            if arr1[i] < arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1
        
        ans.extend(arr1[i:])
        ans.extend(arr2[j:])
        return ans


def main():
    arr = [3, 7, 0, 1, 4, 2, 5, 0]
    k = 2
    arr1 = [1, 1, 2, 3, 3, 4, 5, 5]
    s = "Hellowhatisgoingon"
    c = 'o'

    my_obj = Solution()
    print(my_obj.missingInArray(arr))
    print(my_obj.maxAndMin(arr))
    print(my_obj.reverseArray(arr))
    print(my_obj.countCharFreq(s, c))
    print(my_obj.removeDuplicatesSorted(arr1))
    print(my_obj.removeDuplicates(arr))
    print(my_obj.removeDuplicates1(arr))
    print(my_obj.rotateArrayLeftByk(arr, k))
    print(my_obj.rotateArray(arr, k))
    list1 = [4, 6, 8]
    list2 = [5, 7, 9]
    print(my_obj.mergeTwoArray(list1, list2))
    print(my_obj.mergeTwoSortedArray(list1, list2))


if __name__ == "__main__":
    main()
