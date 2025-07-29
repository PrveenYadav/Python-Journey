# Python DSA Cheat Sheet

## Essential Data Structures

### Lists (Arrays)
```python
# Creation and Basic Operations
arr = [1, 2, 3]
arr.append(4)           # Add to end - O(1)
arr.insert(0, 0)        # Insert at index - O(n)
arr.pop()               # Remove last - O(1)
arr.pop(0)              # Remove at index - O(n)
arr.remove(2)           # Remove first occurrence - O(n)

# Useful Methods
len(arr)                # Length
arr.reverse()           # Reverse in-place
sorted(arr)             # Return sorted copy
arr.sort()              # Sort in-place
arr.count(x)            # Count occurrences
arr.index(x)            # Find first index

# List Comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in arr if x % 2 == 0]
```

### Strings
```python
s = "hello"
s.upper(), s.lower()    # Case conversion
s.strip()               # Remove whitespace
s.split(',')            # Split by delimiter
''.join(arr)            # Join array elements
s.find('l')             # Find substring index (-1 if not found)
s.count('l')            # Count occurrences
s.replace('l', 'x')     # Replace substring

# String slicing
s[1:4]                  # Substring
s[::-1]                 # Reverse string
```

### Dictionaries (Hash Maps)
```python
d = {}
d = dict()
d = {'a': 1, 'b': 2}

# Operations
d['key'] = value        # Set - O(1)
val = d.get('key', 0)   # Get with default - O(1)
del d['key']            # Delete - O(1)
'key' in d              # Check existence - O(1)

# Useful methods
d.keys()                # Get all keys
d.values()              # Get all values
d.items()               # Get key-value pairs
d.pop('key', default)   # Remove and return
```

### Sets
```python
s = set()
s = {1, 2, 3}

# Operations
s.add(4)                # Add element - O(1)
s.remove(2)             # Remove (KeyError if not found) - O(1)
s.discard(2)            # Remove (no error) - O(1)

# Set operations
s1 & s2                 # Intersection
s1 | s2                 # Union
s1 - s2                 # Difference
s1 ^ s2                 # Symmetric difference
```

## Advanced Data Structures

### Heaps
```python
import heapq

heap = []
heapq.heappush(heap, 3)     # Push - O(log n)
min_val = heapq.heappop(heap)  # Pop min - O(log n)
heapq.heapify(arr)          # Convert list to heap - O(n)

# For max heap, use negative values
heapq.heappush(heap, -x)
max_val = -heapq.heappop(heap)

# k largest/smallest
heapq.nlargest(k, arr)
heapq.nsmallest(k, arr)
```

### Deque (Double-ended Queue)
```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)        # Add to left - O(1)
dq.append(4)            # Add to right - O(1)
dq.popleft()            # Remove from left - O(1)
dq.pop()                # Remove from right - O(1)
```

### Counter
```python
from collections import Counter

count = Counter([1, 1, 2, 3, 3, 3])
count['1']              # Get count
count.most_common(2)    # Get 2 most common
count.update([1, 2])    # Add more elements
```

### DefaultDict
```python
from collections import defaultdict

dd = defaultdict(list)  # Default factory function
dd = defaultdict(int)   # Default to 0
dd['key'].append(1)     # Auto-creates empty list/int
```

## Common Algorithms & Techniques

### Sorting
```python
# Built-in sorting
arr.sort()                      # In-place
sorted(arr)                     # New list
sorted(arr, reverse=True)       # Descending
sorted(arr, key=len)            # Custom key function

# Custom comparator
from functools import cmp_to_key
def compare(x, y):
    return x - y
sorted(arr, key=cmp_to_key(compare))
```

### Binary Search
```python
import bisect

# Find insertion point
pos = bisect.bisect_left(arr, x)    # Leftmost position
pos = bisect.bisect_right(arr, x)   # Rightmost position

# Insert maintaining sorted order
bisect.insort(arr, x)

# Manual binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Two Pointers
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### Sliding Window
```python
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return 0
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

## Graph Algorithms

### Graph Representation
```python
# Adjacency List
graph = defaultdict(list)
graph[u].append(v)  # Add edge u -> v

# Adjacency Matrix
n = 5
graph = [[0] * n for _ in range(n)]
graph[u][v] = 1  # Add edge u -> v
```

### DFS (Depth-First Search)
```python
def dfs_recursive(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
```

### BFS (Breadth-First Search)
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## Tree Algorithms

### Binary Tree Node
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Tree Traversals
```python
# Inorder (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Preorder (Root, Left, Right)
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# Postorder (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# Level Order (BFS)
def level_order(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result
```

## Dynamic Programming Patterns

### Memoization (Top-down)
```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Using lru_cache decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cache(n):
    if n <= 1:
        return n
    return fib_cache(n-1) + fib_cache(n-2)
```

### Tabulation (Bottom-up)
```python
def fib_tab(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

## Useful Built-in Functions

### Math Operations
```python
import math

math.ceil(x)            # Ceiling
math.floor(x)           # Floor
math.sqrt(x)            # Square root
math.gcd(a, b)          # Greatest common divisor
math.inf                # Infinity
abs(x)                  # Absolute value
min(a, b, c)            # Minimum
max(a, b, c)            # Maximum
sum(arr)                # Sum of elements
```

### Itertools (Combinations & Permutations)
```python
from itertools import permutations, combinations, combinations_with_replacement

list(permutations([1, 2, 3]))               # All permutations
list(combinations([1, 2, 3, 4], 2))        # All combinations of length 2
list(combinations_with_replacement([1, 2], 2))  # With replacement
```

### String and List Operations
```python
# Zip and enumerate
for i, val in enumerate(arr):       # Index and value
for a, b in zip(arr1, arr2):        # Pair elements

# All/any
all([True, True, False])            # False
any([True, False, False])           # True

# Map and filter
list(map(str, [1, 2, 3]))          # ['1', '2', '3']
list(filter(lambda x: x > 0, arr)) # Filter positive numbers
```

## Time Complexity Quick Reference

| Operation | List | Dict | Set | Deque |
|-----------|------|------|-----|-------|
| Access    | O(1) | O(1) | -   | O(n)  |
| Search    | O(n) | O(1) | O(1)| O(n)  |
| Insert    | O(n) | O(1) | O(1)| O(1)  |
| Delete    | O(n) | O(1) | O(1)| O(1)  |

## Common Patterns & Tips

### Input Reading
```python
# Single integer
n = int(input())

# Multiple integers in one line
a, b, c = map(int, input().split())

# List of integers
arr = list(map(int, input().split()))

# Multiple lines
lines = []
for _ in range(n):
    lines.append(input().strip())
```

### Edge Cases to Consider
- Empty arrays/strings
- Single element
- All elements same
- Sorted/reverse sorted input
- Negative numbers
- Integer overflow (use `float('inf')` for large numbers)

### Python-specific Optimizations
```python
# Use list comprehensions instead of loops when possible
squares = [x*x for x in range(10)]

# Use collections.Counter for frequency counting
from collections import Counter
freq = Counter(arr)

# Use enumerate instead of range(len())
for i, val in enumerate(arr):
    # Process i and val

# Use zip for parallel iteration
for a, b in zip(arr1, arr2):
    # Process pairs
```