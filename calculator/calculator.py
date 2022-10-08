import pygame
import sys
from stringConverter import calculate


pygame.init()
pygame.font.init()
w = 300
h = 400

white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode((w, h))

def button(text, centerx, centery, size = 1):
    global p
    if size == 1:
        myfont = pygame.font.SysFont('Arial', 30)
    elif size == 2:
        myfont = pygame.font.SysFont('Arial', 15)
    elif size == 3:
        myfont = pygame.font.SysFont('Arial', 10)
    else:
        myfont = pygame.font.SysFont('Arial', 15)
    rect = pygame.draw.rect(screen, black, (centerx-20, centery-20, 40, 40), 0, 8)
    
    ts = myfont.render(text, True, white)
    tsR = ts.get_rect(center=(centerx, centery))
    screen.blit(ts, tsR)
    return p.append((centerx-20, centery-20, centerx+20, centery+20))

def text(text, leftx, lefty):
    rect1 = pygame.draw.rect(screen, black, (30, 30, 240, 90))
    myfont = pygame.font.SysFont('Arial', 20)
    ts = myfont.render(text, True, white)
    tsR = ts.get_rect(midleft=(leftx, lefty))
    screen.blit(ts, tsR)

def text2(text1, rightx, righty):
    text = str(text1)
    myfont = pygame.font.SysFont('Arial', 20)
    ts = myfont.render(text, True, white)
    tsR = ts.get_rect(midright=(rightx, righty))
    screen.blit(ts, tsR)
    
p = []
d = []
dstring = ''
screen.fill(white)

button('0', 90, 360)
button('1', 30, 300)
button('2', 90, 300)
button('3', 150, 300)
button('4', 30, 240)
button('5', 90, 240)
button('6', 150, 240)
button('7', 30, 180)
button('8', 90, 180)
button('9', 150, 180)
button('=', 210, 360)
button('+', 210, 300)
button('-', 210, 240)
button('x', 270, 240)
button('÷', 270, 300)
button('AC', 30, 360)
rect1 = pygame.draw.rect(screen, black, (30, 30, 240, 60))
pygame.display.update()
calculated = ''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for i in range(0, len(p)):
                if pos[0] > p[i][0] and pos[0] < p[i][2] and pos[1] > p[i][1] and pos[1] < p[i][3]:
                    if i == 15:
                        d = []
                        dstring = ''
                        calculated = ''
                    elif i == 10:
                        calculated = calculate(dstring)                     
                    else:
                        if i <= 9:
                            d.append(i)
                        elif i > 9:
                            if i == 11:
                                d.append('+')
                            elif i == 12:
                                d.append('-')
                            elif i == 13:
                                d.append('x')
                            elif i == 14:
                                d.append('÷')
                    print(d)
                    print(dstring)
                    dstring = ''
                    for e in range(0, len(d)):
                        try:
                            print(int(d[e]))
                            dstring = dstring + str(d[e])
                        except:
                            dstring = dstring + ' '
                            dstring = dstring + str(d[e])
                            dstring = dstring + ' '
                    print(d)
                    print(dstring)
    
    text(dstring, 45, 60)
    text2(calculated, 255, 90)
    pygame.display.update()
