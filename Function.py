def soma():

 num01 = 10
 num02 = 20

 resultado = num01 + num02

 return resultado

def somarDoisNumeros(nota_01, nota_02):
 num_01 = nota_01
 num_02 = nota_02

 resultado = num_01 + num_02

 return print(resultado)

#somarDoisNumeros(24,98)


def multiplicacao():

 num_01 = 44
 num_02 = 6

 resultado = num_01 * num_02

 return resultado 

def multiplicarDoisNumeros (nota_01, nota_02):
 num_01 = nota_01
 num_02 = nota_02
 resultado = num_01 + num_02
 return print(resultado)
#multiplicarDoisNumeros(24,98)


def divisao():

 num01 = 10
 num02 = 20

 resultado = num01 / num02

 return resultado

def dividirDoisNumeros(nota_01, nota_02):
 num_01 = nota_01
 num_02 = nota_02

 resultado = num_01 + num_02

 return print(resultado)

#dividirDoisNumeros(24,98)

def cadastrar(nome, idade):
    data = {
        "nome": nome,
        "idade": idade
    }
    return print(data)

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

cadastrar(nome, idade)
