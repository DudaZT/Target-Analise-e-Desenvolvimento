# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def contarA(string):
    contador = string.lower().count('a')
    
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

string = input("Digite uma palavra: ")

contarA(string)
