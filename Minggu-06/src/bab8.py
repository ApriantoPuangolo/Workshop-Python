>>>while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
  
  >>>10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>>'2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
  
  >>>while True:
...    try:
...        x = int(input("Please enter a number: "))
...        break
...    except ValueError:
...        print("Oops!  That was no valid number.  Try again...")
...

>>>raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
  
  raise ValueError  # shorthand for 'raise ValueError()'
  
  >>>try:
...    raise NameError('HiThere')
...except NameError:
...    print('An exception flew by!')
...    raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
  
  >>>try:
...    open("database.sqlite")
...except OSError:
...    raise RuntimeError("unable to handle error")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: unable to handle error
  
  # exc must be exception instance or None.
raise RuntimeError from exc

>>>def func():
...    raise ConnectionError
...
>>>try:
...    func()
...except ConnectionError as exc:
...    raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
  
  >>>try:
...    open('database.sqlite')
...except OSError:
...   raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError

>>>try:
...    raise KeyboardInterrupt
...finally:
...    print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  
  >>>def bool_return():
...    try:
...        return True
...    finally:
...        return False
...
>>>bool_return()
False

>>>def divide(x, y):
...    try:
...        result = x / y
...    except ZeroDivisionError:
...        print("division by zero!")
...    else:
...        print("result is", result)
...    finally:
...        print("executing finally clause")
...
>>>divide(2, 1)
result is 2.0
executing finally clause
>>>divide(2, 0)
division by zero!
executing finally clause
>>>divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
    
    for line in open("myfile.txt"):
    print(line, end="")
    
    with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
        
        >>>def f():
...    excs = [OSError('error 1'), SystemError('error 2')]
...    raise ExceptionGroup('there were problems', excs)
...
>>>f()
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |   File "<stdin>", line 3, in f
  | ExceptionGroup: there were problems
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
>>>try:
...    f()
...except Exception as e:
...    print(f'caught {type(e)}: e')
...
caught <class 'ExceptionGroup'>: e
>>>

>>>def f():
...    raise ExceptionGroup("group1",
...                         [OSError(1),
...                          SystemError(2),
...                          ExceptionGroup("group2",
...                                         [OSError(3), RecursionError(4)])])
...
>>>try:
...    f()
...except* OSError as e:
...    print("There were OSErrors")
...except* SystemError as e:
...   print("There were SystemErrors")
...
There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |   File "<stdin>", line 2, in f
  | ExceptionGroup: group1
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
>>>

>>>excs = []
...for test in tests:
...    try:
...        test.run()
...    except Exception as e:
...        excs.append(e)
...
>>>if excs:
...   raise ExceptionGroup("Test Failures", excs)
...

>>>try:
...    raise TypeError('bad type')
...except Exception as e:
...    e.add_note('Add some information')
...    e.add_note('Add some more information')
...    raise
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: bad type
Add some information
Add some more information
>>>

>>>def f():
...    raise OSError('operation failed')
...
>>>excs = []
>>>for i in range(3):
...    try:
...        f()
...    except Exception as e:
...        e.add_note(f'Happened in Iteration {i+1}')
...        excs.append(e)
...
>>>raise ExceptionGroup('We have some problems', excs)
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  | ExceptionGroup: We have some problems (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 1
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 2
    +---------------- 3 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 3
    +------------------------------------
>>>
