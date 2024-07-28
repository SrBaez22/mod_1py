#saudação
def saudacao(nome):
  
 print(f"ola, {nome}!")
print("chamando a função saudação")
saudacao("alice")
saudacao("bob")

#função com um retorno

def quadrado(numero):
 resultado = numero**2
 return resultado
resultado_quadrado = quadrado(6)
print("\nresultado do quadrado: ", resultado_quadrado)

def soma(numero1, numero2):
 resultado = numero1 + numero2
 return resultado
print("\nChamando a função soma")
numero1 = int(input("escolha um numero: "))
numero2 = int(input("escolha outro numero: "))
resultado_soma = soma(numero1, numero2)
print("a soma dos números %s e %s é %s"%(numero1, numero2, resultado_soma))