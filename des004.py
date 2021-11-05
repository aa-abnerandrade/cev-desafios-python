# Fazer um programa que leia algo e mostre o tipo primitvo e demais informações
print ('===== DESAFIO 04 =====')


answer = str(input('\n Digite qualquer caractere: ', ))
print('É ou não é? ')
print('O caractere é do tipo : ', type(answer))
print('É numérico? ', answer.isnumeric())
print('É alfabético? ', answer.isalpha())
print('É alfanumérico? ', answer.isalnum())
print('Está em letras maiúsculas? ', answer.isupper())
print('Está em letras minúsculas?', answer.islower())
print('Está capitalizada? ', answer.istitle())
print('Todos os caracteres são imprimíveis? ', answer.isprintable())
print('É composto de apenas espaços? ', answer.isspace())
