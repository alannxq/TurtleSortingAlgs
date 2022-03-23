import turtle
import random
import time



def drawBars(nums):
	bar.color("black")
	bar.fillcolor("red")
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

	bar.end_fill()


def bubbleSort(arr):
	for _ in numbers:
		for index in range(len(arr) - 1):
			if numbers[index] > numbers[index + 1]:
				numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
			
			drawBars(numbers)
			turtle.update()
			time.sleep(SPEED)


def selection_sort(A):
	for i in range(len(A)):
		min_idx = i
		for j in range(i+1, len(A)):
			if A[min_idx] > A[j]:
				min_idx = j
	                    
		A[i], A[min_idx] = A[min_idx], A[i]

		drawBars(numbers)
		turtle.update()
		time.sleep(SPEED)


def insertionSort(arr):

	for i in range(1, len(arr)):
		key = arr[i]

		j = i-1
		while j >=0 and key < arr[j] :
			arr[j+1] = arr[j]
			j -= 1
			drawBars(numbers)
			turtle.update()
			time.sleep(SPEED)

		arr[j+1] = key

		drawBars(numbers)
		turtle.update()
		time.sleep(SPEED)


sort = input("a) bubble sort\nb) selection sort\nc) insertion sort\n\n> ")
NUM_BARS = int(input("\n\nEnter amount of bars to sort: "))


numbers = [random.randint(20,200) for _ in range(NUM_BARS)]

SPEED = 0.01 ## the lower the faster

WIDTH = 800 / NUM_BARS
START_POS = -((WIDTH * NUM_BARS) / 2), 0

if sort == "a":
	bar = turtle.Turtle()
	bar.hideturtle()
	turtle.tracer(0, 0)
	bubbleSort(numbers)
elif sort == "b":
	bar = turtle.Turtle()
	bar.hideturtle()
	turtle.tracer(0, 0)
	selection_sort(numbers)
else:
	bar = turtle.Turtle()
	bar.hideturtle()
	turtle.tracer(0, 0)
	insertionSort(numbers)
