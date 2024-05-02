def print_params(a=1, b='star', c=True):
    print(a, b, c, )


print_params()
print_params(5)
print_params(10, 'str')
print_params(13, 'string', False)

print_params(b=25)
print_params(c=[1,2,3])

values_list = [[1, 2], 'rats', (3, 4)]
values_dict = {'a': 'str', 'b': [23, 'star'], 'c': {'a': 71, 'b': True}}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [2, 'shot']

print_params(*values_list2, 42)
