arr = [1, 9, 3]

# quero adicionar o elemento 4
arr.append(4)
print(arr)

# extend()
arr.extend([5, 4.5, 1, 8])
print(arr)

# insert
arr.insert(0, 10)
print(arr)

# remove()
arr.remove(4)
print(arr)

# pop()
item_removido = arr.pop(2)
print(f"lista atualizada: {arr}, foi removido o item {item_removido}")

# # clear()
# arr.clear()
# print(arr)

index = arr.index(1)
print(index)

# count
ocorrencias = arr.count(1)
print(ocorrencias)

# sort()
arr.sort()
print(arr)

# reverse()
arr.reverse()
print(arr)

