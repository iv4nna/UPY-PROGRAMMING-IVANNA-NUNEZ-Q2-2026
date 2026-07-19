import random
import stddraw

from color import Color

def bubble_sort(numbers):
    #Get the length of the array
    n = len(numbers)
    
    for sweep in range (n):
        for pair in range (0, n-1 - sweep):
            if numbers[pair] > numbers[pair] + 1:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]

def draw_bars (numbers, selected=()):
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n
    
    for i, number in enumerate(numbers):
        x= i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(500)
    
# ANIMATED
def bubble_sort_animated(numbers):
    # CONIG - Canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    #get the lenght of the array
    n = len(numbers)
    
    for sweep in range(n):
        for pair in range( 0, n-1 - sweep):
            #DRAW the rectangles before the swap
            draw_bars(numbers, selected= (pair, pair +1))
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers [pair+1], numbers[pair]
                #DRAW the rentangles after the swap
                draw_bars(numbers, selected= (pair, pair +1))
                
    draw_bars(numbers)
    stddraw.show()

numbers = [random.randint(0,100) for x in range(10)]
print(f"Before bubble sort: {numbers}")
#bubble_sort(numbers)
bubble_sort_animated(numbers)
print(f"After bubble sort: {numbers}")