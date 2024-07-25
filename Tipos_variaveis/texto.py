nome_completo = "sergio david baez"

nome_completo_aspas = """Sergio 
david
baez """

nome_completo_quebra = "sergio \
baez"

nome = "sergio"
sobrenome = "baez"

#Formatação

print("nome completo (1a forma):", nome_completo)
print("nome completo (2a forma):" + nome_completo)
print("nome completo (3a forma):" + "sergio" +"baez")
print("nome completo (4a forma):" + "sergio", "baez")
print("nome completo (5a forma):", nome_completo_aspas)
print("nome completo (6a forma):", nome_completo_quebra)
print("nome completo (7a forma):%s"% nome_completo)
print("nome completo (8a forma):%s %s"% (nome, sobrenome))
print(f"nome completo (9a forma):{nome} {sobrenome}")
print("nome completo (10a forma):{} {}".format(nome, sobrenome))





