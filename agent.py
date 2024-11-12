# agent.py
import pygame

class Agent:
    def __init__(self, Environment, x=50, y=50, speed=5):
        self.Environment = Environment  # Reference to the Environment
        self.x = x                      # Initial x position
        self.y = y                      # Initial y position
        self.speed = speed              # Movement speed
    
    def move(self, direction):
        # Move agent based on the specified direction
        if direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed
        elif direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed

        # Ensure the agent stays within the environment boundaries
        self.Environment.limit_position(self)

    def get_position(self):
        return self.x, self.y
