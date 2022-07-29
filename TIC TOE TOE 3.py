def display(a):
	print('   |  |')
	print(' ' + a[7] + ' | ' + a[8] + ' | ' + a[9])
	print('   |  |')
	print('-----------')
	print('   |  |')
	print(' ' + a[4] + ' | ' + a[5] + ' | ' + a[6])
	print('   |  |')
	print('-----------')
	print('   |  |')
	print(' ' + a[1] + ' | ' + a[2] + ' | ' + a[3])
	print('   |  |')	
def choosing_object():
	obj=''
	while obj not in ('X','O'):
		obj= input('Player 1, Choose: ')
		if obj=='X':
			return ('X','O')
		elif obj=='O':
			return ('O','X')
		else:
			print('Aole')
def win_check(a):
	if a[1]==a[2]==a[3]=='X' or a[4]==a[5]==a[6]=='X' or a[7]==a[8]==a[9]=='X' or a[1]==a[4]==a[7]=='X' or a[5]==a[2]==a[8]=='X' or a[6]==a[9]==a[3]=='X' or a[1]==a[5]==a[9]=='X' or a[5]==a[7]==a[3]=='X' or a[1]==a[2]==a[3]=='O' or a[4]==a[5]==a[6]=='O' or a[7]==a[8]==a[9]=='O' or a[1]==a[4]==a[7]=='O' or a[5]==a[2]==a[8]=='O' or a[6]==a[9]==a[3]=='O' or a[1]==a[5]==a[9]=='O' or a[5]==a[7]==a[3]=='O':
		return True
	else:
		return False
def empty_or_not(a,position):
	if a[position]=='':
		return True
	else:
		return False
def input_validator(position):
	if position not in range(1,10) and  not empty_or_not(a,position):
		return False
	else:
		return True
def position_input():
	b=False
	while b==False:
	    position=int(input('Which position: '))
	    if input_validator(position):
	    	b=True
	    else:
	    	print('Pic the correct position Aole')
	    return position

def who_goes_first():
	import random
	if random.randint(0,1) == 0:
		return 'Player 1'
	else:
		return 'Player 2'
def fulla(a):
	for i in range(1,10):
		if empty_or_not(a,i):
			return False
	return True				
def replay():
	return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
print("TIC TAC TOE")
f=True
while f==True:
	a=['']*10
	display(a)
	player1,player2=choosing_object()
	d=who_goes_first()
	print(d+' goes first')
	e=True
	while e:
		if d=='Player 1':
			
			pos=position_input()
			a[pos]=player1
			display(a)
			if win_check(a):
				print('Player 1 wins')
				break
			else:
				if fulla(a):
					print('Draw!')
					break
				else:
					d='Player 2'
		elif d=='Player 2':
			
			pos=position_input()
			a[pos]=player2
			display(a)
			if win_check(a):
				print('Player 2 wins')
				break
			else:
				if fulla(a):
					print('Draw!')
					break
				else:
					d='Player 1'
	if not replay():
		f=False

    










	















    


