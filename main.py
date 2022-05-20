import pygame 
from pygame.locals import *
import sys
import os
import numpy as np 
import time 
import copy

from creatures import *

pygame.init()


clock = pygame.time.Clock()
Width = 1200
Height = 960

square_length = 20
alive_color = '#21DEE5'
dead_color = '#343434'
border_color = '#6B6464'
# x = 100
# y = 45
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

screen = pygame.display.set_mode((Width, Height))

grid = np.zeros((Height//square_length,Width//square_length), dtype = int)




def add_creature(creature ,grid):

	for y, row in enumerate(creature):
		for x,cell  in enumerate(row):
			grid[(Height//(2*square_length))-len(creature[0])//2+y][(Width//(2*square_length))-len(creature[0])//2+x] = cell



def update(grid):
	
	grid_mod = copy.deepcopy(grid)

	for y, row in enumerate(grid):
		for x , cell in enumerate(row) :

			
			if (1 <	 x < len(row)-1) and (1 < y < len(grid)-1): 

				check_lst = []
				check_lst = [grid[y-1][x] ,grid[y+1][x] , grid[y-1][x-1],
							 grid[y-1][x+1], grid[y+1][x+1], grid[y+1][x-1],
				 			 grid[y][x-1], grid[y][x+1]]

				alive_neighbours = check_lst.count(1)


				if cell == 0 :

					if alive_neighbours == 3 :

						grid_mod[y][x] = 1 	
					
				else:
					if (alive_neighbours == 2) or (alive_neighbours== 3) :

						grid_mod[y][x] = 1  

					elif (alive_neighbours > 3 ) or (alive_neighbours < 2) :

						grid_mod[y][x] = 0

	return grid_mod

def setup(alive, dead,grid):
	for y, row in enumerate(grid):
		for x , cell in enumerate(row) :

			if cell == 0 :

				pygame.draw.rect(screen , dead , (x*square_length , y*square_length, square_length,square_length))

			else:
				pygame.draw.rect(screen , alive , (x*square_length , y*square_length, square_length,square_length))

			pygame.draw.rect(screen , border_color , (x*square_length , y*square_length, square_length+3,square_length+3),1)
	pygame.display.update()

add_creature(creature_1 ,grid)

def loop():
	global grid
	while True :
		screen.fill(dead_color)
		grid = update(grid)
		setup(alive_color,dead_color,grid)

		
		for event in pygame.event.get():

			if event.type == QUIT:
				pygame.quit()
				quit()
				sys.exit()

		pygame.display.update()
		clock.tick(10)
		

loop()				