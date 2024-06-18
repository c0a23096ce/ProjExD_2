import os
import pygame as pg
from random import randint
import sys
import time


WIDTH, HEIGHT = 1600, 900
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def inscreen(rect: pg.Rect):
    x, y = True, True
    # print(f"rect:{type(rect)}")
    if 0 > rect.left or WIDTH < rect.right:
        x = False
    if 0 > rect.top or HEIGHT < rect.bottom:
        y = False
    return x, y


# 課題2
def circle_accs(r): #半径
    doublelist = []
    imglist = []
    accs = [a for a in range(1, 11)]
    for i in range(1, 11):
        img = pg.Surface((r*2*i, r*2*i))
        pg.draw.circle(img, (255, 0, 0), (r*i, r*i), r*i)
        img.set_colorkey((0, 0, 0))
        imglist.append(img)
        # doublelist.append(pg.draw.circle(img, (255, 0, 0), (r*i, r*i), r*i))
    return (accs, imglist, doublelist)


# 課題3
def gameover(screen):
    go = pg.Surface((WIDTH, HEIGHT))
    go_rct = pg.draw.rect(go, (0, 0, 0), (WIDTH, HEIGHT, 0, 0))
    go.set_alpha(100)
    go_rct.center = 0, 0
    sad_kk_img = pg.transform.rotozoom(pg.image.load("fig/8.png"), 0, 2.0)
    go_text = pg.font.Font(None, 80)
    go_text_render = go_text.render("Game Over", True, (255, 255, 255))
    screen.blit(go, go_rct)
    screen.blit(sad_kk_img, (800, 600))
    screen.blit(go_text_render, (800, 450))
    pg.display.update()
    time.sleep(5)


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    accs, bomb_img, surface = circle_accs(10)
    bomb = bomb_img[0]
    # bomb = pg.Surface((20, 20)) # 表示領域
    # bomb.set_colorkey((0, 0, 0)) # 背景透過
    # bomb_rct = pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10) # = 
    bomb_rct = bomb.get_rect()
    bomb_rct.center = randint(0, WIDTH), randint(0, HEIGHT)

    clock = pg.time.Clock()
    tmr = 0
    keydict = {
        pg.K_UP:(0, -5), 
        pg.K_DOWN:(0, 5), 
        pg.K_LEFT:(-5, 0), 
        pg.K_RIGHT:(5, 0)
        }
    # 課題1
    rotozoom = {
        (-5, -5):-45,
        (-5, 0):0,
        (-5, 5):45,
        (0, 5):90,
        (5, 5):135,
        (5, 0):180,
        (5, -5):225,
        (0, -5):270,
        (5, -5):315
        }
    # 課題2
    # accs, bomb_size, surface = circle_accs(10)
    # accs, bomb_img, surface = circle_accs(10)

    vx, vy = +5, +5
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.blit(bg_img, [0, 0]) 

        if kk_rct.colliderect(bomb_rct):  # 衝突判定
            #pass
            #課題3
            gameover(screen)
            return

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, v in keydict.items():
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)

        if inscreen(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)
        
        #bomb_rct = surface[min(tmr//500, 9)]
        #print(f"bomb_rct:{bomb_rct}")
        # print(f"surface:{bomb_img}")

        x, y = inscreen(bomb_rct)
        if not x:
            vx *= -1
        if not y:
            vy *= -1

        bomb_rct.move_ip(vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)])

        bomb = bomb_img[min(tmr//500, 9)]
        # bomb_rct = bomb.get_rect()
        # print(bomb_rct.center,bomb_rct,bomb_rct.width, bomb_rct.height)
        
        screen.blit(bomb, bomb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
