exemplos= {
1: list(range(0,10,2)),
2: list(range(10)),
3: list(range(5,15)),
4: list(range(0,-20,-1)),
5: list(range(0,80,2**2)),
6: list(range(0) ), 
}

exemplos:{1,2,3,4,5,6}

opcao = int(input("Escolha um exemplo de 1 a 6: "))
print()
if opcao > 6:
  print("Opção inválida. O número escolhido não pode ser maior que 6")
elif opcao < 1:
  print("Opção inválida. O número escolhido não pode ser menor que 1")
else:
  print(exemplos[opcao])