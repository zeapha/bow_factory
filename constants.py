import pygame
# Constants for the Bow Factory game

# Display settings
WIDTH, HEIGHT = 800, 600
TITLE = "Bow Factory"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)
DARK_GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)

# Game settings
STARTING_MONEY = 0
MESSAGE_DURATION = 180  # frames (3 seconds at 60 fps)

# Lists for game options
ITEMS = ["bow", "dress", "skirt", "pants", "shirt", "sweater", "hat", "scarf", "gloves"]
PATTERNS = ["plain", "striped", "dotted", "checkered", "flowery"]
COLORS = ["red", "blue", "green", "yellow", "pink", "purple"]

# UI settings
BUTTON_HEIGHT = 40
ITEM_BUTTON_WIDTH = 150
SECTION_SPACING = 200

# Machine settings
MACHINE_RECT = pygame.Rect(0, 250, 200, 250)  # Left side machine