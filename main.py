## an inefficient
## sorting algorith visualisation
## completely done in turtle

## it should be easy to add sorting algoriths

import turtle
import random
import time

current_bar = None
current_bar_2 = None
current_alg = None
str_current_alg = None
is_running = False

NUM_BARS = 100
SPEED = 0.01 ## the lower the faster
WIDTH = 900 / NUM_BARS
START_POS = -((WIDTH * NUM_BARS) / 2), -400

screen = turtle.Screen()

bar = turtle.Turtle()
bar.pensize(1)
bar.hideturtle()
turtle.tracer(0, 0)


sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("black")
sketch.penup()
sketch.hideturtle()
sketch.goto(-150, 150)
sketch.write(f"Algorithm: {current_alg}", font=("Iosevka Medium", 24, "normal"))

numbers = [random.randint(1,100) for _ in range(NUM_BARS)]

def drawBar(HEIGHT, WIDTH, x):
	global numbers
	#HEIGHT = 800 - (HEIGHT - min(numbers)) * math.floor((800 - 100) / ((max(numbers)) - min(numbers)))
	HEIGHT = HEIGHT + 150 * (HEIGHT / 800 * 20)
	bar.penup()
	bar.goto(x, bar.ycor())
	bar.seth(90)
	bar.down()
	bar.begin_fill()
	bar.forward(HEIGHT) ## left side of bar
	bar.right(90)
	bar.forward(WIDTH) ## draw top
	bar.right(90)
	bar.forward(HEIGHT) ## go back down, right side of bar
	bar.right(90)
	bar.forward(WIDTH)
	bar.end_fill()

def drawBars(nums):
	global current_bar, WIDTH, START_POS
	bar.clear()
	bar.penup()
	bar.pendown()
	bar.goto(START_POS)
	temp_width = START_POS[0]
	for index, num in enumerate(nums):
		bar.fillcolor("grey")
		if index == current_bar or index == current_bar_2:
			bar.fillcolor("red")
		drawBar(num, WIDTH, temp_width)
		temp_width += WIDTH 


def bogoSort():
	global numbers
	nums = numbers
	while not all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)):
		random.shuffle(nums)

		yield nums



def bubbleSort():
	global current_bar, current_bar_2, numbers, is_running
	if is_running:
		for _ in numbers:
			for index in range(len(numbers) - 1):
				if numbers[index] > numbers[index + 1]:
					numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
					current_bar = index
					current_bar_2 = index + 1
				

				yield numbers
		is_running = False


def selectionSort():
	global current_bar, current_bar_2, numbers, is_running
	if is_running:
		A = numbers
		for i in range(len(A)):
			min_idx = i
			for j in range(i + 1, len(A)):
				if A[min_idx] > A[j]:
					min_idx = j
		                    
			A[i], A[min_idx] = A[min_idx], A[i]


			#####################
			current_bar = i
			current_bar_2 = min_idx



			yield A
		is_running = False


def insertionSort():
	global current_bar, current_bar_2, numbers
	arr = numbers
	for i in range(1, len(arr)):
		key = arr[i]

		j = i-1
		while j >=0 and key < arr[j] :
			arr[j+1] = arr[j]
			j -= 1
			current_bar = i
			current_bar_2 = j

			yield arr

		arr[j+1] = key

		


def updateText():
	global sketch
	sketch.clear()
	sketch.write(f"Algorithm: {str_current_alg}\n\nStart Sorting \t| SPACE\nBubble Sort \t| B\nSelection Sort \t| S\nInsertion Sort \t| I\nBogo Sort \t| L\nReset Bars \t| R", 
		font=("Iosevka Medium", 19, "normal")
		)

def doSort():
	global current_alg
	for result in current_alg():
		drawBars(result)
		turtle.update()


def reset():
	global numbers, is_running
	numbers = [random.randint(1,100) for _ in range(NUM_BARS)]
	is_running = False


def isRunning():
	global is_running
	is_running = not is_running

def set_bubbleSort():
	global current_alg, str_current_alg
	current_alg = bubbleSort
	str_current_alg = "Bubble Sort"

def set_selectionSort():
	global current_alg, str_current_alg
	current_alg = selectionSort
	str_current_alg = "Selection Sort"

def set_insertionSort():
	global current_alg, str_current_alg
	current_alg = insertionSort
	str_current_alg = "Insertion Sort"

def set_bogoSort():
	global current_alg, str_current_alg
	current_alg = bogoSort
	str_current_alg = "Bogo Sort"


screen.listen()
screen.onkeypress(reset, "r")
screen.onkeypress(isRunning, "space")
screen.onkeypress(set_bubbleSort, "b")
screen.onkeypress(set_selectionSort, "s")
screen.onkeypress(set_insertionSort, "i")
screen.onkeypress(set_bogoSort, "l")


while True:
	if is_running:
		if current_alg != None:
			doSort()

	updateText()
	drawBars(numbers)
	turtle.update()
