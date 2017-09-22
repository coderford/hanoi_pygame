import pygame

pygame.init()
pygame.display.set_caption("Towers of Hanoi")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

game_done = False
framerate = 60

# game vars:
steps = 0
n_plates = 3
plates = []

# colors:
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
gold = (239, 229, 51)
blue = (78,162,196) 
grey = (170, 170, 170)
green = (77, 206, 145)

def blit_text(screen, text, midtop, aa=True, font=None, font_name = None, size = None, color=(255,0,0)):
    if font is None:                                    # font option is provided to save memory if font is
        font = pygame.font.SysFont(font_name, size)     # already loaded and needs to be reused many times
    font_surface = font.render(text, aa, color)
    font_rect = font_surface.get_rect()
    font_rect.midtop = midtop
    screen.blit(font_surface, font_rect)

def menu_screen():  # to be called before starting actual game loop
    global screen, n_plates, game_done
    menu_done = False
    while not menu_done:  # every screen/scene/level has its own loop
        screen.fill(white)
        blit_text(screen, 'Towers of Hanoi', (323,122), font_name='sans serif', size=90, color=grey)
        blit_text(screen, 'Towers of Hanoi', (320,120), font_name='sans serif', size=90, color=gold)
        blit_text(screen, 'Use arrow keys to select difficulty:', (320, 220), font_name='sans serif', size=30, color=black)
        blit_text(screen, str(n_plates), (320, 260), font_name='sans serif', size=40, color=blue)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu_done = True
                if event.key in [pygame.K_RIGHT, pygame.K_UP]:
                    n_plates += 1
                    if n_plates > 6:
                        n_plates = 6
                if event.key in [pygame.K_LEFT, pygame.K_DOWN]:
                    n_plates -= 1
                    if n_plates < 1:
                        n_plates = 1
            if event.type == pygame.QUIT:
                menu_done = True
                game_done = True
        pygame.display.flip()
        clock.tick(60)
def draw_towers():
    global screen
    for xpos in range(40, 460+1, 200):
        pygame.draw.rect(screen, green, pygame.Rect(xpos, 400, 160 , 20))
        pygame.draw.rect(screen, grey, pygame.Rect(xpos+75, 200, 10, 200))

def make_plates():
    global n_plates, plates
    height = 20
    ypos = 397 - height
    width = n_plates * 23
    for i in range(n_plates):
        plate = {}
        plate['rect'] = pygame.Rect(0, 0, width, height)
        plate['rect'].midtop = (120, ypos)
        plate['val'] = n_plates-i
        plates.append(plate)
        ypos -= height+3
        width -= 23


def draw_plates():
    global screen, plates
    for plate in plates:
        pygame.draw.rect(screen, blue, plate['rect'])


menu_screen()
make_plates()
# main game loop:
while not game_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_done = True
    screen.fill(white)
    draw_towers()
    draw_plates()
    blit_text(screen, 'Steps: '+str(steps), (320, 20), font_name='mono', size=30, color=black)
    pygame.display.flip()
    clock.tick(framerate)