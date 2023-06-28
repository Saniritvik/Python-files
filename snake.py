import math
import random
import pygame
import tkinter as tk

from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500
    
    def __init__(self,start,dirnx=1,dirny=0,color=(0,255,0)):
        self.pos = start 
        self.dirnx = dirnx 
        self.dirny = dirny
        self.color = color
       
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx,self.pos[1] + self.dirny)
    
    def draw(self, surface, eyes=False):
        distance = self.w // self.rows
        x = self.pos[0]
        y = self.pos[1]
        pygame.draw.rect(surface, self.color, (x*distance+1,y*distance+1, distance-2, distance-2))
        if eyes:
            centre = distance//2
            radius = 3
            circleMiddle = (x*distance+centre-radius,y*distance+8)
            circleMiddle2 = (x*distance + distance -radius*2, y*distance+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

class snake(object):
    body=[]
    turns = {
        
    }
    
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dx = 0
        self.dy = 1
        
    
    def move(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
        
        
        ## Gives you list of all keys on a keyboard
            movement = pygame.key.get_pressed()
        
        ## Check which keys are being pressed by checking if they are true
            for i in movement:
                if movement[pygame.K_LEFT]:
                    self.dx = -1 
                    self.dy = 0
                    self.turns[self.head.pos[:]] = [self.dx,self.dy] ## Storing key value pair of the snakes head and the idrection of where it is turning
                
                elif movement[pygame.K_RIGHT]:
                    self.dx = 1
                    self.dy = 0
                    self.turns[self.head.pos[:]] = [self.dx,self.dy]
                
                elif movement[pygame.K_UP]:
                    self.dx = 0
                    self.dy = -1
                    self.turns[self.head.pos[:]] = [self.dx,self.dy]
                
                elif movement[pygame.K_DOWN]:
                    self.dx = 0
                    self.dy = 1
                    self.turns[self.head.pos[:]] = [self.dx,self.dy]
                
        for i,a in enumerate(self.body): ##The content of self.body is a cube object
            poss = a.pos[:]
           
            if poss in self.turns: 
                turned = self.turns[poss]
                a.move(turned[0],turned[1])
                if i == len(self.body)-1: 
                   self.turns.pop(poss)
            else:
                
                if a.dirnx == -1 and a.pos[0] <= 0:
                   a.pos = (a.rows - 1, a.pos[1])
                
                elif a.dirnx == 1 and a.pos[0] >= a.rows - 1:
                    a.pos = (0, a.pos[1])
                
                elif a.dirny == -1 and a.pos[1] <=0:
                    a.pos = (a.pos[0],a.rows - 1)
                
                elif a.dirny == 1 and a.pos[1] >= a.rows - 1:
                    a.pos = (a.pos[0],0)
                
                else:
                    a.move(a.dirnx,a.dirny)
            
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {
            
        }
        self.dx = 0
        self.dy = 1
    
    def addCube(self):
        tail = self.body[-1]
        dx = tail.dirnx
        dy = tail.dirny
        
        if dx == 1 and dy == 0: 
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        
        elif dx == -1 and dy == 0 : 
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
            
        elif dx == 0 and dy == 1: 
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
            
        elif dx == 0 and dy == -1: 
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
        self.body[-1].dirnx=dx
        self.body[-1].dirny=dy
       
    def draw(self, surface):
        for i,a in enumerate(self.body):
            if i == 0: 
                a.draw(surface,True)
            else: 
                a.draw(surface)

def drawGrid(w, rows, surface):
    dis= w // rows
    x = 0 
    y = 0
    for i in range(rows):
        x += dis
        y += dis
        pygame.draw.line(surface,"black",(x,0),(x,w))
        pygame.draw.line(surface,"black",(0,y),(w,y))
       
def redrawWindow(surface):
    global width,rows,snack,snakee
    surface.fill(("black"))
    snakee.draw(surface)
    snack.draw(surface)
    drawGrid(width,rows,surface)
    pygame.display.update()

def randomSnack(rows, item):
    spos = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), spos))) > 0:
            continue
        else:
            break
    return (x,y)


def message_box(subject, content):
    root = tk.Tk() # new tkinter window    
    root.attributes("-topmost", True)
    
    # on top of all oter windows    
    root.withdraw()
    messagebox.showinfo(subject, content)
    
    # shows depending on whatever subject, content we give    
    try:
        root.destroy()
    except:
        pass

def main():
    global width,rows,snakee,snack
    width = 500
    rows = 20
    window = pygame.display.set_mode((width,width))
    snakee = snake((0,255,0),(10,10))
    clock= pygame.time.Clock()
    snack = cube(randomSnack(rows,snakee),color="red")
    
    while True: 
        pygame.time.delay(50) ## Creating delay so the program does not run too fast
        clock.tick(10)
        snakee.move()
        if snakee.body[0].pos == snack.pos:
            snakee.addCube()
            snack = cube(randomSnack(rows,snakee),color="red")
        # check collision        
        for x in range(len(snakee.body)):
            if snakee.body[x].pos in list(map(lambda z:z.pos,snakee.body[x+1:])):
                print('Score: ', len(snakee.body))
                message_box('You Lost!','Play again...' + 'Score: ' + str(len(snakee.body)))
                snakee.reset((10,10))
                break
        
        redrawWindow(window)
main()