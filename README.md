## Notes for Coding Interviews/Assessments 

This assumes you are using python 3 for your coding interviews/assessments. We will first breakdown all the components you should be made aware of before diving deep.

- Big O Notation
- Data Structures and Algorithms
- Navigating Online Assessments and Coding Interviews

## Big O Notation Explained

Big O describes how a solution's running time (time complexity) or memory use (space complexity) grows as the input size `n` grows. It ignores constants and lower-order terms: `3n + 10` is just `O(n)`. Interviewers usually care about the worst case.

### Common complexities (best to worst)

| Big O | Name | Typical example |
|-------|------|-----------------|
| O(1) | Constant | Hash map lookup, array index, stack push/pop |
| O(log n) | Logarithmic | Binary search (halving the input each step) |
| O(√n) | Square root | Checking whether a number is prime by trial division up to its square root |
| O(n) | Linear | Single loop over an array, e.g. Two Sum with a hash map |
| O(n log n) | Linearithmic | Sorting (`sorted()`, `.sort()`), heap-based top-k |
| O(n²) | Quadratic | Nested loops over the same input, brute-force pair checks |
| O(n³) | Cubic | Three nested loops, naive matrix multiplication |
| O(2ⁿ) | Exponential | Naive recursion over subsets, naive Fibonacci |
| O(n!) | Factorial | Generating all permutations |
| O(nⁿ) | Super-exponential | Rare; brute-force over every arrangement with repetition |

### Rules of thumb

- **Drop constants:** `O(2n)` → `O(n)`.
- **Drop lower-order terms:** `O(n² + n)` → `O(n²)`.
- **Sequential steps add:** a loop followed by another loop is `O(n + m)`.
- **Nested steps multiply:** a loop inside a loop is `O(n * m)`.
- **Different inputs get different variables:** looping over two arrays is `O(a + b)`, not `O(n)`.
- **Space counts too:** a hash set holding every element is `O(n)` space, two pointers is `O(1)`.

### Python operation costs

| Operation | Cost |
|-----------|------|
| `list[i]`, `list.append(x)`, `list.pop()` | O(1) |
| `list.pop(0)`, `list.insert(0, x)`, `x in list` | O(n) |
| `list.sort()`, `sorted(list)` | O(n log n) |
| `dict[key]`, `x in dict`, `x in set` | O(1) average |
| `set.add(x)`, `dict[key] = v` | O(1) average |
| `collections.deque.append / popleft` | O(1) |
| `heapq.heappush / heappop` | O(log n) |
| `heapq.heapify(list)` | O(n) |
| String concatenation in a loop (`s += c`) | O(n²) total, use `"".join(parts)` |
| Slicing `list[a:b]` | O(b - a) |

### Space Complexity

Space complexity measures the extra memory a solution uses as `n` grows. It's written in Big O just like time complexity.

- **Count auxiliary space only:** memory you allocate beyond the input itself. An in-place algorithm that only uses a few variables is `O(1)`, even though the input is `O(n)`.
- **Recursion uses space:** each call sits on the call stack, so recursion depth `d` costs `O(d)`. Recursing over a linked list of `n` nodes is `O(n)`, while recursing on a balanced binary tree is `O(log n)`.
- **Copies count:** slicing (`arr[1:]`), `sorted(arr)` and building a new string or list each allocate `O(n)`.

| Space | Example |
|-------|---------|
| O(1) | A few variables or pointers (two pointers, reversing a linked list iteratively) |
| O(log n) | Recursion depth of binary search, or of a balanced tree |
| O(n) | Hash map/set of the input, a stack, a copy of the array |
| O(n²) | A 2D grid or DP table of size `n * n` |

**Time vs. space trade-off:** you can often spend memory to save time. Two Sum goes from O(n²) time and O(1) space (nested loops) to O(n) time and O(n) space (hash map). In interviews, state both and mention the trade-off.

## Data Structures and Algorithms

**A data structure** is a way of organizing data in memory so it can be accessed and modified efficiently. Each one makes some operations cheap and others expensive, so picking the right one is often the whole problem. Examples: arrays (lists), hash maps (dicts), sets, stacks, queues, linked lists, heaps, trees, graphs.

**An algorithm** is a step-by-step procedure that solves a problem, usually by operating on a data structure. Examples: binary search, sorting, two pointers, sliding window, DFS/BFS, dynamic programming.

They work as a pair: the data structure decides what operations cost, and the algorithm decides how many of them you perform. For example, "does this value exist?" is O(n) on a list but O(1) on a set, which is why Contains Duplicate is solved with a set.

The data structures we are going to focus on are:

- Arrays (Lists as referred to in Python)
- Hashmaps (Dictionaries as referred to in Python)
- Sets
- Tuples
- Linked Lists
- Trees
- Stacks and Queues
- Graphs
- Tries
- Heaps / Priority Queues

The algorithms we are going to focus on are (following the NeetCode roadmap):

- Two Pointers
- Sliding Window
- Binary Search
- Prefix Sums
- Sorting (including Bucket Sort)
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Backtracking
- Dynamic Programming (1-D and 2-D)
- Greedy
- Intervals (merge, sweep line)
- Topological Sort
- Union-Find
- Dijkstra's Algorithm (shortest path)
- Bit Manipulation

## Data Structures Explained

Each section below covers: how it works, how you use it (with Big O), the mental model to carry into an interview, and a bare-bones Python implementation. In real interviews use the built-ins (`list`, `dict`, `set`, `deque`, `heapq`); write these from scratch only when asked, or to understand what the built-ins are doing.

### Arrays (Python `list`)

**How it works:** a contiguous block of memory holding elements side by side. Because every slot is the same size, the address of index `i` is `start + i * size`, so the computer jumps straight to it. Python's `list` is a *dynamic array*: when it fills up, it allocates a bigger block (about 1.125x–2x), copies everything over, and carries on. That copy is rare, so `append` is **amortized** O(1).

**Operations:**

| Operation | Time | Notes |
|-----------|------|-------|
| Access / assign `a[i]` | O(1) | Direct address math |
| Append / pop at end | O(1) amortized | Occasional O(n) resize |
| Insert / delete at index `i` | O(n) | Everything after `i` must shift |
| Search `x in a` | O(n) | Must scan (O(log n) if sorted + binary search) |
| Slice `a[i:j]` | O(j - i) | Creates a copy |
| Space | O(n) | |

**Mental model:** a row of numbered lockers. Opening locker 7 is instant. Squeezing a new locker into the middle means shoving every locker after it one spot over. Anything that touches the *end* is cheap; anything that touches the *front or middle* is expensive. Reach for an array when you need fast index access and ordered data; reach for two pointers, sliding window and prefix sums when the problem is "array" shaped.

```python
class DynamicArray:
    def __init__(self):
        self.capacity = 2                       # slots allocated
        self.length = 0                         # slots actually used
        self.data = [None] * self.capacity      # stand-in for raw memory

    def get(self, i):                           # O(1)
        if not 0 <= i < self.length:
            raise IndexError("index out of range")
        return self.data[i]

    def set(self, i, value):                    # O(1)
        if not 0 <= i < self.length:
            raise IndexError("index out of range")
        self.data[i] = value

    def append(self, value):                    # O(1) amortized
        if self.length == self.capacity:
            self._resize(self.capacity * 2)     # double when full
        self.data[self.length] = value
        self.length += 1

    def pop(self):                              # O(1)
        if self.length == 0:
            raise IndexError("pop from empty array")
        value = self.data[self.length - 1]
        self.data[self.length - 1] = None
        self.length -= 1
        return value

    def insert(self, i, value):                 # O(n): shift right
        if not 0 <= i <= self.length:
            raise IndexError("index out of range")
        if self.length == self.capacity:
            self._resize(self.capacity * 2)
        for j in range(self.length, i, -1):     # walk backwards so we don't overwrite
            self.data[j] = self.data[j - 1]
        self.data[i] = value
        self.length += 1

    def remove_at(self, i):                     # O(n): shift left
        if not 0 <= i < self.length:
            raise IndexError("index out of range")
        value = self.data[i]
        for j in range(i, self.length - 1):
            self.data[j] = self.data[j + 1]
        self.data[self.length - 1] = None
        self.length -= 1
        return value

    def _resize(self, new_capacity):            # O(n), but rare
        new_data = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __len__(self):
        return self.length
```

### Hashmaps (Python `dict`)

**How it works:** stores `key -> value` pairs. A *hash function* turns the key into an integer, and that integer (mod the table size) picks a **bucket** in an underlying array. Looking up a key means hashing it and going straight to its bucket instead of searching. Two keys can land in the same bucket (a *collision*); the classic fix is **chaining**: each bucket holds a small list of pairs. When the table gets too full (load factor too high), it grows and rehashes everything so buckets stay short. (CPython actually uses open addressing, but the idea is the same.) Keys must be hashable, so immutable: ints, strings, tuples yes; lists no.

**Operations:**

| Operation | Average | Worst | Notes |
|-----------|---------|-------|-------|
| Get `d[k]` / `k in d` | O(1) | O(n) | Worst case is everything colliding |
| Set `d[k] = v` | O(1) | O(n) | Occasional O(n) rehash on growth |
| Delete `del d[k]` | O(1) | O(n) | |
| Iterate keys/values | O(n) | O(n) | Insertion-ordered in Python 3.7+ |
| Space | O(n) | | |

**Mental model:** a coat check. You hand over a ticket (the key), and the attendant walks straight to the right hook, with no searching the whole room. The price is memory (the hooks) and the fact that the order is not meaningful for lookups. Whenever you catch yourself writing "for each x, scan the array to find y", ask whether a hashmap can answer "have I seen y?" in O(1). Typical uses: counting (`Counter`), grouping (`defaultdict(list)`), complement lookup (Two Sum), caching/memoization.

```python
class HashMap:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]    # each bucket is a list of (key, value)

    def _index(self, key):
        return hash(key) % self.capacity                # hash -> bucket number

    def put(self, key, value):                          # O(1) average
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:                                # key exists: overwrite
                bucket[i] = (key, value)
                return
        bucket.append((key, value))                     # new key (or collision: chain it)
        self.size += 1
        if self.size > self.capacity * 0.75:            # load factor too high
            self._rehash()

    def get(self, key, default=None):                   # O(1) average
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        return default

    def remove(self, key):                              # O(1) average
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def contains(self, key):
        sentinel = object()
        return self.get(key, sentinel) is not sentinel

    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    def _rehash(self):                                  # O(n): double and reinsert everything
        old = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old:
            for k, v in bucket:
                self.put(k, v)

    def __len__(self):
        return self.size
```

### Sets (Python `set`)

**How it works:** a hashmap that stores only keys, no values. It keeps a collection of **unique** elements and answers "is this in here?" through the same hash-and-bucket trick. Adding a duplicate does nothing. Like dict keys, elements must be hashable (use `frozenset` or tuples for nested sets). Sets are unordered, so there is no indexing.

**Operations:**

| Operation | Average | Notes |
|-----------|---------|-------|
| `s.add(x)` | O(1) | No-op if already present |
| `x in s` | O(1) | The reason sets exist |
| `s.remove(x)` / `s.discard(x)` | O(1) | `remove` raises `KeyError` if missing, `discard` doesn't |
| Union `a \| b`, intersection `a & b`, difference `a - b` | O(len(a) + len(b)) | Intersection is O(min) in practice |
| Iterate | O(n) | |
| Space | O(n) | |

**Mental model:** a guest list at the door. You only care whether a name is on it, never *where* or how many times. Use a set to deduplicate, to track "visited" nodes in graph/DFS/BFS problems, and to turn an O(n) `x in list` into O(1) (Contains Duplicate, Longest Consecutive Sequence). If you need a count or an associated value, you want a dict instead.

```python
class HashSet:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]    # each bucket holds items that collided

    def _bucket(self, item):
        return self.buckets[hash(item) % self.capacity]

    def add(self, item):                                # O(1) average
        bucket = self._bucket(item)
        if item in bucket:                              # already present: sets hold uniques
            return
        bucket.append(item)
        self.size += 1
        if self.size > self.capacity * 0.75:
            self._rehash()

    def contains(self, item):                           # O(1) average
        return item in self._bucket(item)

    def remove(self, item):                             # O(1) average
        bucket = self._bucket(item)
        if item in bucket:
            bucket.remove(item)
            self.size -= 1

    def union(self, other):                             # O(n + m)
        result = HashSet()
        for item in self.items() + other.items():
            result.add(item)
        return result

    def intersection(self, other):                      # O(n)
        result = HashSet()
        for item in self.items():
            if other.contains(item):
                result.add(item)
        return result

    def items(self):
        return [item for bucket in self.buckets for item in bucket]

    def _rehash(self):
        old = self.items()
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for item in old:
            self.add(item)

    def __len__(self):
        return self.size
```

### Tuples

**How it works:** an **immutable**, ordered, fixed-size sequence. Under the hood it is an array like a list, but once created you cannot append, remove or reassign elements. Immutability is what makes a tuple *hashable* (as long as its contents are hashable), so tuples can be dict keys and set members, which lists cannot.

**Operations:**

| Operation | Time | Notes |
|-----------|------|-------|
| Create `(a, b, c)` | O(n) | |
| Access `t[i]` | O(1) | |
| Search `x in t`, `t.index(x)`, `t.count(x)` | O(n) | |
| Slice `t[i:j]` | O(j - i) | Returns a new tuple |
| Unpack `a, b = t` | O(n) | |
| Modify | not allowed | Build a new tuple instead, O(n) |
| Space | O(n) | |

**Mental model:** a sealed envelope with a fixed number of labelled slots: a *record* or a *coordinate*, not a growing collection. Use a list for "many things of the same kind that change" and a tuple for "a few things that belong together and don't change": `(row, col)`, `(distance, node)` in a heap, `(x, y)` as a visited-set key, multiple return values. Careful: a tuple holding a list is still hashable-looking but not hashable, and the inner list can still mutate.

```python
class ImmutableTuple:
    """Minimal tuple: fixed contents, read-only access."""
    __slots__ = ("_data",)                              # no per-instance __dict__, no new attributes

    def __init__(self, *items):
        object.__setattr__(self, "_data", list(items))  # bypass our own __setattr__ block

    def __setattr__(self, name, value):
        raise AttributeError("tuple is immutable")

    def __getitem__(self, i):                           # O(1); supports t[i]
        return self._data[i]

    def __len__(self):
        return len(self._data)

    def __iter__(self):                                 # enables unpacking: a, b = t
        return iter(self._data)

    def __eq__(self, other):
        return isinstance(other, ImmutableTuple) and self._data == other._data

    def __hash__(self):                                 # hashable => usable as dict key / set member
        h = 0
        for item in self._data:
            h = h * 31 + hash(item)
        return h

    def index(self, x):                                 # O(n)
        return self._data.index(x)

    def count(self, x):                                 # O(n)
        return self._data.count(x)

    def __repr__(self):
        return "(" + ", ".join(map(repr, self._data)) + ")"
```

### Linked Lists

**How it works:** a chain of **nodes**, where each node stores a value and a pointer to the next node (a *doubly* linked list also stores a pointer to the previous one). Nodes live anywhere in memory; only the pointers connect them. You hold a reference to the `head`, and to reach anything you start there and follow `next` pointers. There is no index math.

**Operations (singly linked list):**

| Operation | Time | Notes |
|-----------|------|-------|
| Access / search by position or value | O(n) | Must walk from the head |
| Insert / delete at head | O(1) | Just rewire `head` |
| Insert at tail | O(n), or O(1) with a `tail` pointer | |
| Insert / delete after a node you already hold | O(1) | Rewire two pointers |
| Delete by value | O(n) | Find it first |
| Reverse | O(n) time, O(1) space | Flip each pointer in one pass |
| Space | O(n) | One extra pointer per node |

**Mental model:** a scavenger hunt: each clue only tells you where the next clue is. You can't skip ahead, but adding or removing a clue only means changing the note on the clue before it, with no shifting of anything. Most interview problems come down to pointer discipline: draw boxes and arrows, and always save `next` *before* you overwrite it. Core tricks: a **dummy node** to avoid special-casing the head, **slow/fast pointers** (find middle, detect cycle), and **prev/curr/next** (reverse).

```python
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next                    # pointer to the next node (None = end)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, val):                 # O(1)
        self.head = ListNode(val, self.head)
        self.size += 1

    def append(self, val):                  # O(n): walk to the tail
        node = ListNode(val)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        self.size += 1

    def find(self, val):                    # O(n)
        curr = self.head
        while curr:
            if curr.val == val:
                return curr
            curr = curr.next
        return None

    def delete(self, val):                  # O(n): delete first node with this value
        dummy = ListNode(0, self.head)      # dummy means the head needs no special case
        prev, curr = dummy, self.head
        while curr:
            if curr.val == val:
                prev.next = curr.next       # skip over curr
                self.size -= 1
                break
            prev, curr = curr, curr.next
        self.head = dummy.next

    def reverse(self):                      # O(n) time, O(1) space
        prev, curr = None, self.head
        while curr:
            nxt = curr.next                 # save before we overwrite it
            curr.next = prev                # flip the pointer
            prev, curr = curr, nxt
        self.head = prev

    def to_list(self):                      # handy for printing/testing
        out, curr = [], self.head
        while curr:
            out.append(curr.val)
            curr = curr.next
        return out
```

### Trees

**How it works:** a hierarchy of nodes. One **root**, and every node has zero or more **children** and exactly one parent (except the root). Nodes with no children are **leaves**. A **binary tree** allows at most two children (`left`, `right`). A **binary search tree (BST)** adds an ordering rule: everything in a node's left subtree is smaller, everything in its right subtree is larger, so each comparison discards half the remaining tree. Trees are naturally recursive: each child is the root of a smaller tree.

**Operations (BST):**

| Operation | Balanced | Worst (skewed into a line) | Notes |
|-----------|----------|----------------------------|-------|
| Search / insert / delete | O(log n) | O(n) | Height `h` is the real cost: O(h) |
| Traversal (in/pre/post/level order) | O(n) | O(n) | Every node visited once |
| Height / size / any "whole tree" question | O(n) | O(n) | |
| Space (structure) | O(n) | O(n) | |
| Space (recursion) | O(log n) | O(n) | Call stack depth = height |

Traversals: **inorder** (left, node, right) gives sorted order on a BST; **preorder** (node, left, right) copies/serializes a tree; **postorder** (left, right, node) processes children before parents (heights, deletion); **level order** (BFS, uses a queue) goes row by row.

**Mental model:** a family tree, or a company org chart. For nearly every tree problem, ask: *"If I trust the recursion to solve my left and right subtrees, how do I combine their answers at this node?"* Write the base case (`if not node: return ...`), recurse on both children, combine. DFS (recursion or a stack) goes deep first; BFS (a queue) goes level by level.

```python
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):                          # O(h)
        if not self.root:
            self.root = TreeNode(val)
            return
        curr = self.root
        while True:
            if val < curr.val:                      # smaller goes left
                if not curr.left:
                    curr.left = TreeNode(val)
                    return
                curr = curr.left
            elif val > curr.val:                    # larger goes right
                if not curr.right:
                    curr.right = TreeNode(val)
                    return
                curr = curr.right
            else:
                return                              # ignore duplicates

    def search(self, val):                          # O(h)
        curr = self.root
        while curr:
            if val == curr.val:
                return True
            curr = curr.left if val < curr.val else curr.right
        return False

    def delete(self, val):                          # O(h)
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:                                       # found it
            if not node.left:                       # 0 or 1 child: replace with the child
                return node.right
            if not node.right:
                return node.left
            succ = node.right                       # 2 children: use the inorder successor
            while succ.left:                        # (smallest value in the right subtree)
                succ = succ.left
            node.val = succ.val
            node.right = self._delete(node.right, succ.val)
        return node

    def inorder(self):                              # O(n): left, node, right (sorted on a BST)
        out = []
        def dfs(node):
            if node:
                dfs(node.left)
                out.append(node.val)
                dfs(node.right)
        dfs(self.root)
        return out

    def preorder(self):                             # O(n): node, left, right
        out = []
        def dfs(node):
            if node:
                out.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(self.root)
        return out

    def postorder(self):                            # O(n): left, right, node
        out = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                out.append(node.val)
        dfs(self.root)
        return out

    def level_order(self):                          # O(n): BFS with a queue
        out, q = [], deque([self.root] if self.root else [])
        while q:
            level = []
            for _ in range(len(q)):                 # freeze the current level's size
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(level)
        return out

    def height(self):                               # O(n): the classic recursive pattern
        def dfs(node):
            if not node:
                return 0                            # base case
            return 1 + max(dfs(node.left), dfs(node.right))   # combine children
        return dfs(self.root)
```

### Stacks and Queues

**How it works:** both are restricted lists that only let you touch the ends.

- **Stack: LIFO** (last in, first out). You push and pop at the same end (the "top"). Backed by a Python `list` (`append` / `pop`).
- **Queue: FIFO** (first in, first out). You enqueue at the back and dequeue from the front. Backed by `collections.deque` (`append` / `popleft`). Do **not** use `list.pop(0)`, which is O(n).

**Operations:**

| Operation | Stack (`list`) | Queue (`deque`) |
|-----------|----------------|-----------------|
| Add (`push` / `enqueue`) | O(1) | O(1) |
| Remove (`pop` / `dequeue`) | O(1) | O(1) |
| Peek top / front | O(1) | O(1) |
| Search | O(n) | O(n) |
| Space | O(n) | O(n) |

**Mental model:** a stack is a pile of plates: you only touch the top one, so the most recent thing is handled first. Reach for it when the problem has *nesting* or "undo/backtrack" flavor: matching parentheses, DFS, evaluating expressions, and **monotonic stacks** ("next greater element", Daily Temperatures). A queue is a line at a shop: first come, first served. Reach for it for *processing in arrival order* or *level by level*: BFS, task scheduling, sliding window maximum (with a deque). Also remember the call stack: recursion is an implicit stack.

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):                  # O(1)
        self.items.append(x)

    def pop(self):                      # O(1)
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):                     # O(1): look at the top without removing
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return not self.items

    def __len__(self):
        return len(self.items)


class _Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    """Linked-list queue: head = front, tail = back, both ends O(1)."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, x):               # O(1): add at the back
        node = _Node(x)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node            # queue was empty
        self.tail = node
        self.size += 1

    def dequeue(self):                  # O(1): remove from the front
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None            # queue became empty
        self.size -= 1
        return val

    def peek(self):                     # O(1)
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.head.val

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
```

### Graphs

**How it works:** a set of **vertices** (nodes) connected by **edges**. Edges can be *directed* or *undirected*, and *weighted* or not. Unlike a tree, a graph may have cycles, multiple components, and no root. Two standard representations:

- **Adjacency list** (default choice): `dict` mapping each node to a list of its neighbors. Space O(V + E).
- **Adjacency matrix**: a `V x V` grid where `m[i][j]` says whether an edge exists. Space O(V²); good for dense graphs and O(1) edge checks.

Grids (`grid[r][c]` with 4 neighbors) are implicit graphs: each cell is a vertex, adjacent cells are edges.

**Operations (adjacency list, V vertices, E edges):**

| Operation | Time | Notes |
|-----------|------|-------|
| Add vertex | O(1) | |
| Add edge | O(1) | |
| Check edge exists `u -> v` | O(deg(u)) | O(1) with sets or a matrix |
| List neighbors of `u` | O(deg(u)) | |
| BFS / DFS traversal | O(V + E) | Every vertex and edge once |
| Space | O(V + E) | O(V) extra for the `visited` set |

**Mental model:** a map of cities and roads, or a social network. Almost every graph problem is "start somewhere and **explore**", and the one rule that matters is *mark nodes as visited so you never loop forever on a cycle*. **BFS** (queue) explores in rings, so it finds the **shortest path in an unweighted graph**. **DFS** (recursion/stack) dives deep, so it suits connectivity, cycle detection, counting components (Number of Islands) and backtracking. Weighted shortest paths need Dijkstra; dependency ordering needs topological sort.

```python
from collections import defaultdict, deque


class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)            # node -> list of neighbors
        self.directed = directed

    def add_edge(self, u, v):                   # O(1)
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)               # undirected: edge goes both ways
        else:
            self.adj[v]                         # touch v so it exists as a vertex

    def neighbors(self, u):                     # O(deg(u))
        return self.adj[u]

    def has_edge(self, u, v):                   # O(deg(u))
        return v in self.adj[u]

    def bfs(self, start):                       # O(V + E): order of visit, nearest first
        visited, order = {start}, []
        q = deque([start])
        while q:
            node = q.popleft()
            order.append(node)
            for nei in self.adj[node]:
                if nei not in visited:
                    visited.add(nei)            # mark when *queued*, not when popped
                    q.append(nei)
        return order

    def dfs(self, start):                       # O(V + E): go deep first
        visited, order = set(), []
        def visit(node):
            visited.add(node)
            order.append(node)
            for nei in self.adj[node]:
                if nei not in visited:
                    visit(nei)
        visit(start)
        return order

    def has_path(self, src, dst):               # O(V + E)
        return dst in self.bfs(src)

    def shortest_path_len(self, src, dst):      # O(V + E): fewest edges (unweighted only)
        visited, q = {src}, deque([(src, 0)])
        while q:
            node, dist = q.popleft()
            if node == dst:
                return dist
            for nei in self.adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, dist + 1))
        return -1                               # unreachable
```

### Tries (Prefix Trees)

**How it works:** a tree where each node represents one **character**, and the path from the root to a node spells a prefix. Each node holds a map of `char -> child` and a flag marking whether a complete word ends there. Words that share a prefix share the same path (`"car"`, `"card"`, `"care"` all share `c -> a -> r`), so nothing is stored twice and prefix questions are cheap.

**Operations** (`L` = length of the word or prefix, independent of how many words are stored):

| Operation | Time | Notes |
|-----------|------|-------|
| Insert word | O(L) | |
| Search exact word | O(L) | Path must exist **and** end flag set |
| Starts-with prefix | O(L) | Path must exist |
| Collect all words under a prefix | O(L + size of subtree) | Autocomplete |
| Space | O(total characters) worst case | Shared prefixes reduce it |

**Mental model:** a dictionary's thumb-index, taken further: to find "card", you open at C, then A, then R, then D, narrowing at each letter, and you never compare whole words. The cost depends on the length of *what you're looking up*, not on how many words you've stored. Reach for it when you see **prefix** in the problem (autocomplete, Implement Trie, Word Search II, Add and Search Words). Remember the two checks: reaching the end of a path is not the same as a word ending there (`"car"` is a prefix of `"card"` but only a word if you inserted it).

```python
class TrieNode:
    def __init__(self):
        self.children = {}              # char -> TrieNode
        self.is_word = False            # True if a word ends at this node


class Trie:
    def __init__(self):
        self.root = TrieNode()          # root represents the empty prefix

    def insert(self, word):             # O(L)
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()      # create the path as needed
            node = node.children[ch]
        node.is_word = True             # mark the end of a complete word

    def _walk(self, s):                 # follow s from the root; None if the path breaks
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word):             # O(L): exact word
        node = self._walk(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):      # O(L): any word with this prefix
        return self._walk(prefix) is not None

    def words_with_prefix(self, prefix):    # autocomplete
        node = self._walk(prefix)
        out = []
        def dfs(n, path):
            if n.is_word:
                out.append(path)
            for ch, child in n.children.items():
                dfs(child, path + ch)
        if node:
            dfs(node, prefix)
        return out
```

### Heaps / Priority Queues

**How it works:** a **complete binary tree** stored flat in an array that maintains the **heap property**: in a *min-heap*, every parent is `<=` its children, so the smallest element is always at index 0. No full sorting is kept, only enough order to know the minimum. For the node at index `i`: children are at `2i + 1` and `2i + 2`, parent is at `(i - 1) // 2`. Insertion adds at the end and **sifts up**; removal swaps the root with the last element, drops it, and **sifts down** the new root. Python's `heapq` is a min-heap; for a max-heap push negated values.

**Operations:**

| Operation | Time | Notes |
|-----------|------|-------|
| Peek min `h[0]` | O(1) | |
| Push `heappush` | O(log n) | Sift up |
| Pop min `heappop` | O(log n) | Sift down |
| Build from list `heapify` | O(n) | Faster than n pushes (O(n log n)) |
| Search arbitrary value | O(n) | Heaps are not searchable |
| Top-k of n items | O(n log k) | Keep a heap of size k |
| Space | O(n) | |

**Mental model:** a tournament bracket where only the champion has to be known at all times. When the champion leaves, you replay just one path (log n matches) to crown the next one, with no need to re-rank everyone. Use it whenever you repeatedly need "the smallest/largest *right now*" while items keep arriving or leaving: top-k, k-th largest, merge k sorted lists, running median (two heaps), task scheduling, Dijkstra. Tuples work as heap items and compare left to right: `(priority, item)`.

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def peek(self):                                 # O(1)
        return self.heap[0]

    def push(self, val):                            # O(log n)
        self.heap.append(val)                       # add at the end of the array...
        self._sift_up(len(self.heap) - 1)           # ...then bubble it up into place

    def pop(self):                                  # O(log n)
        if not self.heap:
            raise IndexError("pop from empty heap")
        root = self.heap[0]
        last = self.heap.pop()                      # remove the last element
        if self.heap:
            self.heap[0] = last                     # move it to the root...
            self._sift_down(0)                      # ...then sink it into place
        return root

    @classmethod
    def heapify(cls, items):                        # O(n): sift down from the last parent up
        h = cls()
        h.heap = list(items)
        for i in range(len(h.heap) // 2 - 1, -1, -1):
            h._sift_down(i)
        return h

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] >= self.heap[parent]:   # heap property holds, stop
                break
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:                       # both children are larger, stop
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def __len__(self):
        return len(self.heap)
```

## Navigating Online Assessments and Coding Interviews

### Before you code

- **Clarify the problem:** ask about input size, empty input, duplicates, negative numbers, and whether the input is sorted.
- **Start with brute force:** say the simple solution and its Big O out loud, then improve it. A working slow answer beats a half-finished fast one.
- **Check constraints for the target complexity:** `n <= 10^5` needs O(n log n) or better, `n <= 20` allows exponential (backtracking), `n <= 1000` allows O(n²).
- **Talk through your approach** before typing, and say the time and space complexity when you finish.

### While coding

- Use clear variable names and keep the code simple. Avoid clever one-liners.
- Handle edge cases first (empty input, single element) with an early return.
- Test by hand with a small example, then an edge case, before saying you're done.
- If you're stuck, narrate your thinking. Interviewers often give hints when they can follow you.

### Online assessments

- Read every problem first and start with the easiest one to bank points.
- Run the provided examples before submitting. Hidden tests usually cover large inputs, so check your complexity.
- Don't spend all your time on one problem. Submit a partial solution and move on.
- In Python, `from collections import defaultdict, Counter, deque` and `import heapq` cover most needs.

### Patterns seen in these solutions

- **Hash map / set to avoid a nested loop:** O(n²) → O(n) time at the cost of O(n) space (Two Sum, Contains Duplicate, Valid Anagram).
- **Sort first, then two pointers:** O(n log n) time, O(1) extra space (3Sum, Container With Most Water).
- **Binary search on sorted data:** O(log n) (Binary Search, Search a 2D Matrix).
- **Monotonic stack:** each element is pushed and popped at most once, so O(n) (Daily Temperatures).
- **Single pass with running state:** O(n) time, O(1) space (Best Time to Buy and Sell Stock).
