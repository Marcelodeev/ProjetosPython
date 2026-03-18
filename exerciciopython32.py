# exercicio da pagina   32 



#Função Saudação: Crie uma função saudacao() que receba um nome  como argumento e imprima uma saudação personalizada.

def saudacao(nome):
    print(f"Minha saudação do exercicio é {nome} ")
saudacao("esse nome guardado")

# Função de Soma e Produto: Escreva uma função soma_produto() que receba dois números e retorne a soma e o produto deles. 

def soma_produto(a, b):
        
        return a + b
    
resultado = soma_produto(1,4)
print(resultado)

# 3 Função com Escopo Local: Crie uma função que defina uma variável local e a modifique. Tente acessar essa variável fora da função para ver o que acontece.

def modifica_local():
    a = 2
    print(a)
modifica_local()
    

# 4 Argumentos Padrão: Crie uma função conta_palavras que conte o número de palavras em uma string, com um argumento padrão para separar as palavras (espaço por padrão).

def nome_separado(texto):
    nome= texto.split(",")
    print(nome)
nome_separado("Marusvauda,Vismundina,gabrinusva,mascinustino")

import math

lista =[1,2,3,4,5,6,7,8,9,10]
numeros = list(range(11))

resultado1 = math.sqrt()


print(resultado1)
