justlog is a simple package to write to command prompt and file. You can change the log file if you want.

This is my code example for printing

```python
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
```

And the result would be like

```console
[I] 18-26-05 10:04:38 -- Hai
[I] 18-26-05 10:04:38 -- {' ': 45,
                          '!': 13,
                          'I': 0,
                          'P': 15,
                          'a': 39,
                          'b': 29,
                          'c': 46,
                          'e': 52,
                          'g': 44,
                          'h': 26,
                          'i': 42,
                          'l': 2,
                          'm': 48,
                          'n': 43,
                          'o': 47,
                          'p': 49,
                          'r': 53,
                          's': 31,
                          't': 51,
                          'u': 50,
                          'v': 4,
                          'y': 16}
```

Feel free to use!