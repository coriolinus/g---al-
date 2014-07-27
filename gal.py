"""
per https://github.com/eatnumber1/goal

g()('al') is a challenge whereby you need to write in as many languages as possible code which enables the code g()('al') to return the string "goal", the code g()()('al') to return the string "gooal", the code g()()()('al') return the string "goooal", etc.
"""

from functools import partial

def g(st=None, n=0):
	if st is None:
		return partial(g, n=n+1)
	else:
		return 'g' + ('o' * n) + st
		
		
if __name__ == '__main__':
	for i in range(5):
		call = 'g' + ('()' * i) + "('al')"
		res = eval(call)
		print call + ' -> ' + res