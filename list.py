
# list example

fruits_numbers = ['apple', 5, 'pear', 6, 'pomegranite', 7, 'banono', 8, 'lemon']


def print_fruit():
	for x in range (len(fruits_numbers)):
		print (fruits_numbers[x])
	print ("======================hehe hoho!======================")

def test_list():
	print_fruit()

	fruits_numbers.append(9)
	print_fruit()

	del fruits_numbers[1]
	print_fruit()

def list_add(games, food):
	favorites = games + food
	print(favorites)

def print_even_numbers(maxx):
	grup = 2
	while grup < maxx:
		print (grup)
		grup = grup + 2
	print ("========================hoho haha!===============")

def print_some_more_numbers(maxx, gupa):
	for i in range(gupa, maxx, 2):
		print(i)
	print ("========================hoho haha!===============")




if __name__ == '__main__':
    # test_list()

	# list1 = [1, 2, 3]
	# list2 = ["a", "b"]
	# list_add(list1, list2)

	# list4 = ["Papa", "is", "big..."]
	# list5 = ["Poo", "head!"]
	# list_add(list4, list5)
	
	# games = ["Sleeping", "ShuaLai", "Reading", "Hehe"]
	# foods = ["Spagehtti", "Mommy'sPizza", "MashedPotato"]
	# list_add(games, foods)

	# print_even_numbers(10)
	# print_even_numbers(20)
	# print_even_numbers(30)

	print_some_more_numbers(10, 2)
	print_some_more_numbers(20, 8)
	print_some_more_numbers(30, 12)


