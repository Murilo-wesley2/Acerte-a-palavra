from random import choice

palavras=['tartaruga','macaco','gato','sapo','cobra','leopardo','papagaio','raposa','abelha','corvo']
letras=[]
chances=5
escolha='#'
x=[]
locais=[]
local=0
derrota=0
vitoria=0
opc=''


def game(x):
	for letra in x:
		print(letra,end=' ')
	print()
	
def gerador():
	global x, escolhida,locais,opc,chances,letras
	x=[]
	locais=[]
	opc=''
	chances=5
	letras=[]
	for c in range(0,len(escolhida)):
		x.append('_')
		
while True:
	escolhida=choice(palavras)
	gerador()
	while True:
		game(x)
		print(f'\033[33mvocê tem {chances} chances\033[m')
		while True:
			escolha=input('digite uma letra:')
			if len(escolha)>1 or len(escolha)==0:
				print('\033[31mdigite apenas uma letra\033[m')
			elif escolha in letras:
				print('\033[31mvocê já digitou esta letra\033[m')
			else:
				letras.append(escolha)
				break
		
		if '_' in x:
			if escolha in escolhida:
				letra=escolhida.count(escolha)
				temporario=0
				for c in range(len(escolhida)):
					if escolhida[c]==escolha:
						x[c]=escolha
			else:
				chances-=1
			if chances<1:
				game(x)
				print('você perdeu')
				print(f'o animal era {escolhida}')
				derrota+=1
				break
			
			elif '_' not in x:
				game(x)
				print('parabêns você ganhou')
				vitoria+=1
				break
	while opc != 's' and opc != 'n':
		opc=input('você quer continuar [s/n]:').lower()
	if opc=='n':
		break

print(f'você ganhou {vitoria} vezes e perdeu {derrota} vezes.')	