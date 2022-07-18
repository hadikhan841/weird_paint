# Weird Paint by Haplook(@hapolook on twitter)

'''
Pygame is a SDL based library to create 2d graphics and games. For more information visit www.pygame.org.
Tkinter is a built-in library in python to create Graphical User Interface. 
'''
import pygame
import tkinter as tk
from tkinter.colorchooser import askcolor
from sys import exit

pygame.init()

#Setting up the main window
screen = pygame.display.set_mode((800,800))
screen.fill("White")
pygame.display.set_caption("Weird Paint")
pygame.mouse.set_cursor(*pygame.cursors.arrow)

#Pen configs
x = 400
y = 400
speed = 0.1
pen_size = 1

def change_color():
    colors = askcolor(title="Color Chooser")
    selected_color = colors[0]
	return selected_color

#color picker built with tkinter
def color_picker():
	root = tk.Tk()
	root.title('Color Chooser')
	root.geometry('200x100')
	tk.Button(root,text='Select a Color',command=change_color).pack(expand=True)
	root.mainloop() 

#color picker must pop up at the first	
color_picker()

#Main Loop
while True:
        
		# Wait What??
		player = pygame.draw.circle(screen,selected_color,(x,y),pen_size)
        
        for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			#Mouse input mangement    
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1: #Left mouse button
					pos = pygame.mouse.get_pos()
					(x,y) = pos
				if event.button == 3: #Right mouse button
					screen.fill("White")              
        
		#Keyboard input managemant
		key_input = pygame.key.get_pressed()
		if key_input[pygame.K_w] : y -= speed
		if key_input[pygame.K_s] : y += speed
		if key_input[pygame.K_d] : x += speed
		if key_input[pygame.K_a] : x -= speed
		if key_input[pygame.K_c] : color_picker()
		if key_input[pygame.K_1] : pen_size = 1
		if key_input[pygame.K_2] : pen_size = 2
		if key_input[pygame.K_3] : pen_size = 3
		if key_input[pygame.K_4] : pen_size = 4
		if key_input[pygame.K_5] : pen_size = 5
		if key_input[pygame.K_6] : pen_size = 6
		if key_input[pygame.K_7] : pen_size = 7
		if key_input[pygame.K_8] : pen_size = 8
		if key_input[pygame.K_9] : pen_size = 9
        

		pygame.display.update()

