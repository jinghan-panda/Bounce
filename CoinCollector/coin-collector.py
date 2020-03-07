from random import randint
WIDTH = 400
HEIGHT = 400

score = 0

game_over = False


fox = Actor("hedgehog")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
	global score 

	screen.fill("purple")
	fox.draw()
	coin.draw()
	screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

	if game_over:
		screen.fill("blue")
		screen.draw.text("Final score: " + str(score), topleft=(10, 10), fontsize = 60)

def place_coin():
	coin.x = randint(20, (WIDTH - 20))
	coin.y = randint(20, (HEIGHT - 20))

def time_up():
	global game_over
	game_over = True

def update():
	global score, fox, coin
	step = 4
	if keyboard.left:
		fox.x = fox.x - step

	elif keyboard.right:
		fox.x = fox.x + step

	elif keyboard.up:
		fox.y = fox.y - step

	elif keyboard.down:
		fox.y = fox.y + step

	coin_collected = fox.colliderect(coin)

	if coin_collected:
		score = score + 10
		place_coin()

clock.schedule(time_up, 30.0)
place_coin()


