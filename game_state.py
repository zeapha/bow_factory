from constants import STARTING_MONEY, MESSAGE_DURATION
from customer import Customer

class GameState:
    def __init__(self):
        self.money = STARTING_MONEY
        self.customer = Customer()
        self.selected_item = None
        self.selected_pattern = None
        self.selected_bg_color = None
        self.selected_fg_color = None
        self.message = ""
        self.message_timer = 0
        # Add variables for item animation
        self.created_item = None
        self.item_position = (-150, 300)  # Start offscreen to the left
        self.item_target_position = (650, 300)  # Final position on the right side
        self.item_moving = False
        self.item_speed = 5
    
    def reset_selections(self):
        """Reset all item selections"""
        self.selected_item = None
        self.selected_pattern = None
        self.selected_bg_color = None
        self.selected_fg_color = None
    
    def set_message(self, message):
        """Set a temporary message"""
        self.message = message
        self.message_timer = MESSAGE_DURATION
    
    def update_message_timer(self):
        """Update the message timer"""
        if self.message_timer > 0:
            self.message_timer -= 1
    
    def update_item_animation(self):
        """Update the animation of the created item"""
        if self.item_moving:
            # Move the item towards the target position
            x, y = self.item_position
            target_x, target_y = self.item_target_position
            
            # Calculate new position
            if x < target_x:
                x += self.item_speed
                if x >= target_x:
                    x = target_x
                    self.item_moving = False
            
            self.item_position = (x, y)
    
    def handle_make_request(self):
        """Handle when player clicks the 'Make' button"""
        if not self.selected_item:
            self.set_message("You need to select an item!")
            return
        
        # Check if the creation is correct
        correct, message = self.customer.check_creation(
            self.selected_item,
            self.selected_pattern,
            self.selected_bg_color,
            self.selected_fg_color
        )
        
        if correct:
            self.money += 10
            self.set_message(message)
            
            # Save the created item before resetting selections
            self.created_item = {
                'item': self.selected_item,
                'pattern': self.selected_pattern,
                'bg_color': self.selected_bg_color,
                'fg_color': self.selected_fg_color
            }
            
            # Start animation
            self.item_position = (-150, 300)  # Start offscreen
            self.item_moving = True
            
            self.reset_selections()
            self.customer = Customer()  # New customer
        else:
            self.set_message(message)