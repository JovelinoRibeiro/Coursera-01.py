#Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da 
nome = input("Digite o nome do cliente: ")
vencimento = int(input("Digite o dia de vencimento: "))
mes = input("Digite o mês de vencimento: ")
valor = float(input("Digite o valor da fatura: "))
print(" Olá, {}  A sua fatura com vencimento em {} de {} no valor de {:.2f} está fechada. ".format(nome, vencimento, mes, valor))
