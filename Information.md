- [Built-in Types](https://docs.python.org/3/library/stdtypes.html#built-in-types) (Python Documentation)

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
  
    - ## Mutating Methods
    **Mutating methods** are ones that change the object after the method has been used. 
    
    - **_Methods_**
      - `append` (Adds the argument passed to it to the end of the list)
      ```python
      mylist.append(5)
      ```
      - `insert`
      ```python
      mylist.insert(1, 12)
      ```
      - `reverse`
      ```python
      mylist.reverse()
      ```
      - `sort`
      ```python
      mylist.sort()
      ```
      - `remove`
      ```python
      mylist.remove(5)
      ```
      - `pop`
        - With **no parameter**, will remove and return the last item of the list
        - If **provide a parameter** for the position, pop will remove and return the item at that position
        
          ```python
          mylist.pop()
          ```
  
    - ## Non-Mutating Methods
    **Non-mutating methods** do not change the object after the method has been used.
  - **_Methods_**
  
     - `count` (Count returns the number of occurances of the argument given but does not change the original string or list)
     ```python
     mylist.count(12)
     ```
     - `index` (Index returns the leftmost occurance of the argument but does not change the original string or list)
     ```python
     mylist.index(3)
     ```
     
  The following table provides a summary of the list methods shown above. The column labeled `result` gives an explanation as to what the return value is as it relates to the new value of the list. The word **mutator** means that the list is changed by the method but nothing is returned (actually `None` is returned). A **hybrid** method is one that not only changes the list but also returns a value as its result. Finally, if the result is simply a return, then the list is unchanged by the method.
  
  <img src="https://github.com/ElizaLo/Practice-Python/blob/master/Python%203%20Programming/List_Methods.png" width="695" height="382">
  
  - ## `+=` and `obj = obj + object_two`
  
    - `obj = obj + object_two` - makes a new object entirely and reassigns to `obj`
    ``` python
     x = ["dogs", "cats", "birds", "reptiles"]
     y = x
     y = y + ['sheep']
    ```
    - `obj += object_two` -  changes the original object so that the contents of `object_two` are added to the end of the first.
    ```python
    x = ["dogs", "cats", "birds", "reptiles"]
    y = x
    x += ['fish', 'horses']
    ```
 
 - ## Objects and References
 
 ``` python
  a = "banana"
  b = "banana"
  print(a is b)
```
  
 In Python, every object has a unique identification tag. Likewise, there is a built-in function that can be called on any object to return its unique id. The function is appropriately called `id` and takes a single parameter, the object that you are interested in knowing about.
 
```python
  print(id(a))
  print(id(b))
```

- ## String
  - `.format()` Method
  
  Since braces have special meaning in a format string, there must be a special rule if you want braces to actually be included in the final formatted string. The rule is to double the braces: \{\{ and \}\}. For example mathematical set notation uses braces. The initial and final doubled braces in the format string below generate literal braces in the formatted string:
```python
a = 5
b = 9
setStr = 'The set is \{\{\{}, {}}}.'.format(a, b)
```
# Class
## Class Variables and Instance Variables

**When the interpreter sees an expression of the form `<obj>.<varname>`, it:**
  
1. Checks if the object has an instance variable set. If so, it uses that value.
2. If it doesn’t find an instance variable, it checks whether the class has a class variable. If so it uses that value.
3. If it doesn’t find an instance or a class variable, it creates a runtime error (actually, it does one other check first, which you will learn about in the next chapter).

**When the interpreter sees an assignment statement of the form `<obj>.<varname> = <expr>`, it:**

1. Evaluates the expression on the right-hand side to yield some python object;
2. Sets the instance variable `<varname>` of `<obj>` to be bound to that python object. Note that an assignment statement of this form never sets the class variable; it only sets the instance variable.
