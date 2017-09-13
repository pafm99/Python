# MAKE DICT FROM 2 LISTS
keys = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
vals = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1,arr2):
    new_dict = {}
    new_dict = dict(zip(arr1,arr2))
    return new_dict

print make_dict(keys,vals)
