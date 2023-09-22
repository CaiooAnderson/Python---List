exemplos = {
    1: list(range(0, 10, 2)),
    2: list(range(10)),
    3: list(range(5, 15)),
    4: list(range(0, -20, -1)),
    5: list(range(0, 80, 2**2)),
    6: list(range(0)),
}
# Listagem dos exemplos que fiz
# while True para repetições
while True:
    opcao = int(input("Escolha um exemplo de 1 a 6: \n"))
    print() # aqui vai printar o input da opcao para que a pessoa escolha

    if opcao > 6 or opcao < 1: # coloquei assim, pois se a pessoa usar números quebrados irá dar erro por conta do 'int' na opcao
        print("Opção inválida! A opção deve ser entre os números 1 e 6!\n")
        continuar = input(str("\nDeseja continuar? (s) para sim e (n) para não!\n")) # caso queira testar outro exemplo da lista
        if continuar == 's':
          print()
          continue # faz com que o programa volte ao loop
        elif continuar == 'n':
          print("Programa encerrado.")
          break # encerra o programa
    else:
        print(exemplos[opcao])
        continuar = input(str("\nDeseja continuar? (s) para sim e (n) para não!\n")) # caso queira testar outro exemplo da lista ou escolher o certo agora
        if continuar == 's':
          print()
          continue
        elif continuar == 'n':
           print("Programa encerrado.")
           break 