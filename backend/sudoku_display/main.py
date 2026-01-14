from PIL import Image, ImageDraw, ImageFont
from typing import List


def solution_to_image(solution: List[str], filename: str = "sudoku.jpg", cell_size: int = 50) -> None:
    """Render a solved sudoku board (list of 9 strings) as a JPG image."""
    size = cell_size * 9
    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", cell_size // 2)
    except:
        font = ImageFont.load_default()

    # Draw numbers
    for i, row in enumerate(solution):
        for j, char in enumerate(row):
            x = j * cell_size + cell_size // 3
            y = i * cell_size + cell_size // 4
            draw.text((x, y), char, fill="black", font=font)

    # Draw grid lines
    for i in range(10):
        width = 3 if i % 3 == 0 else 1
        draw.line([(i * cell_size, 0), (i * cell_size, size)], fill="black", width=width)
        draw.line([(0, i * cell_size), (size, i * cell_size)], fill="black", width=width)

    img.save(filename, "JPEG")
    print(f"Saved to {filename}")
