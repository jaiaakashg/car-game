#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time
import sys
from IPython.display import clear_output

class Car:
    def __init__(self, name, speed, lane):
        self.name = name
        self.speed = speed
        self.lane = lane
        self.position = 0
    
    def move(self):
        self.position += self.speed
    
    def display(self):
        return f"{' ' * (self.lane * 5)}{self.name}: {' ' * self.position}|{self.name}"

class Obstacle:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def display(self):
        return f"{' ' * self.position}|{self.name}"

def racing_game_advanced():
    print("Welcome to the Enhanced Text-Based Racing Game!")
    print("Use 'a' to move left, 'd' to move right. Press Enter to start the race!")
    input("Press Enter to start the race!")
    
    lanes = 3
    cars = [
        Car("Car 1", random.randint(2, 4), 0),
        Car("Car 2", random.randint(2, 4), 1),
        Car("Car 3", random.randint(2, 4), 2),
    ]
    
    obstacles = [
        Obstacle("Rock", random.randint(10, 30)),
        Obstacle("Puddle", random.randint(10, 30)),
        Obstacle("Tree", random.randint(10, 30)),
    ]
    
    winner = None
    while not winner:
        clear_output(wait=True)
        
        # Display track lanes and cars
        for car in cars:
            car.move()
            print(car.display())
        
        # Display obstacles
        for obstacle in obstacles:
            print(obstacle.display())
        
        # Check for collision with obstacles
        for car in cars:
            for obstacle in obstacles:
                if car.position == obstacle.position:
                    car.speed -= 1
                    print(f"{car.name} hit {obstacle.name}! Speed reduced.")
        
        # Check for winner
        for car in cars:
            if car.position >= 40:
                winner = car
                break
        
        if winner:
            break
        
        # User input for lane change
        try:
            user_input = input("Press 'a' to move left, 'd' to move right: ")
            if user_input.lower() == 'a':
                for car in cars:
                    if car.lane > 0:
                        car.lane -= 1
                        print(f"{car.name} moved left!")
                        time.sleep(0.5)
            elif user_input.lower() == 'd':
                for car in cars:
                    if car.lane < lanes - 1:
                        car.lane += 1
                        print(f"{car.name} moved right!")
                        time.sleep(0.5)
            else:
                print("Invalid input. Press 'a' to move left, 'd' to move right.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            sys.exit()
        
        time.sleep(0.5)
    
    print(f"\n{winner.name} wins the race!")

# Run the advanced racing game
racing_game_advanced()


# In[ ]:




