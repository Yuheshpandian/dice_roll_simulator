# importing all required libraries
import pygame
import random

# initialising pygame
pygame.init()

font = pygame.font.Font("freesansbold.ttf", 50)
#display
screen = pygame.display.set_mode((700, 700))

pygame.display.set_caption('DICE-ROLL SIMULATOR')
pygame.display.set_icon(pygame.image.load('dice (3).png'))
roll_btn = pygame.image.load("dice (2).png")
roll_btn_rect = roll_btn.get_rect()
roll_btn_rect.topleft = (296, 572)

back = pygame.transform.scale(pygame.image.load('PngItem_5262081.png'), (100,100))
back_rect = back.get_rect()
back_rect.topleft = (300, 500)

# func tat is called when roll_btn is clicked
def btn_clicked(rect, img):
    mouse_pos = pygame.mouse.get_pos()

    screen.blit(img, (rect.x, rect.y))

    if rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[2]:
            return True

# list containing all paths of dice faces
dice = ['dice-six-faces-five.png', 'dice-six-faces-four.png', 'dice-six-faces-one.png', 'dice-six-faces-six.png', 'dice-six-faces-two.png', 'dice-six-faces-three.png']

run = True

win1_text = font.render('CLICK TO ROLL THE DICE', True, 'black')
win2_text = font.render('YOU GOT ^_^', True, 'black')
win2_text2 = font.render('roll again', True, 'black')


def win2(clr,obj,pos):
    run1 = True
    screen2 = pygame.display.set_mode((700, 700))
    while run1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
        screen2.fill(clr)
        mos_pos = pygame.mouse.get_pos()
        screen2.blit(win2_text, (200, 50))
        screen2.blit(back, (back_rect.x,back_rect.y))
        screen2.blit(win2_text2, (250, 650))
        screen2.blit(obj, pos)
        if back_rect.collidepoint(mos_pos):
            if pygame.mouse.get_pressed()[2]:
                run1 = False
        pygame.display.flip()


# main loop
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    screen.fill('white')
    screen.blit(win1_text, (30,250))
    if btn_clicked(roll_btn_rect, roll_btn):
        dice_img = pygame.transform.scale(pygame.image.load(random.choice(dice)), (200, 200))

        win2('white', dice_img, (250,200))

    pygame.display.flip()
