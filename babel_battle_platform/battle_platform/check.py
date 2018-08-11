import sys
import time

file_name = sys.argv[1]
print (file_name)
f = open(file_name, 'a+')
for i in range(10):
    time.sleep(1)
    f.write("123")
f.close()
