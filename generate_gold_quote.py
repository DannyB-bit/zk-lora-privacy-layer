import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def generate_metallic_gold_quote():
    # Exact text and line breaks
    text_lines = [
        '"The impossible is just code waiting to be written, physics waiting to be rewritten,',
        'math a work in progress, and truth waiting to be discovered."'
    ]
    
    width = 1200
    height = 160
    
    # 1. Create high-res text mask for anti-aliasing (we render at 2x and scale down)
    scale = 2
    w_s, h_s = width * scale, height * scale
    
    mask = Image.new("L", (w_s, h_s), 0)
    draw = ImageDraw.Draw(mask)
    
    # Font selection
    font_paths = [
        "C:\\Windows\\Fonts\\arialbi.ttf", # Arial Bold Italic
        "C:\\Windows\\Fonts\\timesbi.ttf", # Times Bold Italic
        "arial.ttf"
    ]
    font = None
    for path in font_paths:
        if os.path.exists(path):
            try:
                font = ImageFont.truetype(path, 24 * scale)
                break
            except:
                pass
    if not font:
        font = ImageFont.load_default()
        
    # Draw centered text on mask
    y_offset = 28 * scale
    for line in text_lines:
        try:
            bbox = draw.textbbox((0, 0), line, font=font)
            line_w = bbox[2] - bbox[0]
            line_h = bbox[3] - bbox[1]
        except AttributeError:
            line_w, line_h = draw.textsize(line, font=font)
            
        x = (w_s - line_w) // 2
        draw.text((x, y_offset), line, fill=255, font=font)
        y_offset += line_h + 18 * scale

    # 2. Create 3D Bevel layers
    # Convert mask to float for processing
    mask_im = mask.copy()
    
    # Create highlight and shadow offsets to simulate 3D bevel
    shift = 2
    highlight_mask = Image.new("L", (w_s, h_s), 0)
    shadow_mask = Image.new("L", (w_s, h_s), 0)
    
    # Paste shifted versions
    highlight_mask.paste(mask_im, (-shift, -shift))
    shadow_mask.paste(mask_im, (shift, shift))
    
    # Highlights are on the top-left edges
    highlights = Image.new("L", (w_s, h_s), 0)
    draw_hl = ImageDraw.Draw(highlights)
    # highlights = mask_im AND NOT highlight_mask
    # In PIL we can use ImageMath or simple composite
    
    # 3. Create Metallic Gold Reflection Gradient
    gradient = Image.new("RGB", (w_s, h_s))
    # Multi-stop metallic gold reflection map
    stops = [
        (0.0, (138, 100, 33)),   # #8A6421 (Dark Gold)
        (0.2, (212, 175, 55)),   # #D4AF37 (Metallic Gold)
        (0.35, (255, 245, 200)), # #FFF5C8 (Soft Highlight)
        (0.45, (255, 255, 255)), # #FFFFFF (Bright Chrome Shine)
        (0.55, (212, 175, 55)),   # #D4AF37 (Metallic Gold)
        (0.75, (138, 100, 33)),   # #8A6421 (Dark Gold)
        (1.0, (218, 165, 32))    # #DAA520 (Goldenrod)
    ]
    
    for y in range(h_s):
        t = y / float(h_s)
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
        
        for x in range(w_s):
            gradient.putpixel((x, y), (r, g, b))
            
    # Add a diagonal reflection sheen
    for y in range(h_s):
        for x in range(w_s):
            # Diagonal coordinate
            diag = (x + y) / float(w_s + h_s)
            if 0.45 <= diag <= 0.50:
                # Add white highlight
                r, g, b = gradient.getpixel((x, y))
                blend = (diag - 0.45) / 0.05
                r = int(r * (1 - blend) + 255 * blend)
                g = int(g * (1 - blend) + 255 * blend)
                b = int(b * (1 - blend) + 255 * blend)
                gradient.putpixel((x, y), (r, g, b))

    # 4. Render the 3D text
    text_gold = Image.new("RGB", (w_s, h_s), (0, 0, 0))
    text_gold.paste(gradient, (0, 0), mask=mask_im)
    
    # Apply Bevel Highlights (white/light gold on top-left)
    # We can simulate this by drawing the text shifted top-left in white with low opacity
    hl_color = (255, 253, 220) # Pale Gold
    sd_color = (60, 40, 10)     # Dark Shadow
    
    # We create a 3D effect by layering a shadow and a highlight
    shadow_img = Image.new("RGB", (w_s, h_s), (0, 0, 0))
    draw_sd = ImageDraw.Draw(shadow_img)
    
    # Draw shadow
    y_offset = 28 * scale
    for line in text_lines:
        try:
            bbox = draw_sd.textbbox((0, 0), line, font=font)
            line_w = bbox[2] - bbox[0]
            line_h = bbox[3] - bbox[1]
        except AttributeError:
            line_w, line_h = draw_sd.textsize(line, font=font)
        x = (w_s - line_w) // 2
        draw_sd.text((x + 2, y_offset + 2), line, fill=sd_color, font=font)
        y_offset += line_h + 18 * scale
        
    # Combine shadow with gold text
    final_3d = Image.new("RGB", (w_s, h_s), (0, 0, 0))
    final_3d.paste(shadow_img, (0, 0), mask=mask_im)
    final_3d.paste(text_gold, (0, 0), mask=mask_im)
    
    # Overlay highlights on top-left edges
    # We can do this by drawing a 1px offset text in white
    hl_img = Image.new("RGB", (w_s, h_s), (0, 0, 0))
    draw_hl = ImageDraw.Draw(hl_img)
    y_offset = 28 * scale
    for line in text_lines:
        try:
            bbox = draw_hl.textbbox((0, 0), line, font=font)
            line_w = bbox[2] - bbox[0]
            line_h = bbox[3] - bbox[1]
        except AttributeError:
            line_w, line_h = draw_hl.textsize(line, font=font)
        x = (w_s - line_w) // 2
        draw_hl.text((x - 1, y_offset - 1), line, fill=hl_color, font=font)
        y_offset += line_h + 18 * scale
        
    # Blend highlight on top
    final_3d.paste(hl_img, (0, 0), mask=highlights)
    
    # 5. Scale down with high-quality Lanczos resampling for perfect anti-aliasing
    final_3d_rescaled = final_3d.resize((width, height), Image.Resampling.LANCZOS)
    
    # Save image
    final_3d_rescaled.save("gold_quote.png")
    print("Generated 3D metallic gold_quote.png successfully!")

if __name__ == "__main__":
    generate_metallic_gold_quote()
