#if #elif e else

#exemplo de if

idade = int(input("quanto anos você tem? "))
print("exemplo de comando if")
if idade >=18:
  print("você é maior de idade.")
elif idade >= 12:
  print("voce é um adolescente")
else:
  print("voce é menor de idade")

mensagem = "pode tirar a carteira de habilitação" if idade >= 18 else "voce não pode tirar a carteira de habilitação"
print(mensagem)