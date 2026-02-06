# Updated create_map_poster.py

# Add custom width and height parameters for poster dimensions

def create_map_poster(width=None, height=None):
    # Check if the width and height are provided;
    # If not, set to default values.
    if width is None:
        width = 24  # default width
    if height is None:
        height = 36  # default height

    # Create poster logic here using width and height...
    print(f"Creating poster with dimensions: {width} x {height}")

# Example usage
if __name__ == '__main__':
    create_map_poster()  # Use default dimensions
    create_map_poster(width=30, height=40)  # Use custom dimensions