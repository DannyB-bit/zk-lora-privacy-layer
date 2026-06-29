import os
from PIL import Image, ImageDraw, ImageFont

def generate_gold_quote():
    # Text to render with exact line breaks and formatting
    text_lines = [
        '"The impossible is just code waiting to be written, physics waiting to be rewritten,',
        'math a work in progress, and truth waiting to be discovered."'
    ]
    
    # Image size (rectangular to fit perfectly on the page)
    width = 1200
    height = 160
    
    # Create text mask (grayscale)
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    
    # Find a good font
    font_paths = [
        "C:\\Windows\\Fonts\\arialbi.ttf", # Arial Bold Italic
        "C:\\Windows\\Fonts\\timesbi.ttf", # Times Bold Italic
        "C:\\Windows\\Fonts\\georgiai.ttf",
        "arial.ttf"
    ]
    
    font = None
    for path in font_paths:
        if os.path.exists(path):
            try:
                font = ImageFont.truetype(path, 25)
                break
            except:
                pass
    if not font:
        font = ImageFont.load_default()
        
    # Draw centered text on mask
    y_offset = 30
    for line in text_lines:
        try:
            bbox = draw.textbbox((0, 0), line, font=font)
            line_w = bbox[2] - bbox[0]
            line_h = bbox[3] - bbox[1]
        except AttributeError:
            line_w, line_h = draw.textsize(line, font=font)
            
        x = (width - line_w) // 2
        draw.text((x, y_offset), line, fill=255, font=font)
        y_offset += line_h + 20
        
    # Create metallic gold gradient (horizontal stripe gradient to simulate shine)
    gradient = Image.new("RGB", (width, height))
    # Multi-stop gold gradient colors: dark gold -> light gold -> pale shine -> dark gold
    stops = [
        (0.0, (160, 115, 35)),   # Dark Gold
        (0.3, (255, 223, 100)),  # Bright Gold
        (0.5, (255, 245, 200)),  # White-Gold Shine
        (0.7, (230, 175, 55)),   # Medium Gold
        (1.0, (140, 95, 25))     # Deep Gold/Bronze
    ]
    
    for y in range(height):
        t = y / float(height)
        c1, c2 = stops[0][1], stops[-1][1]
        t1, t2 = 0.0, 1.0
        for i in range(len(stops)-1):
            if stops[i][0] <= t <= stops[i+1][0]:
                t1, c1 = stops[i]
                t2, c2 = stops[i+1]
                break
        factor = (t - t1) / (t2 - t1) if t2 > t1 else 0.0
        r = int(c1[0] + (c2[0] - c1[0]) * factor)
        g = int(c1[1] + (c2[1] - c1[1]) * factor)
        b = int(c1[2] + (c2[2] - c1[2]) * factor)
        
        for x in range(width):
            gradient.putpixel((x, y), (r, g, b))
            
    # Create final image (black background)
    final_img = Image.new("RGB", (width, height), (0, 0, 0))
    # Paste the gradient onto the black background using the text mask
    final_img.paste(gradient, (0, 0), mask=mask)
    
    # Save image
    final_img.save("gold_quote.png")
    print("Generated gold_quote.png successfully!")

if __name__ == "__main__":
    generate_gold_quote()
