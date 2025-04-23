import pygame
import math
from constants import *

def draw_preview(screen, preview_rect, selected_item, selected_pattern, selected_bg_color, selected_fg_color):
    """Draw a preview of the current creation"""
    # Draw background
    if selected_bg_color:
        bg_color = globals()[selected_bg_color.upper()]
        pygame.draw.rect(screen, bg_color, preview_rect)
    else:
        pygame.draw.rect(screen, WHITE, preview_rect)
    
    # Draw border
    pygame.draw.rect(screen, BLACK, preview_rect, 2)
    
    # Draw foreground elements based on selected item
    if selected_fg_color:
        fg_color = globals()[selected_fg_color.upper()]
        draw_item(screen, preview_rect, selected_item, fg_color)
    
    # Draw pattern on top (pattern uses the foreground color if selected)
    pattern_color = BLACK
    if selected_fg_color:
        pattern_color = globals()[selected_fg_color.upper()]
        
    if selected_pattern and selected_pattern != "plain":
        draw_pattern(screen, preview_rect, selected_pattern, pattern_color)
    
    # Draw item name below
    if selected_item:
        item_text = pygame.font.SysFont(None, 36).render(selected_item, True, BLACK)
        screen.blit(item_text, (preview_rect.centerx - item_text.get_width() // 2, 
                               preview_rect.bottom + 10))

def draw_item(screen, rect, item_name, color):
    """Draw the selected item"""
    if item_name == "bow":
        # Draw a simple bow
        pygame.draw.rect(screen, color, (rect.centerx - 40, rect.centery - 10, 80, 20))
        pygame.draw.rect(screen, color, (rect.centerx - 10, rect.centery - 40, 20, 80))
    elif item_name == "dress":
        # Draw a simple dress
        # Triangle for skirt part
        points = [(rect.centerx, rect.top + 20), 
                  (rect.centerx - 30, rect.bottom - 10),
                  (rect.centerx + 30, rect.bottom - 10)]
        pygame.draw.polygon(screen, color, points)
        # Rectangle for top part
        pygame.draw.rect(screen, color, (rect.centerx - 20, rect.top + 20, 40, 30))
    elif item_name == "pants":
        # Draw simple pants
        pygame.draw.rect(screen, color, (rect.centerx - 30, rect.top + 20, 20, 70))
        pygame.draw.rect(screen, color, (rect.centerx + 10, rect.top + 20, 20, 70))
        pygame.draw.rect(screen, color, (rect.centerx - 30, rect.top + 20, 60, 20))
    elif item_name == "skirt":
        # Draw a simple skirt
        pygame.draw.polygon(screen, color, [
            (rect.centerx - 30, rect.top + 20),
            (rect.centerx + 30, rect.top + 20),
            (rect.centerx + 40, rect.bottom - 10),
            (rect.centerx - 40, rect.bottom - 10)
        ])
    elif item_name == "shirt":
        # Draw a simple shirt
        pygame.draw.rect(screen, color, (rect.centerx - 30, rect.top + 20, 60, 60))
        pygame.draw.rect(screen, color, (rect.centerx - 30, rect.top + 20, 15, 70))
        pygame.draw.rect(screen, color, (rect.centerx + 15, rect.top + 20, 15, 70))
    elif item_name == "sweater":
        # Draw a simple sweater (similar to shirt but thicker)
        pygame.draw.rect(screen, color, (rect.centerx - 35, rect.top + 15, 70, 65))
        pygame.draw.rect(screen, color, (rect.centerx - 35, rect.top + 15, 20, 75))
        pygame.draw.rect(screen, color, (rect.centerx + 15, rect.top + 15, 20, 75))
    elif item_name == "hat":
        # Draw a simple hat
        pygame.draw.ellipse(screen, color, (rect.centerx - 30, rect.centery, 60, 30))
        pygame.draw.rect(screen, color, (rect.centerx - 20, rect.centery - 30, 40, 30))
    elif item_name == "scarf":
        # Draw a simple scarf
        pygame.draw.rect(screen, color, (rect.centerx - 40, rect.centery - 10, 80, 20))
        pygame.draw.rect(screen, color, (rect.centerx - 10, rect.centery - 10, 20, 50))
    elif item_name == "gloves":
        # Draw simple gloves
        pygame.draw.rect(screen, color, (rect.centerx - 30, rect.centery - 10, 20, 40))
        pygame.draw.rect(screen, color, (rect.centerx + 10, rect.centery - 10, 20, 40))
        pygame.draw.circle(screen, color, (rect.centerx - 20, rect.centery - 20), 10)
        pygame.draw.circle(screen, color, (rect.centerx + 20, rect.centery - 20), 10)

def draw_pattern(screen, rect, pattern_name, color):
    """Draw the selected pattern on top of the item"""
    if pattern_name == "striped":
        for i in range(0, rect.height, 10):
            pygame.draw.line(screen, color, 
                            (rect.left, rect.top + i),
                            (rect.right, rect.top + i), 2)
    elif pattern_name == "dotted":
        for x in range(rect.left + 10, rect.right, 20):
            for y in range(rect.top + 10, rect.bottom, 20):
                pygame.draw.circle(screen, color, (x, y), 5)
    elif pattern_name == "checkered":
        for x in range(0, rect.width, 20):
            for y in range(0, rect.height, 20):
                if (x // 20 + y // 20) % 2 == 0:
                    pygame.draw.rect(screen, color, 
                                    (rect.left + x, rect.top + y, 20, 20))
    elif pattern_name == "flowery":
        for x in range(rect.left + 15, rect.right, 30):
            for y in range(rect.top + 15, rect.bottom, 30):
                pygame.draw.circle(screen, color, (x, y), 10)
                for angle in range(0, 360, 60):
                    angle_rad = angle * math.pi / 180
                    end_x = x + 12 * math.cos(angle_rad)
                    end_y = y + 12 * math.sin(angle_rad)
                    pygame.draw.line(screen, color, (x, y), (end_x, end_y), 3)