import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Example")

# Set up the clock
clock = pygame.time.Clock()

# Set up the circle
circle_pos = [0, height // 2]
circle_radius = 25
circle_color = (255, 0, 0)

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Move the circle
    circle_pos[0] += 5
    if circle_pos[0] > width:
        circle_pos[0] = -circle_radius

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the circle
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
