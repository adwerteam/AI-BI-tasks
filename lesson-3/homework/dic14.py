my_dict = {'a': 1, 'b': 2, 'c': 1}
keys_with_1 = [k for k, v in my_dict.items() if v == 1]
print(keys_with_1)  # Output: ['a', 'c']
