def make_grid(width, height):
    """
    Creates a gris that will hold all of the tiles for a boggle game
    """
    return{(row, col): ' ' for row in range(height)
        for col in range(width)}
