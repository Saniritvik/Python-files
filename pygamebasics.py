import pygame
pygame.init() #Initialise a pygame window by calling constructor
window = pygame.display.set_mode((400,400),pygame.RESIZABLE) # Creating a window of size (200,200)
pygame.display.set_caption("Game testing")
window.fill((255,255,255)) # (R,g,b) 
x=True
# while x:
#     pygame.display.flip()
#     for event in pygame.event.get(): #To work with events
#         if event.type==pygame.QUIT: #Handling close button
#             x=False
#     # Rectangle -x,y,w,h
#     pygame.draw.rect(window,(0,0,255),[0,0,100,100],3)
#     # Parameter 1-screen 2-color of shape 3=[x,y,w,h] optional-filling in shape-default 0 solid
#     pygame.draw.line(window,(255,0,0),[100,100],[0,0],8)
#     pygame.draw.line(window,(0,0,255),[100,0],[0,100],8)
#     # Line parameter 1-screen color of line 3-[x1,y1] 4-[x2.y2] optional-thickness of line -0 defualt thin line
# pygame.quit()

# while x:
#     pygame.display.flip()
#     for event in pygame.event.get(): #To work with events
#         if event.type==pygame.QUIT: #Handling close button
#             x=False
#         pygame.draw.circle(window,(0,0,255),(0,0),70,1)
#         pygame.draw.polygon(window,(0,0,255),[[100,100],[100,200],[200,200],[200,100],[150,50]],5)
#         pygame.draw.rect(window,(0,0,255),(125,170,50,30),2)
#         pygame.draw.rect(window,(0,0,255),(150,100,35,35),2)
# pygame.quit()

# while x:
#     pygame.display.flip()
#     for event in pygame.event.get(): #To work with events
#         if event.type==pygame.QUIT: #Handling close button
#             x=False
#         if event.type == pygame.MOUSEBUTTONDOWN: 
#             x = event.pos[0]
#             y = event.pos[1]
#             pygame.draw.rect(window,(0,0,255),[x,y,50,25],1)
# pygame.quit()

while x:
    pygame.display.flip()
    for event in pygame.event.get(): #To work with events
        if event.type==pygame.QUIT: #Handling close button
            x=False
        s1=pygame.Surface((20,20))
        s1.fill((0,0,0))
        window.blit(s1,(300,200))
pygame.quit()