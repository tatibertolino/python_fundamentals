while True:
   numero = int(input("Informe um número: "))

   if numero == 10:
       break

   print(numero, end=" ") 

for numero in range(100):

   if numero == 10: 
       break #para a excução na condição
   print(numero, end=" ")

    
for numero in range(100):

    if numero == 10:
        continue #pula a execução da condição
    print(numero, end=" ") 
          
for numero in range(100):

    if numero % 2 == 0: #só exibe números ímpares. pares dividos por 2 não resta nada
        continue #pula a execução da condição
    print(numero, end=" ") 


