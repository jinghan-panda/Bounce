class Things:
	pass


class Inanimate(Things):
	pass


class Animate(Things):
	pass


class Animals(Animate):
	def play(self):
		print('Playing')

	def eat(self):
		print('Eating')

	def sleep(self):
		print('Zzz...')


class Panda(Animals):
	def eat_bamboo(self):
		pass

if __name__ == '__main__':
	Jinghan = Panda()
	Jinghan.play()
	Jinghan.eat()
	Jinghan.sleep()

