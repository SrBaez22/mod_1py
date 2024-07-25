#declaração

minha_lista = [1, 2, 3, 4, 5, "sergio", True, False]

#printar
print("minha lista de exemplos",minha_lista)

#printar indices
minha_lista[0] = "python"

print("minha lista de exemplos",minha_lista)
print("minha lista:", minha_lista[0])
print("lista fatiada:",minha_lista[1:7])
print("lista fatiada:",minha_lista[:6])
print("lista fatiada:",minha_lista[2:])

#metodos de lista

#metodo apppend(): Adiciona um elemento ao final da lista 
minha_lista.append(6)
print("apos append(6):",minha_lista)

#método index
indice = minha_lista.index(6)
print("me mostre o indice do elemento (6):",indice)

#metodo insert: insere um elemento num indice especifico
minha_lista.insert(2, 10)
print("após o insert:", minha_lista)

#metodo pop

elemento_removido = minha_lista.pop(3)
print("elemento removido:",elemento_removido)
print("minha lista após o pop:", minha_lista)

#metodo remove

minha_lista.remove(True)
print("minha lista após o metodo remove:",minha_lista)

#metodo sort 
minha_lista.sort()
print("minha lista após o sort:", minha_lista)