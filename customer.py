import random
from constants import ITEMS, PATTERNS, COLORS

class Customer:
    def __init__(self):
        self.request = ""
        self.requested_item = ""
        self.requested_pattern = ""
        self.requested_colors = []
        self.generate_request()
    
    def generate_request(self):
        """Generate a new customer request and parse its components"""
        self.requested_item = random.choice(ITEMS)
        self.requested_pattern = random.choice(PATTERNS)
        
        # Choose 1 or 2 colors
        if random.random() < 0.3:  # 30% chance for two colors
            color1 = random.choice(COLORS)
            color2 = random.choice([c for c in COLORS if c != color1])
            self.requested_colors = [color1, color2]
            color_text = f"{color1} and {color2} "
        elif random.random() < 0.7:  # 70% chance of the remaining 70% for one color
            color1 = random.choice(COLORS)
            self.requested_colors = [color1]
            color_text = f"{color1} "
        else:  # No color specified
            self.requested_colors = []
            color_text = ""
        
        # Randomly decide whether to mention pattern
        if self.requested_pattern != "plain" and random.random() < 0.8:
            pattern_text = f"{self.requested_pattern} "
        else:
            self.requested_pattern = ""
            pattern_text = ""
        
        # Build the final request
        self.request = f"I want a {pattern_text}{color_text}{self.requested_item}, please!"
        return self.request
    
    def check_creation(self, selected_item, selected_pattern, selected_bg_color, selected_fg_color):
        """
        Check if the player's creation matches the request
        
        Returns:
            bool: True if correct, False otherwise
            str: Feedback message
        """
        # Check if selected item matches requested item
        if selected_item != self.requested_item:
            return False, f"Wrong item! I wanted a {self.requested_item}."
        
        # Check pattern
        if self.requested_pattern and selected_pattern != self.requested_pattern:
            return False, f"Wrong pattern! I wanted a {self.requested_pattern} pattern."
        
        # Check colors
        if self.requested_colors:
            selected_colors = [c for c in [selected_bg_color, selected_fg_color] if c]
            
            # Check if at least one of the requested colors is used
            if not any(color in selected_colors for color in self.requested_colors):
                colors_text = " and ".join(self.requested_colors)
                return False, f"Wrong color! I wanted {colors_text}."
        
        return True, "Good job! You earned $10!"