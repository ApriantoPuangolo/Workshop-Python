>>>import os
>>>os.getcwd()      # Return the current working directory
'C:\\Python311'
>>>os.chdir('/server/accesslogs')   # Change current working directory
>>>os.system('mkdir today')   # Run the command mkdir in the system shell
0

>>>import os
>>>dir(os)
<returns a list of all module functions>
>>>help(os)
<returns an extensive manual page created from the module's docstrings>

>>>import shutil
>>>shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>>shutil.move('/build/executables', 'installdir')
'installdir'

>>>import sys
>>>print(sys.argv)
['demo.py', 'one', 'two', 'three']

import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

>>>sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one

>>>import re
>>>re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>>re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'

>>>'tea for too'.replace('too', 'two')
'tea for two'

>>>import math
>>>math.cos(math.pi / 4)
0.70710678118654757
>>>math.log(1024, 2)
10.0

>>>import random
>>>random.choice(['apple', 'pear', 'banana'])
'apple'
>>>random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>>random.random()    # random float
0.17970987693706186
>>>random.randrange(6)    # random integer chosen from range(6)
4

>>>import statistics
>>>data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>>statistics.mean(data)
1.6071428571428572
>>>statistics.median(data)
1.25
>>>statistics.variance(data)
1.3720238095238095

>>>from urllib.request import urlopen
>>>with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...    for line in response:
...        line = line.decode()             # Convert bytes to a str
...        if line.startswith('datetime'):
...            print(line.rstrip())         # Remove trailing newline
...
datetime: 2022-01-01T01:36:47.689215+00:00

>>>import smtplib
>>>server = smtplib.SMTP('localhost')
>>>server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
..."""To: jcaesar@example.org
...From: soothsayer@example.org
...
...Beware the Ides of March.
...""")
>>>server.quit()

>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368

>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979

>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
