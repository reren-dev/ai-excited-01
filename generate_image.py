import os
import sys
import subprocess
import urllib.parse
from PIL import Image, ImageDraw, ImageFont

PROMPT = (
    "A breathtaking, highly dynamic, and energetic cinematic fantasy digital artwork of a colossal cosmic tiger leaping from an open ancient book. "
    "A tiny traveler stands on a dark rocky cliff in the bottom-left corner holding the glowing book. "
    "A massive celestial tiger made of vibrant orange-gold nebula clouds, electric-cyan stardust, and cosmic fire energy erupts diagonally toward the top right, "
    "shattering the dark night sky like breaking glass to reveal a shimmering spiral galaxy behind it. "
    "Surrounded by vortexes of light, flying book pages turning into celestial birds, and glowing star trails. "
    "High contrast, cinematic lighting, ultra-sharp micro-details, epic scale, 1024x1024 square."
)

def draw_fallback_image(path):
    print("Drawing fallback PIL vector cosmic tiger image...")
    img = Image.new("RGB", (1024, 1024), color=(5, 8, 20))
    draw = ImageDraw.Draw(img)
    import random
    rng = random.Random(888)
    for _ in range(300):
        x = rng.randint(0, 1023)
        y = rng.randint(0, 1023)
        r = rng.choice([1, 1, 2, 2, 3])
        color = rng.choice([(200, 220, 255), (255, 180, 100), (100, 220, 255), (255, 255, 255)])
        draw.ellipse([x-r, y-r, x+r, y+r], fill=color)
        
    for i in range(150):
        angle = i * 0.2
        radius = i * 2.5
        gx = 750 + int(radius * 0.8 * math.cos(angle))
        gy = 250 + int(radius * 0.5 * math.sin(angle))
        c = int(150 + 105 * (i / 150))
        draw.ellipse([gx-2, gy-2, gx+2, gy+2], fill=(c, c-30, 255))

    cliff_polygon = [(0, 1024), (0, 750), (150, 780), (300, 720), (450, 800), (350, 1024)]
    draw.polygon(cliff_polygon, fill=(15, 20, 30))
    
    draw.rectangle([120, 730, 135, 770], fill=(240, 240, 240))
    draw.polygon([(110, 745), (120, 740), (125, 755), (115, 760)], fill=(255, 220, 100))

    tiger_points = [(200, 700), (350, 550), (550, 400), (750, 250), (850, 200), (800, 300), (600, 450), (400, 600), (250, 720)]
    for pt in tiger_points:
        draw.ellipse([pt[0]-60, pt[1]-60, pt[0]+60, pt[1]+60], fill=(255, 140, 40))
        draw.ellipse([pt[0]-40, pt[1]-40, pt[0]+40, pt[1]+40], fill=(255, 220, 100))
        
    draw.polygon([(780, 180), (870, 130), (850, 240), (790, 230)], fill=(255, 200, 50))
    
    for _ in range(25):
        sx = rng.randint(400, 950)
        sy = rng.randint(100, 600)
        sz = rng.randint(10, 40)
        draw.polygon([(sx, sy), (sx+sz, sy-sz//2), (sx+sz//2, sy+sz)], outline=(150, 220, 255), width=2)

    img.save(path, "JPEG", quality=90)
    print("Fallback image saved successfully.")

import math

def main():
    # Revised seed: 888 for a different generation run
    encoded = urllib.parse.quote(PROMPT)
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&seed=888&model=flux&nologo=true"
    
    temp_raw = "temp_raw.jpg"
    success = False
    
    for attempt in range(2):
        print(f"Downloading from Pollinations with revised seed 888 (attempt {attempt + 1})...")
        cmd = ["curl", "-s", "-S", "-L", "--max-time", "60", url, "-o", temp_raw]
        res = subprocess.run(cmd)
        if res.returncode == 0 and os.path.exists(temp_raw):
            try:
                with Image.open(temp_raw) as img:
                    img.verify()
                success = True
                print("Download and verification successful!")
                break
            except Exception as e:
                print(f"Downloaded file verification failed: {e}")
        else:
            print("Curl command failed or file missing.")
            
    if success:
        try:
            with Image.open(temp_raw) as img:
                img = img.convert("RGB")
                w, h = img.size
                if w != 1024 or h != 1024:
                    print(f"Resizing/cropping from {w}x{h} to 1024x1024...")
                    ratio = max(1024 / w, 1024 / h)
                    new_w = int(w * ratio)
                    new_h = int(h * ratio)
                    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                    left = (new_w - 1024) // 2
                    top = (new_h - 1024) // 2
                    img = img.crop((left, top, left + 1024, top + 1024))
                
                # Crop slightly from bottom to remove any potential watermark if present
                # e.g., crop bottom 30 pixels if needed, or keep 1024x1024
                # Let's ensure exact 1024x1024
                img.save("entry.png", "JPEG", quality=90)
                print("entry.png saved successfully via Pollinations API (revised run).")
        except Exception as e:
            print(f"Error processing downloaded image: {e}")
            success = False
            
    if not success:
        print("Pollinations download/processing failed. Using fallback drawing.")
        draw_fallback_image("entry.png")
        
    if os.path.exists("entry.png"):
        size_bytes = os.path.getsize("entry.png")
        print(f"entry.png size: {size_bytes} bytes ({size_bytes / (1024*1024):.2f} MiB)")
        with Image.open("entry.png") as im:
            print(f"entry.png dimensions: {im.size}, format: {im.format}")
    else:
        print("ERROR: entry.png was not created!")
        sys.exit(1)

if __name__ == "__main__":
    main()
