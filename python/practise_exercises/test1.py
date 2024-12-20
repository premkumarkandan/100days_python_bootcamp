from PIL import Image, ImageDraw, ImageFont


def create_practice_page(letters, page_number):
    # Define canvas size (A4 size in pixels)
    width, height = 1240, 1754  # Approx for A4
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Font settings
    try:
        font_dashed = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 60)
        font_regular = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
    except IOError:
        font_dashed = ImageFont.load_default()
        font_regular = ImageFont.load_default()

    # Add title
    title = f"Writing Practice - Page {page_number}"
    draw.text((width // 2 - 200, 50), title, fill="black", font=font_regular)

    # Define margins and line spacing
    margin_x = 100
    margin_y = 150
    line_spacing = 120
    guideline_spacing = 20

    # Add rows of letters with guidelines
    for i, letter in enumerate(letters):
        y_position = margin_y + i * line_spacing

        # Dashed uppercase and lowercase letters
        dashed_letters = f"{letter.upper()} {letter.lower()} {letter.upper()} {letter.lower()}"
        draw.text((margin_x, y_position), dashed_letters, fill="gray", font=font_dashed)

        # Add horizontal guidelines
        for j in range(3):  # Top, middle, and bottom lines
            guideline_y = y_position + 50 + j * guideline_spacing
            draw.line((margin_x, guideline_y, width - margin_x, guideline_y), fill="lightgray", width=2)

        # Add space for freehand practice
        freehand_line = "_" * 40  # A line of underscores
        draw.text((margin_x, y_position + 80), freehand_line, fill="black", font=font_regular)

    return image


def generate_writing_practice_book(output_file):
    # Letters A-Z
    alphabet = [chr(i) for i in range(65, 91)]  # A-Z
    pages = []

    # Divide letters into groups of 10 for each page
    for page_number, chunk_start in enumerate(range(0, len(alphabet), 10), start=1):
        letters_chunk = alphabet[chunk_start:chunk_start + 10]
        page = create_practice_page(letters_chunk, page_number)
        pages.append(page)

    # Save all pages into a single PDF
    pages[0].save(output_file, save_all=True, append_images=pages[1:])
    print(f"Writing practice book saved as {output_file}")


# Generate the writing practice book
generate_writing_practice_book("Kindergarten_Writing_Practice_Book.pdf")
