import os
import sys
import pygame as pg
from random import randint

WIDTH, HEIGHT = 1600, 900
os.chdir(os.path.dirname(os.path.abspath(__file__)))



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bomb = pg.Surface((20, 20)) # 表示領域
    bomb.set_colorkey((0, 0, 0)) # 背景透過
    bomb_rct = pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10) #円の描画
    bomb_rct.center = randint(10, WIDTH-10), randint(10, HEIGHT-10)
    clock = pg.time.Clock()
    tmr = 0
    keydict = {
        pg.K_UP:(0, -5), 
        pg.K_DOWN:(0, 5), 
        pg.K_LEFT:(-5, 0), 
        pg.K_RIGHT:(5, 0)
        }
    vx, vy = +5, +5
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, v in keydict.items():
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)


        screen.blit(kk_img, kk_rct)
        bomb_rct.move_ip(vx, vy)

        screen.blit(bomb, bomb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
