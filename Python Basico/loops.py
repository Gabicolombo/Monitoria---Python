arr = ['watson', 'assistant', 'watsonx']

# for el in arr:
#     print(el)

# for i in range(len(arr)):
#     print(arr[i])

# aux = 1

# while aux <= 5:
#     print(aux)
#     aux +=1 # aux = aux + 1 

while True:
    user_input = input("Me de seu nome, e se vc digitar end eu paro de perguntar: ")

    if user_input == 'end':
        break
    
    print(f'Olá {user_input}')


print('While ficou false')