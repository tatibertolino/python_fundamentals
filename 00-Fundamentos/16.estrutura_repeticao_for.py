""""python"

letra = p
letra = y
letra = t
letra = h
letra = o
letra = n"""

texto = input("Informe um texto: ")
#texto = ""
VOGAIS = "AEIOU"

#exemplo usando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else: #não é comum, só pra saber q existe 
    print() # adiciona quebra de linha

#exemplo usando função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ") #end deixa os caracteres todos na mesma linha

