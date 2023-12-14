class point :
    def __init__(self,x,y,player):
        self.__coordone = x,y
        self.__player = player
        # check est sous forme de liste de booléans, avec dans l'ordre si il a été calculé de manière horizontale, verticale, diagonale ascendante, diagonale descendante en fonction de x 
        self.__check = [0]*4
        
    def getPlayer(self):
        return self.__player
    
    def getCheck(self):
        return self.__check
    
    def getCoordone(self):
        return self.__coordone
    
    def representation(self):
        color = ["dark","blue","red"]
        return color[self.__player]
    
class fonctionnement:

    def __init__(self,n,p):
        self.__size = n
        self.__nbrPion = p
        self.__board= self.newBoard()
        self.__player = 1

    def newBoard(self):
        return [[point(x,y,0) for x in range(self.__size)] for y in range(self.__size)]
    
    def display(self):
        for y in range(self.__size):
            print()
            for x in range(self.__size):
                print(self.__board[y][x].representation(),end=" ")
    
    def alignement(self,coordonne):
        x,y= coordonne
        compteur = 0
        a,b = x,x
        while (a+1<= n and self.__board[y][a+1].getPlayer()==self.__player) or (b-1>=0 and self.__board[y][b-1].getPlayer()==self.__player):
            compteur +=1
            if compteur >= self.__nbrPion-1 :
                return True
            elif (a+1<= n and self.__board[y][a+1].getPlayer()==self.__player)
                a+=1
            else :
                b-=1
        compteur=0
                

class gui :
    pass

t = fonctionnement(10,5)
