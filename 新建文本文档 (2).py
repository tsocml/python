from functools import reduce
def str2float(s):
   def fn(x, y):
        return x * 10 + y
   def char2num(s):
         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
   return reduce(fn,map(char2num,s.replace(".","")))

s = '123.456'
if s.find('.') != -1:
	g = str2float(s) / pow(10,len(s) - s.find('.') - 1)
else:
	g = str2float(s)
print(g)

