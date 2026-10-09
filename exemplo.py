produto = "Mouse Gamer Wifi"
valores = [20, 71, 100, 30]



def dobrar(valor):
    resultado = valor * 2
    return resultado
print(dobrar(10))

valores_novos = []
for item in valores:
    valores_novos.append (dobrar(item))
print(valores)
print(valores_novos)

prooduto = input("Digite o produto que deseja: ")
if "mouse".lower() in produto.lower():
    print("Produto encontrado")

else:
    print("Produto não encontrado")




alunos = ["Ana", "Hugo", "Mariana", "Pedro", "Ana Paula"]

aluno_procurado = input("Digite um nome: ")

alunos_encontrados = []
for aluno in alunos:
    alunos_encontrados.append(item)
print(alunos_encontrados)