import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bow Factory")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)

# Fonts
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)

# Game variables
money = 0
customer_request = ""
selected_item = None
selected_pattern = None
selected_bg_color = None
selected_fg_color = None

# Items that can be made
items = ["bow", "dress", "skirt", "pants", "shirt", "sweater", "hat", "scarf", "gloves"]

# Patterns
patterns = ["plain", "striped", "dotted", "checkered", "flowery"]

# Colors
colors = ["red", "blue", "green", "yellow", "pink", "purple"]

# Create a new customer request
def new_customer_request():
    item = random.choice(items)
    pattern = random.choice(patterns)
    color = random.choice(colors)
    variations = ["", f"{pattern} ", f"{color} ", f"{color} and {random.choice(colors)} ", 
                 f"{pattern} {color} "]
    variation = random.choice(variations)
    return f"I want a {variation}{item}, please!"

# Customer request
customer_request = new_customer_request()

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.selected = False
    
    def draw(self):
        # Draw button
        if self.selected:
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, BLACK, self.rect, 3)  # Thicker border when selected
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, BLACK, self.rect, 1)
        
        # Draw text
        text_surface = small_font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create buttons
item_buttons = []
for i, item in enumerate(items):
    item_buttons.append(Button(50, 100 + i * 50, 150, 40, item, WHITE))

pattern_buttons = []
for i, pattern in enumerate(patterns):
    pattern_buttons.append(Button(250, 100 + i * 50, 150, 40, pattern, GRAY))

bg_color_buttons = []
for i, color_name in enumerate(colors):
    color_value = eval(color_name.upper())
    bg_color_buttons.append(Button(450, 100 + i * 50, 150, 40, f"BG: {color_name}", color_value))

fg_color_buttons = []
for i, color_name in enumerate(colors):
    color_value = eval(color_name.upper())
    fg_color_buttons.append(Button(620, 100 + i * 50, 150, 40, f"FG: {color_name}", color_value))

# Make button
make_button = Button(WIDTH // 2 - 75, HEIGHT - 100, 150, 50, "MAKE!", GREEN)

# Game loop
running = True
message = ""
message_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            # Check item buttons
            for button in item_buttons:
                if button.is_clicked(pos):
                    # Unselect all item buttons
                    for b in item_buttons:
                        b.selected = False
                    button.selected = True
                    selected_item = button.text
            
            # Check pattern buttons
            for button in pattern_buttons:
                if button.is_clicked(pos):
                    # Unselect all pattern buttons
                    for b in pattern_buttons:
                        b.selected = False
                    button.selected = True
                    selected_pattern = button.text
            
            # Check background color buttons
            for button in bg_color_buttons:
                if button.is_clicked(pos):
                    # Unselect all bg color buttons
                    for b in bg_color_buttons:
                        b.selected = False
                    button.selected = True
                    selected_bg_color = button.text.split(": ")[1]
            
            # Check foreground color buttons
            for button in fg_color_buttons:
                if button.is_clicked(pos):
                    # Unselect all fg color buttons
                    for b in fg_color_buttons:
                        b.selected = False
                    button.selected = True
                    selected_fg_color = button.text.split(": ")[1]
            
            # Check make button
            if make_button.is_clicked(pos):
                if selected_item:
                    # Check if made correctly
                    request_words = customer_request.lower().split()
                    correct = True
                    
                    # Check if the requested item is there
                    if selected_item not in request_words:
                        correct = False
                    
                    # Check if pattern is required and correct
                    if selected_pattern and selected_pattern in request_words:
                        pass  # Pattern is correct
                    elif any(pattern in request_words for pattern in patterns):
                        correct = False  # A pattern was requested but wrong one selected
                        
                    # Check if colors are required and correct
                    requested_colors = [color for color in colors if color in request_words]
                    if requested_colors:
                        if selected_bg_color not in requested_colors and selected_fg_color not in requested_colors:
                            correct = False
                    
                    if correct:
                        money += 10
                        message = "Good job! You earned $10!"
                        # Reset selections
                        selected_item = None
                        selected_pattern = None
                        selected_bg_color = None
                        selected_fg_color = None
                        for b in item_buttons + pattern_buttons + bg_color_buttons + fg_color_buttons:
                            b.selected = False
                        # New customer
                        customer_request = new_customer_request()
                    else:
                        message = "That's not what I wanted!"
                    
                    message_timer = 180  # Show message for 3 seconds (60 fps * 3)
                else:
                    message = "You need to select an item!"
                    message_timer = 180
    
    # Drawing
    screen.fill(WHITE)
    
    # Draw title
    title_text = font.render("Bow Factory", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 20))
    
    # Draw money
    money_text = font.render(f"Money: ${money}", True, GREEN)
    screen.blit(money_text, (50, 20))
    
    # Draw customer request
    request_box = pygame.Rect(400, 20, 350, 60)
    pygame.draw.rect(screen, GRAY, request_box)
    pygame.draw.rect(screen, BLACK, request_box, 2)
    
    # Wrap text if too long
    if len(customer_request) > 30:
        request_lines = [customer_request[:30], customer_request[30:]]
        screen.blit(small_font.render(request_lines[0], True, BLACK), (request_box.x + 10, request_box.y + 10))
        screen.blit(small_font.render(request_lines[1], True, BLACK), (request_box.x + 10, request_box.y + 35))
    else:
        screen.blit(small_font.render(customer_request, True, BLACK), (request_box.x + 10, request_box.y + 20))
    
    # Draw section labels
    screen.blit(font.render("Items", True, BLACK), (50, 70))
    screen.blit(font.render("Patterns", True, BLACK), (250, 70))
    screen.blit(font.render("Colors", True, BLACK), (450, 70))
    
    # Draw buttons
    for button in item_buttons + pattern_buttons + bg_color_buttons + fg_color_buttons:
        button.draw()
    
    make_button.draw()
    
    # Draw message
    if message_timer > 0:
        message_text = font.render(message, True, BLACK)
        message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT - 150))
        screen.blit(message_text, message_rect)
        message_timer -= 1
    
    # Draw preview of creation
    preview_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 50, 100, 100)
    
    if selected_bg_color:
        bg_color = eval(selected_bg_color.upper())
        pygame.draw.rect(screen, bg_color, preview_rect)
    else:
        pygame.draw.rect(screen, WHITE, preview_rect)
    
    pygame.draw.rect(screen, BLACK, preview_rect, 2)
    
    if selected_item:
        item_text = font.render(selected_item, True, BLACK)
        screen.blit(item_text, (preview_rect.centerx - item_text.get_width() // 2, 
                               preview_rect.bottom + 10))
    
    if selected_pattern and selected_pattern != "plain":
        if selected_pattern == "striped":
            for i in range(0, 100, 10):
                pygame.draw.line(screen, BLACK, 
                                (preview_rect.left, preview_rect.top + i),
                                (preview_rect.right, preview_rect.top + i), 2)
        elif selected_pattern == "dotted":
            for x in range(preview_rect.left + 10, preview_rect.right, 20):
                for y in range(preview_rect.top + 10, preview_rect.bottom, 20):
                    pygame.draw.circle(screen, BLACK, (x, y), 5)
        elif selected_pattern == "checkered":
            for x in range(0, 100, 20):
                for y in range(0, 100, 20):
                    if (x // 20 + y // 20) % 2 == 0:
                        pygame.draw.rect(screen, BLACK, 
                                        (preview_rect.left + x, preview_rect.top + y, 20, 20))
        elif selected_pattern == "flowery":
            for x in range(preview_rect.left + 15, preview_rect.right, 30):
                for y in range(preview_rect.top + 15, preview_rect.bottom, 30):
                    pygame.draw.circle(screen, YELLOW, (x, y), 10)
                    for angle in range(0, 360, 60):
                        angle_rad = angle * 3.14159 / 180
                        end_x = x + 12 * pygame.math.Vector2(1, 0).rotate(angle).x
                        end_y = y + 12 * pygame.math.Vector2(1, 0).rotate(angle).y
                        pygame.draw.line(screen, YELLOW, (x, y), (end_x, end_y), 3)
    
    if selected_fg_color:
        fg_color = eval(selected_fg_color.upper())
        if selected_item == "bow":
            # Draw a simple bow
            pygame.draw.rect(screen, fg_color, (preview_rect.centerx - 40, preview_rect.centery - 10, 80, 20))
            pygame.draw.rect(screen, fg_color, (preview_rect.centerx - 10, preview_rect.centery - 40, 20, 80))
        # Add simple drawings for other items here
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()