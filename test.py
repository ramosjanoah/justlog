import justlog as jl
from justlog import printl

xs = 'I love Python! Python is the best programming computer'
dict__ = {}
i = 0
for x in xs:
	dict__[x] = i
	i += 1

printl('Hai')
printl(str(('this is the dict', dict__)))