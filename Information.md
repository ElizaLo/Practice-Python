- ## Boolean Expressions
  - `=` is an **assignment operator**
  - `==` is a **comparison operator**

- ## Precedence of Operators

Python documentation [Operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence).

- ## `for` loop
  - The **iterable** is the object that you will parsing through in a for loop. Generally, this object does not change while the for loop is being executed.

  - The **iterator (loop) variable** is the variable which stores a portion of the iterable when the for loop is being executed. Each time the loop iterates, the value of the iterator variable will change to a different portion of the iterable.

- ## List
  - ## Cloning Lists

  ```python
  a = [81,82,83]
  b = a[:]     # make a clone using slice
  ```
  
  - ## List Element Deletion
  
  ``` python
  a = ['one', 'two', 'three']
  del a[1]
  ```
  
  ``` python
  alist = ['a', 'b', 'c', 'd', 'e', 'f']
  del alist[1:5]
  ```
 
 - ## Objects and References
 
 ``` python
  a = "banana"
  b = "banana"
  print(a is b)
  
  print(id(a))
  print(id(b))
  ```
