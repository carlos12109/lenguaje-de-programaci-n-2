from tkinter import font

# Define color constants
PRIMARY_COLOR = "#4CAF50"  # Green
SECONDARY_COLOR = "#FFC107"  # Amber
BACKGROUND_COLOR = "#F5F5F5"  # Light Gray
TEXT_COLOR = "#212121"  # Dark Gray

# Define font styles
TITLE_FONT = ("Helvetica", 16, "bold")
BUTTON_FONT = ("Helvetica", 12)
LABEL_FONT = ("Helvetica", 12)

def apply_styles(widget):
    widget.config(bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    widget.option_add("*Font", LABEL_FONT)
    widget.option_add("*Button*Font", BUTTON_FONT)
    widget.option_add("*TButton*highlightBackground", PRIMARY_COLOR)
    widget.option_add("*TButton*highlightColor", PRIMARY_COLOR)