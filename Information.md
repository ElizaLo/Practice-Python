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

## Inheriting Variables and Methods

**This is how the interpreter looks up attributes:**

1. First, it checks for an instance variable or an instance method by the name it’s looking for.
2. If an instance variable or method by that name is not found, it checks for a class variable.
3. If no class variable is found, it looks for a class variable in the parent class.
4. If no class variable is found, the interpreter looks for a class variable in THAT class’s parent (the “grandparent” class).
5. This process goes on until the last ancestor is reached, at which point Python will signal an error.

## Invoking the Parent Class’s Method

Call `super().feed()`. This is nice because it’s easier to read, and also because it puts the specification of the class that Dog inherits from in just one place, `class Dog(Pet)`. Elsewhere, you just refer to `super()` and python takes care of looking up that the parent (super) class of Dog is Pet

# Test Cases

- **Unit tests** check that small bits of code are correctly implemented. 
- **Functional tests** check that larger chunks of code work correctly.

Python provides a statement called `assert`.

- Following the word assert there will be a python expression.
- If that expression evaluates to the Boolean `False`, then the interpreter will raise a runtime error.
- If the expression evaluates to `True`, then nothing happens and the execution goes on to the next line of code.

## Writing Test Cases for Functions

A useful function will do some combination of three things, given its input parameters:

- Return a value. For these, you will write return **value tests**.
- Modify the contents of some mutable object, like a list or dictionary. For these you will write **side effect tests**.
- Print something or write something to a file. Tests of whether a function generates the right printed output are beyond the scope of this testing framework; you won’t write these tests.

To deal with increasingly complex programs, we are going to suggest a technique called **incremental development**. The goal of incremental development is to avoid long debugging sessions by adding and testing only a small amount of code at a time.

**If you write unit tests before doing the incremental development, you will be able to track your progress as the code passes more and more of the tests. Alternatively, you can write additional tests at each stage of incremental development.**

# Exception

With **try/except**, you tell the python interpreter:

  - **Try to execute a block of code, the “try” clause.**
    - If the whole block of code executes without any run-time errors, just carry on with the rest of the program after the try/except statement.
  - **If a run-time error does occur during execution of the block of code:**
    - skip the rest of that block of code (but don’t exit the whole program)
    - execute a block of code in the “except” clause
    - then carry on with the rest of the program after the try/except statement
    
    ```python
    try:
      <try clause code block>
    except <ErrorType>:
      <exception handler code block>
    ```
   
   ```python
   try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
  except Exception as e:
    print("got an error")
    print(e)
    ```
