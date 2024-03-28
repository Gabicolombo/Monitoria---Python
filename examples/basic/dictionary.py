dicionarios = {'a': 1, 'b': 2, 'c': 3}

print(f"valor da chave b: {dicionarios['b']}")

dicionarios['d'] = 4

print(dicionarios)

dicionarios['c'] = ['watson', 'assistant']

print(dicionarios)

del dicionarios['a']
print(dicionarios)