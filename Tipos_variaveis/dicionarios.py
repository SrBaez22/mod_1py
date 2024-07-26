#não ordenadas: não podem ser ordenados
#chave valor: possuem uma chave e um valor

#criando um dicionário
pessoa = {"nome": "joão", "idade": 30, "cidade": "são paulo"}

print("meu dicionário de exemplo: ", pessoa)

#acessando valores por chave

print("nome:", pessoa["nome"])
print("idade:", pessoa["idade"])
print("cidade:", pessoa ["cidade"])

pessoa["sobrenome"] = "silva"
print("sobrenome:", pessoa["sobrenome"])

#atualizando dados do dicionário
pessoa["idade"] = 31
print("idade atualizada:", pessoa["idade"])

#remover um par chave-valor
print("meu dicionário de exemplo: ", pessoa)
del pessoa["sobrenome"] 
print("meu dicionário de exemplo: ", pessoa)


#método keys(): retorno de todas as chaves
chaves = list(pessoa.keys())
print("chaves do dicionário:", chaves)
print("primera chave:", chaves[0])

#método values():retorno de todos os valores em formato de lista
valores = list(pessoa.values())
print("valores do meu dicionário:", valores)
print("primeiro valor do meu dicionário:", valores[0])

#método items(): lista de tuplas contendo todos os pares chave-valor
items = list(pessoa.items())
print("pares chave-valor do dicionário:", items)
print("primeiro valor do meu dicionário:", items[0][1])
print("primeira chave-valor: %s = %s"% (items[0][0], items[0][1]))
