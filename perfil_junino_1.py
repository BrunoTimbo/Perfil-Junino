print("\nPERFIL JUNINO - Veja quem é você nesse São joão")

print("\nPergunta 1:\na. \nb. \nc. \nd.")
resposta1 = input("Digite a opção: ")

if resposta1 == "a" or resposta1 == "b" or resposta1 == "c" or resposta1 == "d":
   print("\nPergunta 2:\na. \nb. \nc. \nd.")
   resposta2 = input("Digite a opção: ")

   if resposta2 == "a" or resposta2 == "b" or resposta2 == "c" or resposta2 == "d":
      print("\nPergunta 3:\na. \nb. \nc. \nd.")
      resposta3 = input("Digite a opção: ")

      if resposta3 == "a" or resposta3 == "b" or resposta3 == "c" or resposta3 == "d":
         print("\nPergunta 4:\na. \nb. \nc. \nd.")
         resposta4 = input("Digite a opção: ")
      else:
         print("Opção Inválida! Digite uma letra das opções disponíveis.")
   else:
         print("Opção Inválida! Digite uma letra das opções disponíveis.")
else:
   print("Opção Inválida! Digite uma letra das opções disponíveis.")








if resposta1 == "a" and resposta2 == "a" and resposta3 == "a" and resposta4 == "a":
    print("Perfil 1")

elif resposta1 == "b" and resposta2 == "b" and resposta3 == "b" and resposta4 == "b":
   print("Perfil 2")

elif resposta1 == "c" and resposta2 == "c" and resposta3 == "c" and resposta4 == "c":
   print("Perfil 3")

elif resposta1 == "d" and resposta2 == "d" and resposta3 == "d" and resposta4 == "d":
   print("Perfil 4")       