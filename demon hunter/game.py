

from gamelib import *

game = Game(1000,700, "Demon Hunter")

# graphics variable
bk1 = Image("start.jpg",game)
bk1.resizeTo(game.width,game.height)
game.setBackground(bk1)
title = Image("title.png",game)
title.moveTo(x=500,y=40)
play = Image("PLAY.png",game)
play.moveTo(x=500,y=650)
story = Image("story.png",game)
story.moveTo(x=500,y=550)
health = Image("Health.png",game)
health.resizeBy(-30)
health.moveTo(x=100,y=650)
kills = Image("kills.png",game)
kills.resizeBy(-30)
kills.moveTo(x=800,y=650)


#Title screen
game.over = False
while not game.over:
    game.processInput()
    
    bk1.draw()
    title.draw()
    play.draw()
    story.draw()
    

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    game.update(4)
#level 1 graphics
bk2 = Image("level1.jpg",game)
bk2.resizeTo(game.width,game.height)
level1 = Image("level-1.png",game)
level1.resizeBy(-50)
level1.moveTo(x=100,y=25)
hero = Image("hero.png",game)
hero.resizeBy(-20)
key = Image("key.png",game)
key.resizeBy(-90)
key.moveTo(x=750,y=300)
plasmaball = Animation("plasmaball1.png",11,game,352/11,32)
plasmaball.visible = False

badguy = []
for index in range(100):
    badguy.append(Image("badguy1.png",game))
for index in range(100):
    x = randint(100,700)
    y = randint(100,4000)
    badguy[index].moveTo(x, -y)
    badguy[index].resizeBy(-60)
    s = randint(8,12)
    badguy[index].setSpeed(s,180)
    badguy[index].resizeBy(200)
    
#level 2 graphics
bk3 = Image("level2.png",game)
bk3.resizeTo(game.width,game.height)
level2 = Image("level-2.png",game)
level2.resizeBy(-50)
level2.moveTo(x=100,y=25)

knight = []
for index in range(50):
    knight.append(Image("knight.png",game))
for index in range(50):
    x = randint(100,700)
    y = randint(100,4000)
    knight[index].moveTo(x, -y)
    knight[index].resizeBy(-60)
    s = randint(8,12)
    knight[index].setSpeed(s,180)
    knight[index].resizeBy(200)
#level 3 graphics
bk4 = Image("boss room.jpg",game)
bk4.resizeTo (game.width,game.height)
finallevel = Image("final-level.png",game)
finallevel.moveTo(x=500,y=50)
ape = Image("evil.png",game)
ape.resizeBy(-40)
ape = []
for index in range(50):
    ape.append(Image("evil.png",game))
for index in range(50):
    x = randint(100,700)
    y = randint(100,4000)
    ape[index].moveTo(x, -y)
    ape[index].resizeBy(-60)
    s = randint(8,12)
    ape[index].setSpeed(s,180)
    ape[index].resizeBy(20)

#Character movement
back = Animation("walk for.png",4,game,600/4,184)
back.resizeBy(-50)
forward= Animation("walk back.png",4,game,527/4,197)
forward.resizeBy(-50)
left = Animation("walk side 1.png",4,game,492/4,151)
left.resizeBy(-50)
right = Animation("walk side.png",4,game,493/4,159)
right.resizeBy(-50)
    
game.over = False
#level 1
badguyPassed = 0
badguyskilled = 0
while not game.over:
    game.processInput()

    bk2.draw()
    level1.draw()
    key.draw()
    plasmaball.move()
    health.draw()
    game.drawText(hero.health,health.right + 10, health.y,Font(black,60,green))
    kills.draw()
    game.drawText(badguyskilled,kills.right + 10, kills.y,Font(black,60,green))
    
   

    if keys.Pressed[K_UP]:
        hero.y -= 8
        forward.moveTo(hero.x,hero.y)
        forward.draw()
    elif keys.Pressed[K_DOWN]:
        hero.y += 8
        back.moveTo(hero.x,hero.y)
        back.draw()
    elif keys.Pressed[K_RIGHT]:

        hero.x += 8
        right.moveTo(hero.x,hero.y)
        right.draw()
    elif keys.Pressed[K_LEFT]:
        hero.x -= 8
        left.moveTo(hero.x,hero.y)
        left.draw()
    else:
        forward.moveTo(hero.x,hero.y)

        hero.collidedWith(key,game.over)

    if keys.Pressed[K_SPACE]:
        plasmaball.moveTo(hero.x, hero.y)
        plasmaball.setSpeed(24,0)
        plasmaball.visible = True

    for index in range(100):
        if badguy[index].y < 210:
            badguy[index].move()
        else:
            badguy[index].forward(4)
            badguy[index].move()

        if badguy[index].y >= 200 and badguy[index].y < 210:
            a = badguy[index].angleTo(hero)
            badguy[index].rotateTo(a)

        if badguy[index].isOffScreen(100):
            game.over = True

        if keys.Pressed[K_SPACE]: 
            plasmaball.moveTo(hero.x, hero.y)
            plasmaball.setSpeed(24,0)
            plasmaball.visible = True

                                   
        if plasmaball.collidedWith(badguy[index]):
            badguy[index].visible = False
            badguyskilled += 1

       
        
        if badguy[index].collidedWith(hero):
            hero.health -= 1

        if hero.health < 1:
            game.over = True

    
    game.drawText(" x " +str(game.score),health.x - 10, health.y - 40)
    game.update(30)
                 
game.over = False
#level 2
knightPassed = 0
knightskilled = 0

while not game.over:
    game.processInput()
    
    bk3.draw()
    level2.draw()
    plasmaball.move()
    health.draw()
    game.drawText(hero.health,health.right + 10, health.y,Font(black,60,green))
    kills.draw()
    game.drawText(knightskilled,kills.right + 10, kills.y,Font(black,60,green))

   
    if keys.Pressed[K_UP]:
        hero.y -= 8
        forward.moveTo(hero.x,hero.y)
        forward.draw()
    elif keys.Pressed[K_DOWN]:
        hero.y += 8
        back.moveTo(hero.x,hero.y)
        back.draw()
    elif keys.Pressed[K_RIGHT]:

        hero.x += 8
        right.moveTo(hero.x,hero.y)
        right.draw()
    elif keys.Pressed[K_LEFT]:
        hero.x -= 8
        left.moveTo(hero.x,hero.y)
        left.draw()
    else:
        forward.moveTo(hero.x,hero.y)

    if keys.Pressed[K_SPACE]:
        plasmaball.moveTo(hero.x, hero.y)
        plasmaball.setSpeed(24,0)
        plasmaball.visible = True

    for index in range(50):
        if knight[index].y < 210:
            knight[index].move()
        else:
            knight[index].forward(4)
            knight[index].move()

        if knight[index].y >= 200 and knight[index].y < 210:
            a = knight[index].angleTo(hero)
            knight[index].rotateTo(a)

        if knight[index].isOffScreen("bottom") and knight[index].visible:
            knightPassed += 1
            knight[index].visible = False
            if knightPassed >= 50:
                game.over = True
        if knight[index].collidedWith(hero):
            hero.health -= 10

        if plasmaball.collidedWith(knight[index]):
            knight[index].visible = False
            knightskilled += 1


        if hero.health < 1:
            game.over = True

       
    game.update(30)
game.over = False
# level 3
apePassed = 0
apeskilled = 0
while not game.over:
    game.processInput()

    bk4.draw()
    finallevel.draw()
    plasmaball.move()
    health.draw()
    game.drawText(hero.health,health.right + 10, health.y,Font(black,60,green))
    kills.draw()
    game.drawText(apeskilled,kills.right + 10, kills.y,Font(black,60,green))

    
    if keys.Pressed[K_UP]:
        hero.y -= 8
        forward.moveTo(hero.x,hero.y)
        forward.draw()
    elif keys.Pressed[K_DOWN]:
        hero.y += 8
        back.moveTo(hero.x,hero.y)
        back.draw()
    elif keys.Pressed[K_RIGHT]:

        hero.x += 8
        right.moveTo(hero.x,hero.y)
        right.draw()
    elif keys.Pressed[K_LEFT]:
        hero.x -= 8
        left.moveTo(hero.x,hero.y)
        left.draw()
    else:
        forward.moveTo(hero.x,hero.y)

    if keys.Pressed[K_SPACE]:
        plasmaball.moveTo(hero.x, hero.y)
        plasmaball.setSpeed(24,0)
        plasmaball.visible = True

    for index in range(50):
        if ape[index].y < 210:
            ape[index].move()
        else:
            ape[index].forward(6)
            ape[index].move()

        if ape[index].y >= 200 and ape[index].y < 210:
            a = ape[index].angleTo(hero)
            ape[index].rotateTo(a)

        if ape[index].isOffScreen("right") and ape[index].visible:
            apePassed += 1
            ape[index].visible = False
            if apePassed >= 50:
                game.over = True
        if ape[index].collidedWith(hero):
            hero.health -= 20

        if ape[index].collidedWith(hero):
            hero.health -= 10

        if plasmaball.collidedWith(ape[index]):
            ape[index].visible = False
            apeskilled += 1

        if hero.health < 1:
            game.over = True

        game.drawText(" x " +str(game.score),health.x - 10, health.y - 40)

    game.update(30)
game.over = False
game.quit()
