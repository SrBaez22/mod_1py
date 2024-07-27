print("for utilizando lista")
lista = [1, 2, 3, 4, 5]
for i in lista: 
  print(i)

print("for utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for j in tupla:
  print(j)


pessoa = {"nome":"joão", "idade":30, "cidade":"manaus"}
print("for utilizando dicionário - chaves")

for chave in pessoa.keys():

  print(chave)

print("for utilizando dicionário - valor")

for valor in pessoa.values():
  print(valor)

for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")

  # range(): intervalo numerico
  #[0, 1,2,3,4,5,6,7,8,9]
for numero in range(1,5):
  print("numero: ", numero)

#função range com len
print("\nutilizando a função range com len")
lista = [1, 2, 3, 4, 5]
for indice in range(0,len(lista)):
  print("indice:", indice)