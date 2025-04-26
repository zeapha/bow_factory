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
    
    # Draw item shape if selected
    if selected_item:
        # Draw foreground elements based on selected item
        if selected_fg_color:
            fg_color = globals()[selected_fg_color.upper()]
            draw_item(screen, preview_rect, selected_item, fg_color)
        else:
            # Use a default color if no fg_color is selected
            draw_item(screen, preview_rect, selected_item, BLACK)
    
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

def draw_created_item(screen, rect, item_name, pattern_name, bg_color_name, fg_color_name):
    """Draw a created item at the given rect position (similar to preview but for finished items)"""
    # Draw background
    if bg_color_name:
        bg_color = globals()[bg_color_name.upper()]
        pygame.draw.rect(screen, bg_color, rect)
    else:
        pygame.draw.rect(screen, WHITE, rect)
    
    # Draw border
    pygame.draw.rect(screen, BLACK, rect, 2)
    
    # Draw item shape
    if item_name:
        # Draw foreground elements based on item
        if fg_color_name:
            fg_color = globals()[fg_color_name.upper()]
            draw_item(screen, rect, item_name, fg_color)
        else:
            # Use a default color if no fg_color is selected
            draw_item(screen, rect, item_name, BLACK)
    
    # Draw pattern on top
    pattern_color = BLACK
    if fg_color_name:
        pattern_color = globals()[fg_color_name.upper()]
        
    if pattern_name and pattern_name != "plain":
        draw_pattern(screen, rect, pattern_name, pattern_color)
    
    # Draw item name below
    if item_name:
        item_text = pygame.font.SysFont(None, 36).render(item_name, True, BLACK)
        screen.blit(item_text, (rect.centerx - item_text.get_width() // 2, 
                               rect.bottom + 10))

def draw_item(screen, rect, item_name, color):
    """Draw the selected item"""
    if item_name == "bow":
        # Draw a better looking bow
        # Center circle
        pygame.draw.circle(screen, color, (rect.centerx, rect.centery), 10)
        # Left loop
        pygame.draw.ellipse(screen, color, (rect.centerx - 40, rect.centery - 20, 30, 40), 3)
        # Right loop
        pygame.draw.ellipse(screen, color, (rect.centerx + 10, rect.centery - 20, 30, 40), 3)
        # Ribbons
        pygame.draw.polygon(screen, color, [
            (rect.centerx, rect.centery + 10),
            (rect.centerx - 15, rect.bottom - 10),
            (rect.centerx - 5, rect.bottom - 10)
        ])
        pygame.draw.polygon(screen, color, [
            (rect.centerx, rect.centery + 10),
            (rect.centerx + 15, rect.bottom - 10),
            (rect.centerx + 5, rect.bottom - 10)
        ])
    elif item_name == "dress":
        # Draw a better dress
        # Triangle for skirt part
        points = [(rect.centerx, rect.top + 30), 
                  (rect.centerx - 40, rect.bottom - 5),
                  (rect.centerx + 40, rect.bottom - 5)]
        pygame.draw.polygon(screen, color, points)
        # Top part
        pygame.draw.rect(screen, color, (rect.centerx - 20, rect.top + 10, 40, 25))
        # Sleeves
        pygame.draw.ellipse(screen, color, (rect.centerx - 35, rect.top + 15, 20, 10))
        pygame.draw.ellipse(screen, color, (rect.centerx + 15, rect.top + 15, 20, 10))
    elif item_name == "pants":
        # Draw better looking pants
        # Waistband
        pygame.draw.rect(screen, color, (rect.centerx - 30, rect.top + 10, 60, 15))
        # Left leg
        pygame.draw.rect(screen, color, (rect.centerx - 30, rect.top + 25, 25, 65))
        # Right leg
        pygame.draw.rect(screen, color, (rect.centerx + 5, rect.top + 25, 25, 65))
    elif item_name == "skirt":
        # Draw a better skirt
        # Waistband
        pygame.draw.rect(screen, color, (rect.centerx - 30, rect.top + 10, 60, 15))
        # Skirt part - pleated look
        for i in range(-30, 31, 10):
            pygame.draw.polygon(screen, color, [
                (rect.centerx + i, rect.top + 25),
                (rect.centerx + i - 5, rect.bottom - 5),
                (rect.centerx + i + 5, rect.bottom - 5)
            ])
    elif item_name == "shirt":
        # Draw a better shirt
        # Main body
        pygame.draw.rect(screen, color, (rect.centerx - 30, rect.top + 20, 60, 50))
        # Collar
        pygame.draw.polygon(screen, color, [
            (rect.centerx - 15, rect.top + 20),
            (rect.centerx, rect.top + 10),
            (rect.centerx + 15, rect.top + 20)
        ])
        # Left sleeve
        pygame.draw.ellipse(screen, color, (rect.centerx - 45, rect.top + 25, 20, 15))
        # Right sleeve
        pygame.draw.ellipse(screen, color, (rect.centerx + 25, rect.top + 25, 20, 15))
    elif item_name == "sweater":
        # Draw a better sweater
        # Main body (thicker than shirt)
        pygame.draw.rect(screen, color, (rect.centerx - 35, rect.top + 15, 70, 60))
        # Collar - round neck
        pygame.draw.ellipse(screen, WHITE, (rect.centerx - 20, rect.top + 10, 40, 20))
        # Left sleeve (thicker)
        pygame.draw.rect(screen, color, (rect.centerx - 35, rect.top + 20, 15, 40))
        pygame.draw.ellipse(screen, color, (rect.centerx - 45, rect.top + 30, 25, 20))
        # Right sleeve (thicker)
        pygame.draw.rect(screen, color, (rect.centerx + 20, rect.top + 20, 15, 40))
        pygame.draw.ellipse(screen, color, (rect.centerx + 20, rect.top + 30, 25, 20))
    elif item_name == "hat":
        # Draw a better hat
        # Brim
        pygame.draw.ellipse(screen, color, (rect.centerx - 35, rect.centery + 10, 70, 20))
        # Top part
        pygame.draw.rect(screen, color, (rect.centerx - 25, rect.top + 20, 50, 40))
        pygame.draw.ellipse(screen, color, (rect.centerx - 25, rect.top + 15, 50, 15))
    elif item_name == "scarf":
        # Draw a better scarf
        # Main part
        pygame.draw.rect(screen, color, (rect.centerx - 40, rect.centery - 10, 80, 20))
        # Hanging part
        pygame.draw.rect(screen, color, (rect.centerx - 10, rect.centery - 10, 20, 60))
        # Fringe on ends
        for i in range(-40, -20, 5):
            pygame.draw.line(screen, color, 
                            (rect.centerx + i, rect.centery + 10),
                            (rect.centerx + i, rect.centery + 20), 2)
        for i in range(20, 41, 5):
            pygame.draw.line(screen, color, 
                            (rect.centerx + i, rect.centery + 10),
                            (rect.centerx + i, rect.centery + 20), 2)
    elif item_name == "gloves":
        # Draw better gloves
        # Left glove
        pygame.draw.rect(screen, color, (rect.centerx - 35, rect.centery - 10, 25, 45))
        # Left fingers
        for i in range(-30, -10, 5):
            pygame.draw.line(screen, color, 
                            (rect.centerx + i, rect.centery - 10),
                            (rect.centerx + i, rect.centery - 25), 3)
        # Right glove
        pygame.draw.rect(screen, color, (rect.centerx + 10, rect.centery - 10, 25, 45))
        # Right fingers
        for i in range(15, 36, 5):
            pygame.draw.line(screen, color, 
                            (rect.centerx + i, rect.centery - 10),
                            (rect.centerx + i, rect.centery - 25), 3)

def draw_pattern(screen, rect, pattern_name, color):
    """Draw the selected pattern on top of the item"""
    if pattern_name == "striped":
        for i in range(0, rect.height, 10):
            pygame.draw.line(screen, color, 
                            (rect.left, rect.top + i),
                            (rect.right, rect.top + i), 2)
    elif pattern_name == "dotted":
        for x in range(rect.left + 10, rect.right, 15):
            for y in range(rect.top + 10, rect.bottom, 15):
                pygame.draw.circle(screen, color, (x, y), 3)
    elif pattern_name == "checkered":
        for x in range(0, rect.width, 20):
            for y in range(0, rect.height, 20):
                if (x // 20 + y // 20) % 2 == 0:
                    pygame.draw.rect(screen, color, 
                                    (rect.left + x, rect.top + y, 20, 20))
    elif pattern_name == "flowery":
        for x in range(rect.left + 20, rect.right, 30):
            for y in range(rect.top + 20, rect.bottom, 30):
                # Center
                pygame.draw.circle(screen, color, (x, y), 5)
                # Petals
                for angle in range(0, 360, 60):
                    angle_rad = angle * math.pi / 180
                    end_x = x + 10 * math.cos(angle_rad)
                    end_y = y + 10 * math.sin(angle_rad)
                    pygame.draw.circle(screen, color, (end_x, end_y), 3)