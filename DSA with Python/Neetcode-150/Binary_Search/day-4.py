# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.store = {} # key : [[val, timestamps], [val, timestamps], ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        values = self.store.get(key, [])
        left, right = 0, len(values)-1

        while left <= right:
            mid = left + (right-left)//2
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                left = mid+1
            else:
                right = mid-1
        return ans


if __name__ == "__main__":
    myObj = TimeMap()

    """
    Input: ["TimeMap", "set", "get", "get", "set", "get", "get"]

    [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    
    Output: [null, null, "bar", "bar", null, "bar2", "bar2"]

    """