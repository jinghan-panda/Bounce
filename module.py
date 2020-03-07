import time
import sys


def ask_time():
	print('Type something:')    
	hehe = sys.stdin.readline()
	if hehe == 'Time?\n':
		print(time.asctime())
	else:
		print('What do you want?')

def ask_age():
	print('How old are you?')
	age = int(sys.stdin.readline())
	if age < 15 and age > 10:
		print('You are a medium poo!')
	elif age >= 15:
		print('You are a big poo!')
	else:
		print('You are a small poo!')

def moon_weight_in_years(curr_weight, in_years, percentage):
	wei = curr_weight

	for x in range(0, in_years):
		print('Year ' + str(x + 1) + ', weight on Earth: ' + str(wei) + 
			', weight on moon: ' + str(wei * percentage) )

		wei = wei + 1


if __name__ == '__main__':
	# for x in range(0, 5):
	# 	ask_age()
	
	moon_weight_in_years(curr_weight = 30, in_years = 5, percentage = 0.165)





