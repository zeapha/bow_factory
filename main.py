import pygame
import sys
from constants import *
from ui import *
from items import draw_preview, draw_created_item
from game_state import GameState

def main():
    # Initialize pygame
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    
    # Create buttons
    item_buttons, pattern_buttons, bg_color_buttons, fg_color_buttons, make_button = create_buttons()
    
    # Create game state
    game_state = GameState()
    
    # Create preview rectangle (now moved to the right of the machine)
    preview_rect = pygame.Rect(300, HEIGHT // 2 - 50, 100, 100)
    
    # Game loop
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # Event handling
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
                        game_state.selected_item = button.text
                
                # Check pattern buttons
                for button in pattern_buttons:
                    if button.is_clicked(pos):
                        # Unselect all pattern buttons
                        for b in pattern_buttons:
                            b.selected = False
                        button.selected = True
                        game_state.selected_pattern = button.text
                
                # Check background color buttons
                for button in bg_color_buttons:
                    if button.is_clicked(pos):
                        # Unselect all bg color buttons
                        for b in bg_color_buttons:
                            b.selected = False
                        button.selected = True
                        game_state.selected_bg_color = button.text.split(": ")[1]
                
                # Check foreground color buttons
                for button in fg_color_buttons:
                    if button.is_clicked(pos):
                        # Unselect all fg color buttons
                        for b in fg_color_buttons:
                            b.selected = False
                        button.selected = True
                        game_state.selected_fg_color = button.text.split(": ")[1]
                
                # Check make button
                if make_button.is_clicked(pos):
                    game_state.handle_make_request()
                    
                    # Update button selections after checking the request
                    for button_list in [item_buttons, pattern_buttons, bg_color_buttons, fg_color_buttons]:
                        for button in button_list:
                            button.selected = False
        
        # Update game state
        game_state.update_message_timer()
        game_state.update_item_animation()  # Update the item animation
        
        # Drawing
        screen.fill(WHITE)
        
        # Draw UI elements
        draw_title(screen)
        draw_money(screen, game_state.money)
        draw_customer_request(screen, game_state.customer.request)
        draw_section_labels(screen)
        
        # Draw the machine
        draw_machine(screen)
        
        # Draw all buttons
        for button in item_buttons + pattern_buttons + bg_color_buttons + fg_color_buttons:
            button.draw(screen)
        make_button.draw(screen)
        
        # Draw message
        draw_message(screen, game_state.message, game_state.message_timer)
        
        # Draw preview
        draw_preview(
            screen,
            preview_rect,
            game_state.selected_item,
            game_state.selected_pattern,
            game_state.selected_bg_color,
            game_state.selected_fg_color
        )
        
        # Draw created item if it exists and is moving
        if game_state.created_item:
            item_rect = pygame.Rect(
                game_state.item_position[0] - 50,
                game_state.item_position[1] - 50,
                100, 100
            )
            draw_created_item(
                screen,
                item_rect,
                game_state.created_item['item'],
                game_state.created_item['pattern'],
                game_state.created_item['bg_color'],
                game_state.created_item['fg_color']
            )
        
        # Draw a conveyor belt between the machine and the creation
        if game_state.item_moving:
            # Draw conveyor belt
            conveyor_rect = pygame.Rect(MACHINE_RECT.right, MACHINE_RECT.centery - 10, 
                                     500, 20)
            pygame.draw.rect(screen, DARK_GRAY, conveyor_rect)
            
            # Draw rollers
            for x in range(MACHINE_RECT.right + 10, 710, 30):
                pygame.draw.rect(screen, BLACK, 
                              (x, MACHINE_RECT.centery - 5, 20, 10))
        
        # Update display
        pygame.display.flip()
        
        # Cap the framerate
        clock.tick(60)
    
    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()