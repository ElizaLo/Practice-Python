## Table of Contents

- [Read](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#read)
- [Boolean Expressions](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#boolean-expressions)
- [Precedence of Operators](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#precedence-of-operators)
- [`for` loop](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#for-loop)
- [List](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#list)
  - [Cloning Lists](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#cloning-lists)
  - [List Element Deletion](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#list-element-deletion)
  - [Mutating Methods](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#mutating-methods)
  - [Non-Mutating Methods](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#non-mutating-methods)
  - [`+=` and `obj = obj + object_two`](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#-and-obj--obj--object_two)
- [Objects and References](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#objects-and-references)
- [String](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#string)
- [Class](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#class)
  - [Class Variables and Instance Variables](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#class-variables-and-instance-variables)
  - [Inheriting Variables and Methods](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#inheriting-variables-and-methods)
  - [Invoking the Parent Class’s Method](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#invoking-the-parent-classs-method)
  - [Дескрипторы](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#дескрипторы)
  - [`__slots__`](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#__slots__)
  - [Метаклассы](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#метаклассы)
  - []()
  - []()
- [Test Cases](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#test-cases)  
  - [Writing Test Cases for Functions](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#writing-test-cases-for-functions)
- [Exception](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#exception)
  - [Standard Exceptions](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#standard-exceptions)
  - [Language Exceptions](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#language-exceptions)
  - [Math Exceptions](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#math-exceptions)
  - [Other Exceptions](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#other-exceptions)
- [Debugging and Testing in Python](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#debugging-and-testing-in-python)
- [Parallelism in Python](https://github.com/ElizaLo/Practice-Python/blob/master/Information.md#parallelism-in-python)
- []()

## Read

- [Built-in Types](https://docs.python.org/3/library/stdtypes.html#built-in-types) (Python Documentation)
- [Data model](https://docs.python.org/3/reference/datamodel.html)
- [Руководство по **магическим методам** в Питоне](https://habr.com/ru/post/186608/)
- [Итерируемый объект, итератор и генератор](https://habr.com/ru/post/337314/)
- [Descriptor HowTo Guide](https://docs.python.org/3/howto/descriptor.html)
- [Python: статические методы, методы класса и экземпляра класса](https://medium.com/nuances-of-programming/python-статические-методы-методы-класса-и-экземпляра-класса-3e8529d24786)

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

**B каком порядке выполняются магические методы new, init и call при создании объекта?**

```python
class Class:
  def __new__(cls): pass
  def __init__(self): pass
  def __call__(self): pass

new_obj = Class()
```

- Магический метод `__call__` используется **_при вызове экземпляра класса, а не самого класса_**.

‼️ Однако, если класс с переопределённым методом call является метаклассом (о них мы поговорим чуть позже), то экземпляром этого класса является новый класс. А это значит, что при создании объекта класса, метаклассом которого является класс с переопределённым магическим методом call, вызывается этот самый метод call. Причем вызывается он раньше new и init.

## Inheriting Variables and Methods

**This is how the interpreter looks up attributes:**

1. First, it checks for an instance variable or an instance method by the name it’s looking for.
2. If an instance variable or method by that name is not found, it checks for a class variable.
3. If no class variable is found, it looks for a class variable in the parent class.
4. If no class variable is found, the interpreter looks for a class variable in THAT class’s parent (the “grandparent” class).
5. This process goes on until the last ancestor is reached, at which point Python will signal an error.

## Invoking the Parent Class’s Method

Call `super().feed()`. This is nice because it’s easier to read, and also because it puts the specification of the class that Dog inherits from in just one place, `class Dog(Pet)`. Elsewhere, you just refer to `super()` and python takes care of looking up that the parent (super) class of Dog is Pet

## Дескрипторы

Чтобы определить свой собственный дескриптор, нужно определить методы класса `__get__`, `__set__` или `__delete__`. После этого мы можем создать какой-то новый класс и в атрибут этого класса записать объект типа дескриптор. Теперь у данного объекта будет переопределено поведение при доступе к атрибуту (метод `__get__`), при присваивании значений (метод `__set__`) или при удалении (метод `__delete__`). Мы создадим объект класса Class и посмотрим, что будет происходить при обращении к атрибуту:

```python
class Descriptor:
    def __get__(self, obj, obj_type):
        print('get')
        
    def __set__(self, obj, value):
        print('set')
        
    def __delete__(self, obj):
        print('delete')


class Class:
    attr = Descriptor()
    

instance = Class()
```
Дескрипторы явялются мощным механизмом, который позволяет вам незаметно от пользователя переопределять поведение атрибутов в ваших классах. Например, мы можем определить **дескриптор Value**, который будет переопределять поведение при присваивании ему значения. Определим класс с атрибутом, который будет являться дескрип- тором, и будем наблюдать модифицированное поведение (умножение на 10) при присваивании значения

```python
class Value:
    def __init__(self):
        self.value = None
    
    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, obj, obj_type):
        return self.value
    
    def __set__(self, obj, value):
        self.value = self._prepare_value(value)
```
```python
class Class:
    attr = Value()

    
instance = Class()
instance.attr = 10

print(instance.attr)
```
100

Когда мы обращаемся к методу с помощью `obj.method`, возвращается **bound method** — метод, привязанный к определённому объекту. А если мы обращаемся к методу от Class, получаем **unbound method** — это просто функция. Как видите, один и тот же метод возвращает разные объекты в зависимости от того, как к нему обращаются. Это и есть поведение дескриптора:

```python
class Class:
    def method(self):
pass

obj = Class()
print(obj.method) print(Class.method)

---------------------------------------

<bound method Class.method of <__main__.Class object at 0x10ee77278>> 
<function Class.method at 0x10ee3bea0>
```


Напишем свою реализацию этих декораторов `@staticmethod` и `@classmethod`. 

**StaticMethod** будет просто сохранять функцию и возвращать её при вызове:

```python
class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        return self.func
```

В то же время, **ClassMethod** возвращает функцию, которая первым аргументом принимает `obj_type`, то есть класс:

```python
class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        if obj_type is None:
            obj_type = type(obj)

        def new_func(*args, **kwargs):
            return self.func(obj_type, *args, **kwargs)

        return new_func
```

- Дескрипторы данных и не данных отличаются в том, как будет изменено поведение поиска, если в словаре объекта уже есть запись с таким же именем как у дескриптора. Если попадается **дескриптор данных**, то _он вызывается раньше, чем запись из словаря объекта_. Если в такой же ситуации окажется **дескриптор не данных**, то _запись из словаря объекта имеет преимущество перед этим дескриптором_.

**Важные части, которые следует запомнить:**

- дескрипторы вызываются с помощью метода `__getattribute__`
- переопределение `__getattribute__` прекратит автоматический вызов дескрипторов
- `__getattribute__` доступен только внутри классов и объектов нового стиля
- `object.__getattribute__` и `type.__getattribute__` делают разные вызовы к `__get__`
- **дескрипторы данных** всегда имеют преимущество перед переменными объекта
- **дескрипторы не данных** могут потерять преимущество из-за переменных объекта

## `__slots__`

Последний пример дескрипторов в стандартной библиотеке Python — конструкция `__slots__`, которая позволяет определить класс с жестко заданным набором атрибутов. Как вы помните, у каждого класса есть словарь, в котором хранятся все его атрибуты. Очень часто это бывает излишне. У вас может быть огромное количество объек- тов, и вы не хотите создавать для каждого объекта словарь. В таком случае конструкция `__slots__` позволяет жестко задать количество элементов, которые ваш класс может содержать. В следующем примере мы постулируем, что в нашем классе должен быть только атрибут _anakin_. Если мы попытаемся добавить в наш класс еще один атрибут, ничего не получится:

```python
class Class:
    __slots__ = ['anakin']
    
    def __init__(self):
        self.anakin = 'the chosen one'

        
obj = Class()

obj.luke = 'the chosen too'

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-14-66c0c798df1f> in <module>()
      8 obj = Class()
      9 
---> 10 obj.luke = 'the chosen too'

AttributeError: 'Class' object has no attribute 'luke'
```

### Пример на дескрипторы

```python
class ImportantValue:
    def __init__(self, amount):
        self.amount = amount
    
    def __get__(self, obj, obj_type):
        return self.amount
    
    def __set__(self, obj, value):
        with open('log.txt', 'w') as f:
            f.write(str(value))
            
        self.amount = value
    
    
class Account:
    amount = ImportantValue(100)
    
bobs_account = Account()
bobs_account.amount = 200

with open('log.txt', 'r') as f:
    print(f.read())
    
----------------------

200
```

## Метаклассы

У класса тоже есть тип — `type`, потому что type, создал наш класс. В данном случае `type`, является **метаклассом**, **_т.е. он создаёт другие классы_**:

```python
type(Class)
----------------
type
```

Очень важно понимать разницу между созданием и наследованием. В данном случае класс **не является subclass-ом type**. Type его создаёт, но класс не наследуется от него, а наследуется от класса object:

```python
issubclass(Class, type)
False

issubclass(Class, object)
True
```

Для создания классов используется ме- такласс type, и вы можете на лету создать класс, вызвав type и передав ему название класса. Для примера создадим класс **NewClass без родителей и атрибутов**. Это настоящий класс, мы создали его на лету без использования литерала class:

```python
NewClass = type('NewClass', (), {})

print(NewClass)
print(NewClass())

------------------------

<class '__main__.NewClass'>
<__main__.NewClass object at 0x110cd7438>
```

Чаще всего классы создаются с помощью метаклассов. Давайте определим свой собственный метакласс Meta, который будет управлять поведением при создании класса. Для того чтобы он бы метаклассом, он должен наследоваться от другого метакласса (type). Метод метакласса `__new__` принимает название класса, его родителей и атрибуты. Мы можем определить новый класс A и указать, что его метаклассом является Meta. Именно этот метакласс и будет управлять поведением при создании нового класса. Таким образом, мы можем переопределить поведение при создании класса (например, добавить ему атрибут или сделать что-нибудь другое):

```python
class Meta(type):
    def __new__(cls, name, parents, attrs):
        print('Creating {}'.format(name))

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)


class A(metaclass=Meta):
    pass
    
-------------------------

Creating A
```

Например, мы можем определить метакласс, который переопределяет функцию `__init__`, и тогда каждый класс, созданный этим метаклассом, будет запоминать все созданные подклассы. Новый `__init__` записывает свой собственный атрибут, в котором будет храниться словарь созданных классов. В следующем примере у нас вначале создаётся класс Base, метаклассом которого является Meta, и у него создаётся атрибут класса registry, в который мы будем записывать все его подклассы. Каждый раз, когда у нас создаётся какой-то класс, который наследуется от Base, мы записываем в registry со- ответствующее значение, то есть название созданного класса и ссылку на него:

```python
class Meta(type):
    def __init__(cls, name, bases, attrs):
        print('Initializing — {}'.format(name))

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls
            
        super().__init__(name, bases, attrs)
        
        
class Base(metaclass=Meta): pass

class A(Base): pass

class B(Base): pass

---------------------------------------------

Initializing — Base
Initializing — A
Initializing — B
```

```python
print(Base.registry)
print(Base.__subclasses__())

-------------------------------------------------------

{'a': <class '__main__.A'>, 'b': <class '__main__.B'>}
[<class '__main__.A'>, <class '__main__.B'>]
```

## Абстрактные методы

В Python-е абстрактные методы реализованы **в стандартной библиотеки abc**. Здесь также работают метаклассы — они могут создать абстрактный класс с методом `@abstractmethod`. Декоратор @abstractmethod гарантирует, что у нас не получится создать класс-наследник, не определив этот метод — мы обязаны его переопределить в классе, который наследуется от нашего класса. В следующем примере Child не переопределяет метод send, и поэтому вызывается ошибка:

```python
from abc import ABCMeta, abstractmethod

class Sender(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        """Do something"""
```

```python
class Child(Sender): pass

Child()

----------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)
<ipython-input-15-5e10f1ccf1fd> in <module>()
      1 class Child(Sender): pass
      2 
----> 3 Child()

TypeError: Can't instantiate abstract class Child with abstract methods send
```

Переопределим метод send, и программа будет работать:

```python
class Child(Sender):
    def send(self):
        print('Sending')
        

Child()
--------------------------------------

<__main__.Child at 0x110cfa860>
```

На самом деле, абстрактные методы используются в Python-е довольно редко, чаще всего вызывается исключение `NotImplementedError`, которое говорит о том, что этот метод нужно реализовать. Программист видит в определении класса, что в методе вызываетсяraise `NotImplementedError`,и понимает,что этот метод нужно переопределить в потомке:

```python
class PythonWay:

    def send(self):
        raise NotImplementedError
```

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

- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions)

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
  
## Standard Exceptions

All exceptions are objects. The classes that define the objects are organized in a hierarchy, which is shown below. This is important because the parent class of a set of related exceptions will catch all exception messages for itself and its child exceptions. For example, an **ArithmeticError** exception will catch itself and all **FloatingPointError**, **OverflowError**, and **ZeroDivisionError** exceptions.

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

## Language Exceptions
<img src="https://github.com/ElizaLo/Practice-Python/blob/master/Python%203%20Programming/Language_Exceptions.png" width="692" height="666">

## Math Exceptions
<img src="https://github.com/ElizaLo/Practice-Python/blob/master/Python%203%20Programming/Math_Exceptions.png" width="689" height="524">

## Other Exceptions
<img src="https://github.com/ElizaLo/Practice-Python/blob/master/Python%203%20Programming/Other_Exceptions.png" width="682" height="368">

## Debugging and Testing in Python

- [pdb](https://docs.python.org/3/library/pdb.html) — The Python Debugger 
- [unittest](https://docs.python.org/3/library/unittest.html) — Unit testing framework
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — mock object library
  - [unittest.mock](https://docs.python.org/3/library/unittest.mock-examples.html) — getting started
  
## Parallelism in Python

- [multiprocessing](https://docs.python.org/3.6/library/multiprocessing.html) — Process-based parallelism
- [threading](https://docs.python.org/3.6/library/threading.html) - — Thread-based parallelism
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) — Launching parallel tasks
- [socket](https://docs.python.org/3.6/library/socket.html) — Low-level networking interface
