from main import *

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