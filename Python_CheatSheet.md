**Comprehensive, structured, and categorized list of built-in Python methods** that work with:

* ✅ **Strings**
* ✅ **Lists**
* ✅ **Dictionaries**
* ✅ **Sets**
* ✅ **Tuples**
* ✅ **Other Common Data Structures**

This acts as a **complete method reference guide** and is great for learning, revision, and interview prep.

---

## 🔤 STRING METHODS (`str`)

### ✅ **Case Conversion**

* `s.lower()` – lowercase
* `s.upper()` – uppercase
* `s.capitalize()` – first letter capital
* `s.title()` – title case
* `s.swapcase()` – swap upper/lower

### ✅ **Searching**

* `s.find(sub)` – returns first index or -1
* `s.index(sub)` – like find, but error if not found
* `s.count(sub)` – count occurrences
* `s.startswith(prefix)`
* `s.endswith(suffix)`

### ✅ **Modification**

* `s.replace(old, new)`
* `s.strip()` – remove spaces both sides
* `s.lstrip()` / `s.rstrip()` – left/right strip
* `s.zfill(width)` – pad with zeros

### ✅ **Splitting & Joining**

* `s.split(sep)` – split into list
* `s.rsplit(sep)`
* `s.partition(sep)` – returns (before, sep, after)
* `'sep'.join(iterable)` – joins elements with sep

### ✅ **Validation**

* `s.isalpha()` / `s.isdigit()` / `s.isalnum()`
* `s.islower()` / `s.isupper()`
* `s.isspace()` – only spaces
* `s.isnumeric()` – includes Unicode digits
* `s.isidentifier()` – valid variable name?

---

## 📋 LIST METHODS (`list`)

### ✅ **Modification**

* `lst.append(x)`
* `lst.extend(iterable)`
* `lst.insert(i, x)`
* `lst.remove(x)` – remove first occurrence
* `lst.pop(i)` – pop at index (default last)
* `lst.clear()` – remove all items

### ✅ **Info & Search**

* `lst.index(x)` – index of x
* `lst.count(x)` – number of times x occurs

### ✅ **Sorting & Reversing**

* `lst.sort()` – in-place sort
* `lst.sort(reverse=True)`
* `lst.reverse()` – in-place reverse
* `sorted(lst)` – returns new sorted list
* `reversed(lst)` – returns reverse iterator

### ✅ **Copying**

* `lst.copy()` – shallow copy
* `lst[:]` – slicing copy

---

## 📕 DICTIONARY METHODS (`dict`)

### ✅ **Access**

* `d.get(key, default)`
* `d[key]` – throws error if key not found

### ✅ **Modification**

* `d.update(other_dict)`
* `d.pop(key)` – remove key and return value
* `d.popitem()` – remove last inserted pair
* `d.setdefault(key, default)` – if key not exist, set default
* `d.clear()` – remove all items

### ✅ **Info**

* `d.keys()` – view of keys
* `d.values()` – view of values
* `d.items()` – view of (key, value) tuples
* `key in d` – check key existence

---

## 🔣 SET METHODS (`set`)

### ✅ **Modification**

* `s.add(x)`
* `s.update(iterable)`
* `s.remove(x)` – error if not found
* `s.discard(x)` – no error if not found
* `s.pop()` – remove random element
* `s.clear()`

### ✅ **Set Operations**

* `s.union(t)` or `s | t`
* `s.intersection(t)` or `s & t`
* `s.difference(t)` or `s - t`
* `s.symmetric_difference(t)` or `s ^ t`
* `s.issubset(t)`
* `s.issuperset(t)`
* `s.isdisjoint(t)`

---

## 🌀 TUPLE METHODS (`tuple`)

(Tuples are **immutable**, so methods are few.)

* `t.count(x)` – count occurrences of x
* `t.index(x)` – return index of x

---

## 📚 BUILT-IN FUNCTIONS (WORK ACROSS STRUCTURES)

### ✅ **Length & Type**

* `len(obj)`
* `type(obj)`
* `isinstance(obj, type)`

### ✅ **Conversion**

* `list()`, `dict()`, `set()`, `tuple()`, `str()`
* `int()`, `float()`, `bool()`

### ✅ **Iteration**

* `enumerate(iterable)`
* `zip(iter1, iter2)`
* `reversed(iterable)`
* `sorted(iterable)`

### ✅ **Mathematical**

* `sum(iterable)`
* `min(iterable)`
* `max(iterable)`
* `all(iterable)`
* `any(iterable)`

### ✅ **Map, Filter, Reduce**

```python
map(func, iterable)
filter(func, iterable)
from functools import reduce
reduce(func, iterable)
```

---

## 🧰 SPECIAL STRUCTURES & MODULE METHODS

### 🔹 `collections`

* `Counter()`, `defaultdict()`, `deque()`, `OrderedDict()`, `namedtuple()`

### 🔹 `heapq`

* `heappush()`, `heappop()`, `heapify()`

### 🔹 `itertools`

* `combinations()`, `permutations()`, `product()`, `groupby()`, `accumulate()`

---
