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
            self.reset_selections()
            self.customer = Customer()  # New customer
        else:
            self.set_message(message)