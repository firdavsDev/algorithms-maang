# Data Structures (Python)

Data structures are a way of organizing and storing data in a computer so that it can be accessed and modified efficiently. In Python, there are several built-in data structures that you can use to store and manipulate data. Here are some of the most common ones:

1. **List**: A list is an ordered collection of items that can be of different types. You can add, remove, and modify items in a list. Lists are defined using square brackets `[]`.

```python
my_list = [1, 2, 3, 'hello', True]
```
2. **Tuple**: A tuple is similar to a list, but it is immutable, meaning that once you create a tuple, you cannot modify it. Tuples are defined using parentheses `()`.

```python
my_tuple = (1, 2, 3, 'hello', True)
```
3. **Set**: A set is an unordered collection of unique items. Sets are defined using curly braces `{}`.
```python
my_set = {1, 2, 3, 'hello', True}
```
4. **Dictionary**: A dictionary is a collection of key-value pairs. Each key is unique and maps to a value. Dictionaries are defined using curly braces `{}` with key-value pairs separated by colons `:`.
```python
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
```
5. **String**: A string is a sequence of characters. Strings are defined using single quotes `''` or double quotes `""`.
```python
my_string = "Hello, World!"
```

These data structures are fundamental to programming in Python and are used in various applications, from simple scripts to complex algorithms. Understanding how to use these data structures effectively is crucial for writing efficient and readable code.

In addition to these built-in data structures, Python also provides several modules that offer more specialized data structures, such as `collections` for named tuples, deque, and defaultdict, and `array` for efficient arrays of numeric data. Depending on your specific use case, you may find these additional data structures useful for optimizing your code.

## Difference table
| Data Structure | Mutable | Ordered | Unique Elements | Syntax |
|----------------|---------|---------|-----------------|--------|
| List           | Yes     | Yes     | No              | `[]`   |
| Tuple          | No      | Yes     | No              | `()`   |
| Set            | Yes     | No      | Yes             | `{}`   |
| Dictionary      | Yes     | No      | Keys are unique | `{}`   |
| String         | No      | Yes     | No              | `''` or `""` |

- This table summarizes the key differences between the various data structures in Python, including whether they are mutable, ordered, and whether they allow for unique elements. Understanding these differences can help you choose the appropriate data structure for your specific use case.
