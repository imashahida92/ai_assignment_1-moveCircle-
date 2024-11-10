# run.py
import pygame
from agent import Agent
from environment import Environment

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Agent-Environment Simulation")

# Set up environment and agent
environment = Environment(width, height)
agent = Agent(environment)

# Set up font for displaying position
font = pygame.font.Font(None, 36)

# Run the simulation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses and move the agent
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        agent.move('up')
    if keys[pygame.K_DOWN]:
        agent.move('down')
    if keys[pygame.K_LEFT]:
        agent.move('left')
    if keys[pygame.K_RIGHT]:
        agent.move('right')

    # Fill the background
    window.fill((0, 0, 0))

    # Draw the agent
    x, y = agent.get_position()
    pygame.draw.circle(window, (86, 200, 245), (x, y), 10)

    # Display the agent's position
    position_text = font.render(f"Position: ({x}, {y})", True, (255, 255, 255))
    window.blit(position_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
