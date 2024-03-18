import sys
import re
import time
import collections

#1
print(sys.path)

#2
text = 'mi texto es lo nuevo que tengo que estar asiendo para generar 4 6 nuevo capital'
result = re.findall('[0,9]+', text)

#3
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

#4
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)