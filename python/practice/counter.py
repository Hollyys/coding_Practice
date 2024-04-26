from collections import Counter

l = ["hi", "hey", "hi", "hi", "hello", "hey"]
print('\n',l)
print(Counter(l))

l = 'PORSCHE 911 GT3RS'
print('\n',l)
print(Counter(l))
counter = Counter(l)
print('P:', counter["P"])
print('R:', counter["R"])
print('K:', counter["K"])