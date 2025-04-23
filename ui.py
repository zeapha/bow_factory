import pygame
from constants import *

# Initialize pygame font
pygame.font.init()
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)

class Button:
    def __init__(self, x, y, width, height, text, color, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.selected = False
    
    def draw(self, screen):
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

def create_buttons():
    """Create all game buttons"""
    item_buttons = []
    for i, item in enumerate(ITEMS):
        item_buttons.append(Button(50, 100 + i * 50, ITEM_BUTTON_WIDTH, BUTTON_HEIGHT, item, WHITE))

    pattern_buttons = []
    for i, pattern in enumerate(PATTERNS):
        pattern_buttons.append(Button(250, 100 + i * 50, ITEM_BUTTON_WIDTH, BUTTON_HEIGHT, pattern, GRAY))

    bg_color_buttons = []
    for i, color_name in enumerate(COLORS):
        color_value = globals()[color_name.upper()]
        bg_color_buttons.append(Button(450, 100 + i * 50, ITEM_BUTTON_WIDTH, BUTTON_HEIGHT, f"BG: {color_name}", color_value))

    fg_color_buttons = []
    for i, color_name in enumerate(COLORS):
        color_value = globals()[color_name.upper()]
        fg_color_buttons.append(Button(620, 100 + i * 50, ITEM_BUTTON_WIDTH, BUTTON_HEIGHT, f"FG: {color_name}", color_value))

    # Make button
    make_button = Button(WIDTH // 2 - 75, HEIGHT - 100, 150, 50, "MAKE!", GREEN)
    
    return item_buttons, pattern_buttons, bg_color_buttons, fg_color_buttons, make_button

def draw_message(screen, message, timer):
    """Draw a temporary message on screen"""
    if timer > 0:
        message_text = font.render(message, True, BLACK)
        message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT - 150))
        screen.blit(message_text, message_rect)

def draw_money(screen, money):
    """Draw the money display"""
    money_text = font.render(f"Money: ${money}", True, GREEN)
    screen.blit(money_text, (50, 20))

def draw_title(screen):
    """Draw the game title"""
    title_text = font.render("Bow Factory", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 20))

def draw_customer_request(screen, request):
    """Draw the customer request box"""
    request_box = pygame.Rect(400, 20, 350, 60)
    pygame.draw.rect(screen, GRAY, request_box)
    pygame.draw.rect(screen, BLACK, request_box, 2)
    
    # Wrap text if too long
    if len(request) > 30:
        request_lines = [request[:30], request[30:]]
        screen.blit(small_font.render(request_lines[0], True, BLACK), (request_box.x + 10, request_box.y + 10))
        screen.blit(small_font.render(request_lines[1], True, BLACK), (request_box.x + 10, request_box.y + 35))
    else:
        screen.blit(small_font.render(request, True, BLACK), (request_box.x + 10, request_box.y + 20))

def draw_section_labels(screen):
    """Draw the section labels"""
    screen.blit(font.render("Items", True, BLACK), (50, 70))
    screen.blit(font.render("Patterns", True, BLACK), (250, 70))
    screen.blit(font.render("Colors", True, BLACK), (450, 70))