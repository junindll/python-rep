nome = input(str('Qual seu nome? '))
altura = float(input('Qual sua altura? '))
peso = int(input('Qual seu peso? '))
imc = (peso / altura ** 2)
print('{}, tem {:.2f}, pesa {} kg e seu imc corporal é {:.2f}'.format(nome, altura, peso, imc))