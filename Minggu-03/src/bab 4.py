>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>>fruits.count('tangerine')
0
>>>fruits.index('banana')
3
>>>fruits.index('banana', 4)  # Find next banana starting at position 4
6
>>>fruits.reverse()
>>>fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>>fruits.append('grape')
>>>fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>>fruits.sort()
>>>fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>>fruits.pop()
'pear'


>>>stack = [3, 4, 5]
>>>stack.append(6)
>>>stack.append(7)
>>>stack
[3, 4, 5, 6, 7]
>>>stack.pop()
7
>>>stack
[3, 4, 5, 6]
>>>stack.pop()
6
>>>stack.pop()
5
stack
[3, 4]


>>>from collections import deque
>>>queue = deque(["Eric", "John", "Michael"])
>>>queue.append("Terry")           # Terry arrives
>>>queue.append("Graham")          # Graham arrives
>>>queue.popleft()                 # The first to arrive now leaves
'Eric'
>>>queue.popleft()                 # The second to arrive now leaves
'John'
>>>queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])


>>> squares = []
>>>for x in range(10):
...    squares.append(x**2)
...
>>>squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


>>>matrix = [
...    [1, 2, 3, 4],
...    [5, 6, 7, 8],
...    [9, 10, 11, 12],
...]


>>>a = [-1, 1, 66.25, 333, 333, 1234.5]
>>>del a[0]
>>>a
[1, 66.25, 333, 333, 1234.5]
>>>del a[2:4]
>>>a
[1, 66.25, 1234.5]
>>>del a[:]
>>>a
[]


>>>t = 12345, 54321, 'hello!'
>>>t[0]
12345
>>>t
(12345, 54321, 'hello!')
>>># Tuples may be nested:
...u = t, (1, 2, 3, 4, 5)
>>>u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>># Tuples are immutable:
...t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>># but they can contain mutable objects:
...v = ([1, 2, 3], [3, 2, 1])
>>>v
([1, 2, 3], [3, 2, 1])


>>>basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>>print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>>'orange' in basket                 # fast membership testing
True
>>>'crabgrass' in basket
False

>>># Demonstrate set operations on unique letters from two words
...
>>>a = set('abracadabra')
>>>b = set('alacazam')
>>>a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>>a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>>a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>>a & b                              # letters in both a and b
{'a', 'c'}
>>>a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}


>>>tel = {'jack': 4098, 'sape': 4139}
>>>tel['guido'] = 4127
>>>tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>>tel['jack']
4098
>>>del tel['sape']
>>>tel['irv'] = 4127
>>>tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>>list(tel)
['jack', 'guido', 'irv']
>>>sorted(tel)
['guido', 'irv', 'jack']
>>>'guido' in tel
True
>>>'jack' not in tel
False


>>>knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>>for k, v in knights.items():
...    print(k, v)
...
gallahad the pure
robin the brave


>>>string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>>non_null = string1 or string2 or string3
>>>non_null
'Trondheim'


(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
