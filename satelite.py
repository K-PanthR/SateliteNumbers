import pgzrun , random
WIDTH=800
HEIGHT=600
satelites=[]
number_satelite=8
def create_satelite():
    for i in range(0,number_satelite):
        satelite=Actor("satellite")
        satelite.pos = random.randint(40 , WIDTH-40) , random.randint (40 , HEIGHT-40)
        satelites.append(satelite)
def draw():
    #screen.blit("background" , (0,0))
    screen.fill("black")
    number=1
    for satelite in satelites:
        screen.draw.text(str(number) , (satelite.pos[0] , satelite.pos[1]+20))
        satelite.draw()
        number=number+1
create_satelite()
pgzrun.go()