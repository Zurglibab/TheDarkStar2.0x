from tkinter import *

class point :
    def __init__(self,x,y,etat):
        self.__coordone = x,y
        # etat est une liste, [numéro du player, état du pion], 0 est le pion et 1 est l'ancien emplacement
        self.__etat = etat
        
    def getEtat(self):
        return self.__etat
    
    def setEtat(self, etat):
        self.__etat = etat
    
    def getCoordone(self):
        return self.__coordone
    
    def couleurs(self):
        color = ["black","blue","red"]
        return color[self.__etat[0]]
    
class fonctionnement:

    def __init__(self,n,p):
        self.__size = n
        self.__nbrPion = p
        self.__board= self.newBoard()
        self.__board[2][2].setEtat([1,0])
        self.__board[5][2].setEtat([2,0])
        self.__player = 1
        self.__compteur=0 
        self.__couleurBase  = 'black'
        self.__pion1 = [-1,-1]
        self.__pion2 = [-1,-1]
    
    def getBoard(self):
        return self.__board
    
    def getPlayer(self):
        return self.__player
    
    def setPlayer(self, player):
        self.__player = player

    def newBoard(self):
        return [[point(x,y,[0,-1]) for x in range(self.__size)] for y in range(self.__size)]
    
    def alignement(self, x, y):
        self.__compteur = 0
        a,b = x,x-1
        # vérfication pour chaque ligne
        while (a+1<= self.__size and self.__board[y][a+1].getEtat()==[self.__player,1]) or (b-1>=0 and self.__board[y][b-1].getEtat()==[self.__player,1]):
            print("5")
            self.__compteur +=1
            if self.__compteur >= self.__nbrPion-1 :
                return True
            elif (a+1<= self.__size and self.__board[y][a+1].getEtat()==[self.__player,1]) :
                a+=1
            else :
                b-=1
        self.__compteur=0
        
        # vérification pour chaque colonne
        a,b=y,y-1
        while (a+1<= self.__size and self.__board[a+1][x].getEtat()==[self.__player,1]) or (b-1>=0 and self.__board[b-1][x].getEtat()==[self.__player,1]):
            self.__compteur +=1
            if self.__compteur >= self.__nbrPion-1 :
                return True
            elif (a+1<= self.__size and self.__board[a+1][x].getEtat()==[self.__player,1]) :
                a+=1
            else :
                b-=1
        self.__compteur = 0
        
        # vérification diagonale ascendante
        a,b=1,1
        while (x+a<= self.__size and y-a<= self.__size and self.__board[y-a][x+a].getEtat()==[self.__player,1]) or (x-b>=0 and y+b>=0 and self.__board[y+b][x-b].getEtat()==[self.__player,1]):
            self.__compteur +=1
            print("7")
            if self.__compteur >= self.__nbrPion-1 :
                return True
            elif x+a<= self.__size and y-a<= self.__size and self.__board[y-a][x+a].getEtat()==[self.__player,1] :
                a+=1
            else :
                b+=1
        self.__compteur = 0        
        # vérification diagonale descendante
        a,b=1,-1
        while (x+a<= self.__size and y+a<= self.__size and self.__board[y+a][x+a].getEtat()==[self.__player,1]) or (x+b>=0 and y+b>=0 and self.__board[y+b][x+b].getEtat()==[self.__player,1]):
            self.__compteur +=1
            print("8")
            if self.__compteur >= self.__nbrPion-1 :
                return True
            elif x<= self.__size and y+a<= self.__size and self.__board[y+a][x+a].getEtat()==[self.__player,1] :
                a+=1
            else :
                b-=1
        self.__compteur = 0
        
        return False
        
    def possible(self, x,y):
        """
        Vérifie toute les cases vides autour de la case x,y
        Si aucune case est vide renvoie False
        Sinon renvoie la liste de toutes les coordonées de possible 
        """
        liste1, liste2 = [-1, 1], [-2, 2]
        res= []
        for i in liste1:
            for j in liste2:
                 if 0 <= x+i < self.__size and 0 <= y+j < self.__size and self.__board[y+j][x+i].getEtat() == [self.__player,0]:
                     res.append([x+i,y+j])
                 elif 0 <= x+j < self.__size and 0 <= y+i < self.__size and self.__board[y+i][x+j].getEtat() == [self.__player,0]:
                     res.append([x+j,y+i])
        return False
   
    def move(self, x, y):
        if self.possible(x, y)!= False:
            i, j = self.possible(x,y)
            self.__board[j][i].setEtat([self.__player,1])
            self.__board[y][x].setEtat([self.__player,0])
            return True
        return False
    
    def again(self):
        for y in range(self.__size):
            for x in range(self.__size):
                if self.__board[y][x].getEtat() == [self.__player, 1]:
                    if self.alignement(x, y):
                        print("1")
                        return False
                if self.__board[y][x].getEtat() == [self.__player, 0]:
                    for j in range(-1,2,2):
                        for i in range(-2,3,4):
                            if 0 <= x+i < self.__size and 0 <= y+j < self.__size and self.__board[y+j][x+i].getEtat() == [0,-1]:
                                print("2")
                                return True
                            elif 0 <= x+j < self.__size and 0 <= y+i < self.__size and self.__board[y+i][x+j].getEtat() == [0,-1]:
                                print("3")
                                return True         
        return False    
                
class gui :
    def __init__(self, n):
        self.__size = n
        self.__board = fonctionnement(15,5)
        self.__root = Tk()
        self.__root.title("Game")   
        self.__root.resizable(False,False)
        
        self.__frame1 = Frame(self.__root)
        self.__frame1.grid(row=0, column=0, rowspan=2)
        self.__frame1.config(height = self.__size*50+1, width = self.__size*50+1,highlightthickness=0, bd=0, bg="black", padx=50, pady=50)
        
        self.__canvas = Canvas(self.__frame1)
        self.__canvas.config(width = self.__size*50+1, height = self.__size*50+1 ,highlightthickness=0, bd=0, bg="black")
        self.__canvas.bind('<Button-1>',self.click)
        self.__canvas.pack()
        
        self.__playerNum = StringVar()
        self.__textPlayer = Label(self.__frame1, textvariable=self.__playerNum,width=30)
        self.__textPlayer.pack(pady = 10)
        self.updateLabels()
        self.display()
        
        self.__root.mainloop()
    
    def update(self):
        self.display()
        if self.__board.again():
            self.__board.setPlayer(3-self.__board.getPlayer())
            self.updateLabels()
        else:
            print('Fin')

    def updateLabels(self):
        self.__playerNum.set('Player : {}'.format(self.__board.getPlayer()))
    
    def click(self, event):
        x = event.x // 50
        y = event.y // 50
        if self.__board.move(x,y):
            self.update()
            
    def display(self):
        self.__canvas.delete("all")
        for y in range(self.__size):
            for x in range(self.__size):
                self.__case = self.__canvas.create_rectangle(x*50, y*50,(x+1)*50,(y+1)*50, fill = "Black", outline = 'white')
                if self.__board.getBoard()[y][x].getEtat()[1] == 0:
                    self.__canvas.create_oval(x*50+10,y*50+10,(x+1)*50-10,(y+1)*50-10, fill=self.__board.getBoard()[y][x].couleurs(), outline = "white")
                elif self.__board.getBoard()[y][x].getEtat()[1] == 1:
                    self.__canvas.create_line(x*50+10,y*50+10,(x+1)*50-10,(y+1)*50-10, fill=self.__board.getBoard()[y][x].couleurs(), width = 4) 
                    self.__canvas.create_line(x*50+10,(y+1)*50-10,(x+1)*50-10,y*50+10, fill=self.__board.getBoard()[y][x].couleurs(), width = 4)
        self.__canvas.update()

