# What we should do for having a dictionary that has order (dictionaries do not have order)
# Answer: Use OrderedDict function from collections module

from collections import OrderedDict

definition = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
definition['six'] = 6
OrderedDict((word, True) for word in definition)
print(definition)