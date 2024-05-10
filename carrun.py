import pygame
from pygame.locals import *
import random
import tkinter as tk
from tkinter import messagebox
import sys

def show_game_over():
    # Create a simple pop-up dialog using tkinter
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.geometry("500x500")
    messagebox.showinfo("Game Over", "You Lost!")

# Initialize Pygame
pygame.init()

size = width, height = (600, 600)
road_width = int(width / 1.6)
roadmark_width = int(width / 80)
right_lane = width / 2 + road_width / 4
left_lane = width / 2 - road_width / 4
speed = 1

# Create the game window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("New Car_Run")
screen.fill((60, 179, 113))
pygame.display.update()

# Load images
car = pygame.image.load("C-car1.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.85

car2 = pygame.image.load("S-car1.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.185

car3 = pygame.image.load("S-car2.png")
car3_loc = car3.get_rect()
car3_loc.center = left_lane, height * 0.185

car4 = pygame.image.load("S-car3.png")
car4_loc = car4.get_rect()
car4_loc.center = left_lane, height * 0.185

car5 = pygame.image.load("S-car4.png")
car5_loc = car5.get_rect()
car5_loc.center = left_lane, height * 0.185

counter = 0
running = True

# Game loop
while running:
    counter += 1
    if counter == 2000:
        speed += 0.05
        counter = 0
        print("LEVEL UP")

    car2_loc[1] += speed
    if car2_loc[1] > height:
        car2_loc[1] = -180
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -180
        else:
            car2_loc.center = left_lane, -180

    car3_loc[1] += speed
    if car3_loc[1] > height:
    	car3_loc[1] = -180
    	if random.randint(0, 1) == 0:
    		car3_loc.center = right_lane, -180
    	else:
            car3_loc.center = left_lane, -180

    car4_loc[1] += speed
    if car4_loc[1] > height:
    	car4_loc[1] = -180
    	if random.randint(0, 1) == 0:
    		car4_loc.center = right_lane, -180
    	else:
            car4_loc.center = left_lane, -180

    car5_loc[1] += speed
    if car5_loc[1] > height:
    	car5_loc[1] = -180
    	if random.randint(0, 1) == 0:
    		car5_loc.center = right_lane, -180
    	else:
            car5_loc.center = left_lane, -180

    # End game
    if (car_loc[0]==car2_loc[0] and car2_loc[1]>car_loc[1] - 100):
        print("GAME OVER!")
        print("YOU LOST!")
        show_game_over()
        pygame.quit()
        sys.exit()
    elif (car_loc[0]==car3_loc[0] and car3_loc[1]>car_loc[1] - 100):
        print("GAME OVER!")
        print("YOU LOST!")
        show_game_over()
        pygame.quit()
        sys.exit()
    elif (car_loc[0]==car4_loc[0] and car4_loc[1]>car_loc[1] - 100):
        print("GAME OVER!")
        print("YOU LOST!")
        show_game_over()
        pygame.quit()
        sys.exit()
    elif (car_loc[0]==car5_loc[0] and car5_loc[1]>car_loc[1] - 100):
        print("GAME OVER!")
        print("YOU LOST!")
        show_game_over()
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_width / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_width / 2), 0])

    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_width / 2, 0, road_width, height))
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - roadmark_width / 2, 0, roadmark_width, height))
    
    # Draw dashed line
    dash_length = 20  # Adjust the length of each dash
    gap_length = 5   # Adjust the length of each gap
    num_dashes = height // (dash_length + gap_length)
    for i in range(num_dashes):
        dash_y = i * (dash_length + gap_length)
        pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_width / 3.5 - roadmark_width * 3, dash_y, roadmark_width, dash_length))

    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_width / 2 + roadmark_width * 2, 0, roadmark_width, height))
 
    # Draw dashed line
    dash_length = 20  # Adjust the length of each dash
    gap_length = 5   # Adjust the length of each gap
    num_dashes = height // (dash_length + gap_length)
    for i in range(num_dashes):
        dash_y = i * (dash_length + gap_length)
        pygame.draw.rect(screen, (255, 255, 255), (width / 4 + road_width / 4.5 - roadmark_width * 4, dash_y, roadmark_width, dash_length))

    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_width / 2 - roadmark_width * 3, 0, roadmark_width, height))

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    screen.blit(car3, car3_loc)
    screen.blit(car4, car4_loc)
    screen.blit(car5, car5_loc)
    pygame.display.update()

# Close the game loop
pygame.quit()
sys.exit()

