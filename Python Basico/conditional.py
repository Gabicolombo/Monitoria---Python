number = 0

if number > 0:
    print("Positivo")
else:
    print("Pode ser 0 ou negativo")

# print('------------------------')

# # if number > 0:
# #     print("Positivo")
# # elif number < 0:
# #     print("Negativo")
# # else:
# #     print("É 0")

# frase = 'Wa'

# if 't' in frase or 'a' in frase:
#     print('Está em frase')
# else:
#     print('não está na frase')

number = 2

# if 'number' in globals():
#     if(number >=0 ):
#         print('Sim')
#     else: 
#         print('Não')
# else:
#     print('Essa variável nem existe')

if 'number' in globals() and number >0:
    print('Sim')
else:
    print('Essa variável nem existe')