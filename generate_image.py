import math
import random
from PIL import Image, ImageDraw

def draw_cosmic_tiger():
    width, height = 1024, 1024
    image = Image.new("RGB", (width, height), (3, 5, 15))
    draw = ImageDraw.Draw(image, "RGBA")
    
    random.seed(1337)

    # 1. Background Starfield
    for _ in range(1000):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        brightness = random.randint(120, 255)
        size = random.choice([1, 1, 2, 2, 3])
        color = random.choice([
            (255, 255, 255, brightness),
            (180, 220, 255, brightness),
            (255, 210, 140, brightness)
        ])
        draw.ellipse([x, y, x + size, y + size], fill=color)

    # 2. Spiral Galaxy in Center/Right (Revealed behind cracks)
    gx, gy = 700, 350
    # Vibrant galaxy glow rings
    for r in range(400, 10, -15):
        alpha = int(max(0, 100 * (1 - r / 400)))
        draw.ellipse([gx - r, gy - r//2, gx + r, gy + r//2], fill=(30, 160, 210, alpha // 3))
        draw.ellipse([gx - r//2, gy - r, gx + r//2, gy + r], fill=(255, 180, 60, alpha // 4))

    # Spiral arms stars
    for i in range(400):
        angle = i * 0.12
        dist = i * 1.3
        sx = int(gx + math.cos(angle) * dist)
        sy = int(gy + math.sin(angle) * (dist * 0.55))
        if 0 <= sx < width and 0 <= sy < height:
            col = (220, 255, 255, random.randint(180, 255))
            draw.ellipse([sx, sy, sx + 2, sy + 2], fill=col)

    # Glass cracks radiating across the night sky
    crack_lines = [
        [(700, 350), (520, 260), (380, 180), (220, 90), (90, 40)],
        [(520, 260), (580, 480), (640, 620), (780, 780)],
        [(380, 180), (320, 320), (180, 420), (70, 580)],
        [(220, 90), (280, 220), (440, 360), (520, 520)],
        [(580, 480), (840, 320), (960, 160)],
        [(320, 320), (120, 280)]
    ]
    for line in crack_lines:
        for j in range(len(line) - 1):
            p1, p2 = line[j], line[j+1]
            draw.line([p1, p2], fill=(200, 255, 255, 250), width=4)
            draw.line([p1, p2], fill=(255, 255, 255, 255), width=2)
            # Glass shard polygons
            hx, hy = (p1[0]+p2[0])//2, (p1[1]+p2[1])//2
            draw.polygon([
                (hx, hy), (hx + random.randint(-18, 18), hy + random.randint(-18, 18)),
                (hx + random.randint(-12, 12), hy + random.randint(-12, 12))
            ], fill=(160, 230, 255, 140))

    # 3. Dark Rocky Cliff at bottom-left
    cliff_polygon = [
        (0, 1024), (0, 780), (140, 760), (220, 730), (300, 770), 
        (380, 840), (460, 940), (520, 1024)
    ]
    draw.polygon(cliff_polygon, fill=(10, 14, 25))
    draw.line([(0, 780), (140, 760), (220, 730), (300, 770), (380, 840)], fill=(45, 65, 95), width=4)

    # Tiny Hooded Traveler holding glowing book
    tx, ty = 170, 705
    # Hooded body
    draw.polygon([(tx, ty), (tx - 16, ty + 45), (tx + 16, ty + 45)], fill=(15, 20, 35))
    # Head / hood
    draw.ellipse([tx - 9, ty - 18, tx + 9, ty + 2], fill=(25, 30, 45))
    # Open glowing book
    draw.rectangle([tx + 12, ty + 15, tx + 38, ty + 32], fill=(255, 255, 220))
    for r in range(30, 5, -6):
        draw.ellipse([tx + 25 - r, ty + 23 - r, tx + 25 + r, ty + 23 + r], fill=(255, 210, 80, 35))

    # Flying pages turning into birds / butterflies of light
    page_positions = [
        (tx + 48, ty + 2), (tx + 75, ty - 25), (tx + 110, ty - 60),
        (tx + 90, ty - 105), (tx + 145, ty - 140), (tx + 180, ty - 190)
    ]
    for px, py in page_positions:
        draw.polygon([(px, py), (px + 12, py - 8), (px + 16, py + 5), (px + 5, py + 10)], fill=(255, 255, 220, 240))
        draw.ellipse([px-4, py-4, px+18, py+14], fill=(255, 190, 80, 70))

    # 4. ENORMOUS COSMIC TIGER Leaping Diagonally with clear anatomy
    # Body glowing nebula aura
    for offset_r in range(110, 10, -20):
        alpha = int(130 * (1 - offset_r / 110))
        draw.ellipse([280 - offset_r, 480 - offset_r, 780 + offset_r, 720 + offset_r], fill=(255, 130, 10, alpha // 2))
        draw.ellipse([380 - offset_r, 320 - offset_r, 880 + offset_r, 580 + offset_r], fill=(255, 190, 40, alpha // 2))

    # Powerful Hind Legs (coiled at bottom-left)
    draw.polygon([(240, 740), (360, 660), (410, 730), (280, 810)], fill=(220, 110, 10))
    draw.polygon([(280, 810), (380, 750), (330, 670), (240, 740)], fill=(255, 140, 20))
    # Hind Paws with claws
    draw.polygon([(265, 805), (295, 835), (255, 825)], fill=(255, 220, 150))

    # Massive Muscular Torso
    draw.polygon([(340, 630), (580, 450), (780, 290), (720, 410), (480, 590), (370, 690)], fill=(240, 130, 15))
    # Bright golden chest & underbelly
    draw.polygon([(400, 610), (600, 460), (740, 340), (680, 430), (480, 580), (420, 640)], fill=(255, 195, 50))

    # Extended Forelegs reaching forward-right
    draw.polygon([(660, 360), (835, 210), (880, 245), (710, 410)], fill=(230, 120, 10))
    draw.polygon([(710, 300), (900, 150), (945, 190), (760, 350)], fill=(255, 150, 25))
    # Front Paws with sharp glowing claws
    draw.polygon([(885, 220), (925, 250), (905, 260), (865, 230)], fill=(255, 240, 180))
    draw.polygon([(935, 170), (975, 200), (955, 210), (915, 180)], fill=(255, 240, 180))

    # Large Ferocious Roaring Head at Top-Right
    # Head base polygon
    draw.polygon([
        (765, 270), (845, 210), (915, 140), (945, 200), (880, 290), (800, 320)
    ], fill=(255, 140, 15))
    # Tiger Ears (prominent, pointed forward/up)
    draw.polygon([(785, 260), (770, 210), (810, 240)], fill=(200, 90, 10))
    draw.polygon([(870, 190), (895, 140), (910, 180)], fill=(200, 90, 10))

    # Roaring Open Mouth (deep dark interior with sharp white fangs and tongue)
    draw.polygon([
        (890, 170), (960, 130), (945, 210), (885, 230)
    ], fill=(30, 5, 5))
    # Sharp white fangs
    draw.polygon([(900, 175), (915, 200), (895, 195)], fill=(255, 255, 255))
    draw.polygon([(935, 150), (950, 190), (930, 180)], fill=(255, 255, 255))
    # Red tongue
    draw.polygon([(915, 200), (935, 185), (940, 210), (920, 220)], fill=(220, 50, 50))

    # Electric-Cyan Blue Accents along Spine, Back, and Tail
    spine_pts = [
        (360, 660), (440, 580), (540, 480), (640, 380), (740, 290), (805, 245)
    ]
    for i in range(len(spine_pts) - 1):
        draw.line([spine_pts[i], spine_pts[i+1]], fill=(40, 235, 255, 255), width=10)
        draw.line([spine_pts[i], spine_pts[i+1]], fill=(255, 255, 255, 255), width=4)

    # Long Sweeping Tail with Cyan Tip
    tail_pts = [
        (340, 630), (230, 560), (150, 450), (95, 340), (60, 230)
    ]
    for i in range(len(tail_pts) - 1):
        draw.line([tail_pts[i], tail_pts[i+1]], fill=(255, 130, 15), width=18 - i*2)
        draw.line([tail_pts[i], tail_pts[i+1]], fill=(40, 235, 255), width=7)

    # Bold Dark Tiger Stripes across Body
    stripe_list = [
        [(440, 560), (475, 650)],
        [(495, 520), (530, 600)],
        [(555, 470), (590, 560)],
        [(615, 420), (650, 510)],
        [(675, 370), (710, 455)],
        [(735, 320), (765, 395)],
        [(370, 690), (395, 745)],
        [(315, 610), (340, 670)],
        [(275, 750), (300, 810)]
    ]
    for stripe in stripe_list:
        draw.line(stripe, fill=(15, 5, 2), width=14)

    # Thousands of Star Points over Tiger Body
    for _ in range(500):
        tx_star = random.randint(120, 960)
        ty_star = random.randint(140, 840)
        draw.ellipse([tx_star, ty_star, tx_star + 2, ty_star + 2], fill=(255, 255, 255, random.randint(190, 255)))

    # 5. Momentum: Vortexes of Light, Shooting Embers, Star Trails
    for _ in range(150):
        ex = random.randint(150, 980)
        ey = random.randint(80, 850)
        length = random.randint(12, 40)
        ex2 = ex + int(length * 1.6)
        ey2 = ey - int(length * 0.7)
        draw.line([(ex, ey), (ex2, ey2)], fill=(255, 210, 120, 200), width=2)
        draw.ellipse([ex2, ey2, ex2 + 2, ey2 + 2], fill=(255, 255, 255, 230))

    # Save final PNG
    image.save("entry.png", "PNG")
    print("Successfully generated refined entry.png")

if __name__ == "__main__":
    draw_cosmic_tiger()
