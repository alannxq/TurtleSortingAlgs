import turtle
import random
import time

bar = turtle.Turtle()
bar.hideturtle()
turtle.tracer(0, 0)

NUM_BARS = 100
SPEED = 0.01 ## the lower the faster

WIDTH = 800 / NUM_BARS
START_POS = -((WIDTH * NUM_BARS) / 2), 0

numbers = [random.randint(20,200) for _ in range(NUM_BARS)]


def drawBars(nums):
	bar.begin_fill()
	bar.clear() ## clear previous drawings
	bar.penup()
	bar.goto(START_POS) ## go to start
	bar.pendown()
	bar.seth(90) ## point up // set-h(eading)

	for HEIGHT in nums:
		bar.forward(HEIGHT) ## left side of bar
		bar.right(90)
		bar.forward(WIDTH) ## draw top
		bar.right(90)
		bar.forward(HEIGHT) ## go back down, right side of bar
		bar.left(180) ## after going down, turn around for next bar


def bubbleSort(arr):
	for _ in numbers:
		for index in range(len(arr) - 1):
			try:
				if numbers[index] > numbers[index + 1]:
					numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
			except:
				pass
			
			drawBars(numbers)
			turtle.update()
			time.sleep(SPEED)

bubbleSort(numbers)
