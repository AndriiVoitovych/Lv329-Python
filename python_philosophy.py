python_philosophy = """\t\t\tThe Zen of Python, by Tim Peters.\n
\tBeautiful is better than ugly.
\tExplicit is better than implicit.
\tSimple is better than complex.
\tComplex is better than complicated.
\tFlat is better than nested.
\tSparse is better than dense.
\tReadability counts.
\tSpecial cases aren't special enough to break the rules.
\tAlthough practicality beats purity.
\tErrors should never pass silently.
\tUnless explicitly silenced.
\tIn the face of ambiguity, refuse the temptation to guess.
\tThere should be one-- and preferably only one --obvious way to do it.
\tAlthough that way may not be obvious at first unless you're Dutch.
\tNow is better than never."""
print (python_philosophy)
res1 = len(python_philosophy.split('better'))
print("The number of word 'better' is " + str(res1))
res2 = len(python_philosophy.split('never'))
print("The number of word 'never' is " + str(res2))
res3 = len(python_philosophy.split('is'))
print("The number of word 'is' is " + str(res3))

print (python_philosophy.upper())

print(python_philosophy.replace('i','&'))