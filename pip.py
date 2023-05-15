import pygame

pygame.init()

W , H = 50 , 30
TILE = 20
FPS  = 60
GAME_RES = W * TILE , H * TILE 
clock = pygame.time.Clock()

grid = [pygame.Rect(x * TILE , y * TILE , TILE , TILE) for x in range(W) for y in range(H)]

x , y = 0 , 20
x1 , y1 = 0 , 0
screen = pygame.display.set_mode((GAME_RES))  
kubike = pygame.Surface((20,20))
mass = [kubike]
masLen = [[0,0]]
count = 0
truar = 0
coun,spee,limi = 0,100,2000
while True:
   
    coun += spee
    if coun >= limi:
        coun = 0
        
        x += x1
        y += y1
                
        screen.fill('black')

        kubike.fill('white')
        
        screen.blit(kubike , (x,y))
        
        def chiz(x,y):
            screen.blit(mass[truar],(x,y))
            
        if count > 1:
            for i in range(len(mass)):
                chiz(masLen[i][0],masLen[i][1])
            truar += 1
            
        if truar >= len(mass):
            truar = 0   
                    
        masLen[truar]=x,y    
        count += 1
    
    
        if x >= 1000:
            x1 = -20
        elif x <= 0:
            x1 = 20
        elif y >= 500:
            y1 = -20
        elif y <= 0:
            y1 = 20
               
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                    x1 = -20 
                    y1 = 0
            elif event.key == pygame.K_RIGHT:
                    x1 = 20
                    y1 = 0
            elif event.key == pygame.K_UP:
                    y1 = -20  
                    x1 = 0
            elif event.key == pygame.K_DOWN:
                    y1 = 20 
                    x1 = 0    
    [pygame.draw.rect(screen,(40,40,40),i_rect,1) for i_rect in grid]                   
    pygame.display.update()
    clock.tick(FPS)
     


