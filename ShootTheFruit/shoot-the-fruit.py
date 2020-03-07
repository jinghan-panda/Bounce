from random import randint

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
	new_x = randint(10, 800)

	apple.x = new_x
	print(f"new_x: {new_x}")

	new_y = randint(10, 600)

	apple.y = new_y
	print(f"new_y: {new_y}")

def on_mouse_down(pos):
	if apple.collidepoint(pos):
		print("Good shot!")

		place_apple()

	else:
		print("You missed!")
		quit()

