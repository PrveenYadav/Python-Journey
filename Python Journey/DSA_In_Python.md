Here's your **Python DSA Cheat Sheet** to make the transition smooth and efficient. Print this or save it as a quick reference!  

---

# **🐍 Python DSA Cheat Sheet**  
*(For Interview Prep & LeetCode Grinding)*  

## **📌 Basic Syntax (vs C++)**
| **Concept**       | **C++**                          | **Python**                      |
|-------------------|----------------------------------|---------------------------------|
| Loop              | `for(int i=0; i<n; i++)`         | `for i in range(n):`            |
| Dynamic Array     | `vector<int> v;`                 | `list = []`                     |
| Hashmap           | `unordered_map<int, int> mp;`    | `dict = {}`                     |
| String Concatenate| `s1 + s2`                        | `s1 + s2` (or `f"{s1}{s2}"`)    |
| Sort              | `sort(arr.begin(), arr.end());`   | `arr.sort()`                    |

---

## **🔥 Top Data Structures in Python**
### **1. List (Dynamic Array)**
```python
nums = [1, 2, 3]
nums.append(4)       # [1, 2, 3, 4]
nums.pop()           # [1, 2, 3] (last element removed)
nums.insert(1, 99)   # [1, 99, 2, 3]
nums.sort()          # [1, 2, 3, 99]
```

### **2. Dictionary (Hashmap)**
```python
hashmap = {"a": 1, "b": 2}
hashmap["c"] = 3     # {"a":1, "b":2, "c":3}
if "a" in hashmap:   # Key check
    print(hashmap["a"])
```

### **3. Set (Unique Elements)**
```python
unique = set()
unique.add(1)        # {1}
unique.add(1)        # Still {1}
```

### **4. Heap (Priority Queue)**
```python
import heapq
min_heap = [3, 1, 2]
heapq.heapify(min_heap)  # Converts list to heap
heapq.heappop(min_heap)  # Returns 1 (smallest)
```

---

## **⚡ Must-Know Python Tricks for DSA**
### **1. List Slicing**
```python
arr = [1, 2, 3, 4, 5]
print(arr[1:4])      # [2, 3, 4] (sublist from index 1 to 3)
print(arr[::-1])     # [5, 4, 3, 2, 1] (reverse list)
```

### **2. Lambda Functions (Quick Sorting)**
```python
# Sort list of tuples by second element
pairs = [(1, 4), (2, 3), (3, 2)]
pairs.sort(key=lambda x: x[1])  # [(3,2), (2,3), (1,4)]
```

### **3. Counter (Frequency Map)**
```python
from collections import Counter
arr = [1, 1, 2, 3]
freq = Counter(arr)  # {1:2, 2:1, 3:1}
```

### **4. Defaultdict (Avoid KeyErrors)**
```python
from collections import defaultdict
dd = defaultdict(int)
dd["a"] += 1   # No KeyError, initializes to 0
```

---

## **📌 Python vs C++: Key DSA Differences**
| **Operation**       | **C++**                     | **Python**                   |
|----------------------|-----------------------------|------------------------------|
| **Stack**            | `stack<int> s; s.push(x);`  | `stack = []; stack.append(x)`|
| **Queue**            | `queue<int> q; q.push(x);`  | `from collections import deque; q = deque()` |
| **String Manipulation** | `s.substr(pos, len)`     | `s[start:end]`               |
| **Binary Search**    | `binary_search(arr.begin(), arr.end(), x)` | `bisect.bisect_left(arr, x)` |

---

## **🚀 Next Steps**
1. **Practice 50 LeetCode Easy** problems in Python (focus on lists, dicts, strings).  
2. **Learn `collections` module** (`deque`, `Counter`, `defaultdict`).  
3. **Use Pythonic tricks** (list comprehensions, slicing) to write concise code.  

---

### **💡 Pro Tip:**  
- **Python is slower than C++**, but **interviewers care about logic, not speed**.  
- **Use Python for interviews**, but keep C++ for CP (if needed).  

**Need a list of Python DSA practice problems?** Let me know! 😊  

(Print this or save as PDF for quick reference!)