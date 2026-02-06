import argparse


def get_figure_size(width=None, height=None):
    if width and height:
        return (width, height)
    else:
        return (DEFAULT_WIDTH, DEFAULT_HEIGHT)


def create_poster(width, height):
    figure_size = get_figure_size(width, height)
    # ... rest of the function


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a map poster.')
    parser.add_argument('--width', type=int, help='Specify the width of the poster.')
    parser.add_argument('--height', type=int, help='Specify the height of the poster.')
    args = parser.parse_args()

    create_poster(args.width, args.height)