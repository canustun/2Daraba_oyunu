import pygame
from math import trunc
from random import choice,randint
pygame.init()

ekran=pygame.display.set_mode((600,650))
font=pygame.font.SysFont("Arial",27)

skor,kalan_can=0.1,3

fps=pygame.time.Clock()

calis=True

araba=pygame.transform.scale(pygame.image.load("araba.png"),(70,140))
karşı_araba=pygame.transform.scale(pygame.image.load("karşıyol_araba.png"),(75,140))
araba_konum,karşıyol_araba_konum,cizgi,araba_X,araba_Y=[],[],[10,180,350,520],300,510
adet_araba=4
def sıfırla():
    global araba_konum,araba_hazır_konum_Y,araba_hazır_konum_X,adet_araba
    araba_konum=[]
    araba_hazır_konum_Y=[-300,-450,-600,-750,-900,-140]
    araba_hazır_konum_X=[320,400,460,550]

    for i in range(adet_araba):
        hazır_konum_seç_Y=choice(araba_hazır_konum_Y)
        hazır_konum_seç_X=choice(araba_hazır_konum_X)
        araba_konum.append((hazır_konum_seç_X,hazır_konum_seç_Y))
        araba_hazır_konum_X.remove(hazır_konum_seç_X)
        araba_hazır_konum_Y.remove(hazır_konum_seç_Y)

def sıfırla2():
    global karşıyol_araba_konum,karşı_araba_hazır_konum_Y,karşı_araba_hazır_konum_X
    global adet_araba
    karşıyol_araba_konum=[]
    karşı_araba_hazır_konum_Y=[-300,-450,-600,-750,-900]
    karşı_araba_hazır_konum_X=[0,140,235,240,130,20]
    
    for i in range(adet_araba):
        hazır_konum_seç_Y=choice(karşı_araba_hazır_konum_Y)
        hazır_konum_seç_X=choice(karşı_araba_hazır_konum_X)
        karşıyol_araba_konum.append((hazır_konum_seç_X,hazır_konum_seç_Y))
        karşı_araba_hazır_konum_X.remove(hazır_konum_seç_X)
        karşı_araba_hazır_konum_Y.remove(hazır_konum_seç_Y)

sıfırla()
sıfırla2()
while calis:
    
    for i in range(adet_araba):
        pygame.draw.rect(ekran,(240,240,240),pygame.Rect(araba_konum[i][0]+9.2,araba_konum[i][1]+6.5,40,123),100)
        pygame.draw.rect(ekran,(240,240,240),pygame.Rect(karşıyol_araba_konum[i][0]+9.2,karşıyol_araba_konum[i][1]+6.5,47,127),100)

    hitbox2=pygame.draw.rect(ekran,(240,240,240),(araba_X+9.1,araba_Y+6.4,50,130),100)
    ekran.fill((105,105,105))
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            calis=False
            
    #yol çizgileri
    pygame.draw.rect(ekran,("white"),pygame.Rect((300,0),(20,650)))
    for i in range(3):
        pygame.draw.rect(ekran,("white"),pygame.Rect((470,cizgi[i]),(20,130)))
        pygame.draw.rect(ekran,("white"),pygame.Rect((130,cizgi[i]),(20,130)))
        cizgi[i]+=1.6
        if cizgi[i]>=520:
            cizgi[i]=0

    ekran.blit(araba,(araba_X,araba_Y))
    
    for i in range(adet_araba):
        ekran.blit(araba,araba_konum[i])
        araba_konum2=list(araba_konum[i])
        araba_konum2[1]+=1
        araba_konum[i]=araba_konum2
        if hitbox2.colliderect(araba_konum[i][0],araba_konum[i][1],70,135):
            kalan_can-=1
            sıfırla()
        ekran.blit(karşı_araba,karşıyol_araba_konum[i])
        karşıyol_araba_konum2=list(karşıyol_araba_konum[i])
        karşıyol_araba_konum2[1]+=1.5
        karşıyol_araba_konum[i]=karşıyol_araba_konum2
        if hitbox2.colliderect(karşıyol_araba_konum[i][0],karşıyol_araba_konum[i][1],70,135):
            kalan_can-=1
            sıfırla2()

    tıklama=pygame.key.get_pressed()
    if tıklama[pygame.K_LEFT] and araba_X>0:araba_X-=0.9
    
    elif tıklama[pygame.K_RIGHT] and araba_X<530:araba_X+=0.9

    if tıklama[pygame.K_UP]:
        if araba_Y>0:
            araba_Y-=0.6
            skor+=0.02
        for i in range(adet_araba):
            cizgi[i]+=1.6
            ekran.blit(araba,araba_konum[i])
            araba_konum2=list(araba_konum[i])
            araba_konum2[1]+=2
            araba_konum[i]=araba_konum2
            
            ekran.blit(karşı_araba,karşıyol_araba_konum[i])
            karşıyol_araba_konum2=list(karşıyol_araba_konum[i])
            karşıyol_araba_konum2[1]+=2
            karşıyol_araba_konum[i]=karşıyol_araba_konum2

    elif tıklama[pygame.K_DOWN]:
        if araba_Y<500:
            araba_Y+=0.6
        for i in range(adet_araba):
            cizgi[i]-=0.6
            ekran.blit(araba,araba_konum[i])
            araba_konum2=list(araba_konum[i])
            araba_konum2[1]-=2
            araba_konum[i]=araba_konum2

            karşıyol_araba_konum2=list(karşıyol_araba_konum[i])
            karşıyol_araba_konum2[1]+=1
            karşıyol_araba_konum[i]=karşıyol_araba_konum2
            
    skor+=0.01
    if araba_Y<500:araba_Y+=0.1
    if araba_X<300:skor+=0.06
    for i in range(adet_araba):
        if araba_konum[i][1]>1500:
            sıfırla()
            sıfırla()
        if karşıyol_araba_konum[i][1]>1500:
            sıfırla2()

    if kalan_can==0:
        araba_X,araba_Y=300,510
        skor,kalan_can=0.0,3
        
    ekran.blit(font.render("Skor : "+str(trunc(skor)),True,("White")),(5,0))
    ekran.blit(font.render(f"Kalan Can : {kalan_can}",True,("White")),(5,30))
    pygame.display.update()
    fps.tick(200)
