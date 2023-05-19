import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import random

pygame.init()
pygame.mixer.init()

CLOCK = pygame.time.Clock()

WIDTH, HEIGHT = (700, 524)
size = (WIDTH, HEIGHT)
WINDOW = pygame.display.set_mode(size)

FONT = pygame.font.Font("Lato-Regular.ttf",27)
TEXT_ELEMENT = FONT.render("Use Arrow Keys to change Scale",
            True,
            (25,25,25),
            (200,200,200))
IMAGE_INDEXES = (0,1,2,1,2,2,1,0,1,2,2,1,2,1,0)
diamond_circle_image = pygame.image.load(f"images/diamond_circle.png")
diamond_image = pygame.image.load(f"images/diamond.png")
circle_image = pygame.image.load(f"images/circle.png")
images = [
    diamond_circle_image,
    diamond_image,
    circle_image
]
COLOURS = ((224, 182, 109), (177, 196, 153), (166, 156, 140), (177, 145, 147), (145, 151, 177), (166, 140, 156), (132, 161, 141), (139, 162, 168), (162, 139, 150), (154, 166, 138), (156, 140, 116), (139, 160, 120))

button_size = 128
button_spacing = 10
rows = 3
cols = 5
scale = 0

pygame.display.set_icon(diamond_circle_image)
WINDOW.fill(random.choice(COLOURS))
pygame.display.set_caption("Sky: Children of the Light Practise Piano")

def play(index):
    keys = (0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24)
    note = pygame.mixer.Sound(file=f"audio/{(keys[index]+scale )}.wav")
    note.play()

button_rects = []

for i in range(rows):
    for j in range(cols):
        x = j * (button_size + button_spacing) + button_spacing
        y = i * (button_size + button_spacing) + button_spacing

        button_rect = pygame.Rect(x, y, button_size, button_size)
        button_rects.append(button_rect)
        WINDOW.blit(
            images[IMAGE_INDEXES[5*i+j]],
            button_rect)

pygame.display.flip()
RUNNING = True

VALID_KEYS = (
    pygame.K_q,
    pygame.K_w,
    pygame.K_e,
    pygame.K_r,
    pygame.K_t,
    pygame.K_a,
    pygame.K_s,
    pygame.K_d,
    pygame.K_f,
    pygame.K_g,
    pygame.K_z,
    pygame.K_x,
    pygame.K_c,
    pygame.K_v,
    pygame.K_b
)

HOLD_MAP =      [0]*15
ARROW_HOLD_MAP =[0]*2

CENTER = (WIDTH/2, 8*HEIGHT/9)

while RUNNING:

    WINDOW.blit(
        TEXT_ELEMENT,
        TEXT_ELEMENT.get_rect(center=CENTER),
        )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, button_rect in enumerate(button_rects):
                if button_rect.collidepoint(event.pos):
                    play(i)
        
    KEY_INPUT = pygame.key.get_pressed()

    index = 0
    for KEY in VALID_KEYS:
        if KEY_INPUT[KEY] and HOLD_MAP[index]==0:
            play(index)
            HOLD_MAP[index] = 1
        elif not KEY_INPUT[KEY]:
            HOLD_MAP[index] = 0

        index +=1
    CLOCK.tick(20)

    if KEY_INPUT[pygame.K_LEFT] and ARROW_HOLD_MAP[0]==0:
        ARROW_HOLD_MAP[0]=1
        scale -= 1
    elif KEY_INPUT[pygame.K_RIGHT] and ARROW_HOLD_MAP[1]==0:
        ARROW_HOLD_MAP[1]=1
        scale += 1
    else:
        ARROW_HOLD_MAP = [0,0]
        scale = scale%12
    CLOCK.tick(20)

    pygame.display.flip()

pygame.quit()