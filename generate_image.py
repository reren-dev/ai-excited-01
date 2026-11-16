#!/usr/bin/env python3
import math
import random
from PIL import Image, ImageDraw

def create_image():
    width, height = 1024, 1024
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    # 1. Sky Gradient (Dusk: Deep Indigo to Vibrant Sunset Orange)
    for y in range(height):
        t = y / height
        if t < 0.55:
            factor = t / 0.55
            r = int(22 + (85 - 22) * factor)
            g = int(14 + (40 - 14) * factor)
            b = int(55 + (90 - 55) * factor)
        else:
            factor = (t - 0.55) / 0.45
            r = int(85 + (255 - 85) * factor)
            g = int(40 + (130 - 40) * factor)
            b = int(90 + (60 - 90) * factor)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Add radiant sun glow near horizon
    sun_overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    sun_draw = ImageDraw.Draw(sun_overlay)
    sun_draw.ellipse([width * 0.48 - 280, height * 0.52 - 280, width * 0.48 + 280, height * 0.52 + 280], fill=(255, 170, 70, 90))
    sun_draw.ellipse([width * 0.48 - 140, height * 0.55 - 140, width * 0.48 + 140, height * 0.55 + 140], fill=(255, 215, 130, 140))
    image.paste(Image.alpha_composite(image.convert("RGBA"), sun_overlay).convert("RGB"))

    # 2. City Skyline at Bottom with detailed skyscrapers
    random.seed(123)
    skyline_base = height - 210
    
    bw = 0
    while bw < width:
        bx = bw
        bwidth = random.randint(40, 85)
        bheight = random.randint(130, 340)
        by = skyline_base + 50 - bheight
        
        # Building silhouette
        draw.rectangle([bx, by, bx + bwidth, height], fill=(18, 16, 30))
        
        # Glowing windows
        for wy in range(by + 12, height - 20, 20):
            for wx in range(bx + 6, bx + bwidth - 6, 12):
                if random.random() > 0.3:
                    w_color = (255, 225, 130) if random.random() > 0.15 else (120, 230, 255)
                    draw.rectangle([wx, wy, wx + 5, wy + 9], fill=w_color)
        bw += bwidth - 8

    # Foreground dark ocean water and foaming crests
    draw.rectangle([0, skyline_base + 25, width, height], fill=(12, 22, 40))
    draw.arc([0, skyline_base - 10, width, skyline_base + 70], 180, 360, fill=(230, 245, 255), width=8)

    # 3. Colossal Whale (Enhanced lightness, larger tail fluke, prominent eye & mouth)
    whale_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    w_draw = ImageDraw.Draw(whale_layer)

    # Main body polygon (Lighter blue-grey for maximum readability)
    body_points = [
        (190, 860),
        (110, 770),
        (85, 690),
        (130, 660),
        (210, 720),
        (350, 610),
        (530, 470),
        (710, 340),
        (840, 275),
        (790, 350),
        (660, 440),
        (460, 590),
        (290, 770)
    ]
    w_draw.polygon(body_points, fill=(130, 162, 195, 255))

    # Distinct Pale Belly (Clean cream / white-blue)
    belly_points = [
        (350, 610),
        (530, 470),
        (710, 340),
        (750, 370),
        (610, 510),
        (430, 670),
        (310, 750),
        (350, 610)
    ]
    w_draw.polygon(belly_points, fill=(238, 246, 252, 255))

    # Large Prominent Tail Fluke (Classic whale tail silhouette)
    w_draw.polygon([(100, 730), (40, 620), (120, 650), (160, 720)], fill=(110, 142, 175, 255))
    w_draw.polygon([(120, 720), (170, 600), (200, 650), (170, 730)], fill=(110, 142, 175, 255))
    # Tail notch highlight
    w_draw.line([(85, 690), (105, 695)], fill=(200, 220, 240, 255), width=4)

    # Large Pectoral Fin
    w_draw.polygon([(490, 540), (435, 690), (525, 630), (540, 570)], fill=(100, 132, 165, 255))

    # Clear Eye (Dark pupil with bright specular highlight)
    w_draw.ellipse([775, 305, 795, 325], fill=(25, 35, 50, 255))
    w_draw.ellipse([780, 310, 788, 318], fill=(255, 255, 255, 255))

    # Curved Smile / Mouth Line
    w_draw.arc([730, 290, 830, 385], 25, 85, fill=(40, 55, 75, 255), width=6)

    image.paste(whale_layer, (0, 0), whale_layer)

    # 4. Spiralling Sea Spray, Foam & Energetic Droplets
    spray_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(spray_layer)

    for i in range(150):
        angle = i * 0.13
        dist = 160 + i * 3.8
        cx = 460 + math.cos(angle + 1.1) * dist
        cy = 540 + math.sin(angle - 0.4) * dist * 0.85
        
        r = random.randint(5, 16)
        alpha = random.randint(160, 255)
        color_choice = random.choice([
            (170, 235, 255, alpha),
            (210, 250, 255, alpha),
            (255, 255, 255, alpha),
            (120, 220, 250, alpha)
        ])
        s_draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color_choice)

    # Dynamic cascading water arcs
    s_draw.arc([130, 430, 770, 870], 195, 325, fill=(190, 240, 255, 200), width=14)
    s_draw.arc([230, 330, 870, 770], 185, 315, fill=(230, 255, 255, 220), width=10)

    # 5. Tiny Surfer riding the wave crest near whale midsection
    surfer_x, surfer_y = 600, 415
    # Vibrant orange surfboard
    s_draw.polygon([
        (surfer_x - 14, surfer_y + 9),
        (surfer_x + 14, surfer_y - 9),
        (surfer_x + 18, surfer_y - 4),
        (surfer_x - 10, surfer_y + 14)
    ], fill=(255, 80, 40, 255))
    
    # Surfer body
    s_draw.ellipse([surfer_x - 5, surfer_y - 16, surfer_x + 5, surfer_y - 7], fill=(15, 20, 30, 255))
    s_draw.rectangle([surfer_x - 6, surfer_y - 7, surfer_x + 6, surfer_y + 5], fill=(15, 20, 30, 255))
    # Sparkly wake trail
    s_draw.line([(surfer_x - 24, surfer_y + 18), (surfer_x - 6, surfer_y + 6)], fill=(255, 255, 255, 240), width=5)

    image.paste(spray_layer, (0, 0), spray_layer)

    image.save("entry.png", "PNG")
    print("Successfully generated revised entry.png (1024x1024)")

if __name__ == "__main__":
    create_image()
