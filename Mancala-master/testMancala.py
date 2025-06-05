from random import *
from graphics import *

x = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]

class Mancala:
    def __init__(self):
        #self.board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] this was a test
        self.board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
        self.win = GraphWin("Mancala", 1700, 500)

    def intro(self):

        x = Text(Point(750,250), 'Mancala is an ancient game played all around the world with many variations \n Archeological and Historical evidence dates Mancala to the Aksumite Empire in 700 A.D. \n But the oldest boards that resemble Mancala boards were found in An Ghazal, Jordan \n It is believed that Arab traders are the reason why Mancala spread throughout Africa \n In fact, the name Mancala comes from the Arabic word nakala, which means to transport \n However, throughout the world, the game has different names \n For example in my own language, Afaan Oromoo, we call Mancala “Bulto” \n')
        x.setSize(25)
        x.setFill("black")
        x.draw(self.win)
        self.win.getMouse()

        x.undraw()
        y = Text(Point(750,250), 'Now as mentioned before, Mancala has many different variations \n The one you will be playing in this game is the one that was taught to me by my family \n In this version of Mancala, you pick any pocket to start with from your side of the board. \n From the pocket, you start with, you take all the stones from that hole, and in a circular motion, you drop one stone into each pocket that follows the original pocket you picked in a counterclockwise direction. \n You do this until you run out of stones in your hands. \n If you landed in your own Mancala, you get to go again picking any pocket you want that still has stones in it. \n If you instead landed on a pocket with stones inside them, you pick up the remaining stones in that pocket and continue going on and on until there are no stones left in the pockets.')
        y.setSize(10)
        y.setFill("black")
        y.draw(self.win)
        self.win.getMouse()

        y.undraw()
        z = Text(Point(750,250), 'To pick a pocket to start from, just click the pocket you want with your mouth. \n Now are you ready to start?')
        z.setSize(25)
        z.setFill("black")
        z.draw(self.win)
        self.win.getMouse()
        
        z.undraw()

        vpocket = Oval(Point(200,100), Point(300,200))
        vpocket11 = vpocket.clone()
        vpocket12 = vpocket11.clone()
        vpocket12.move(200,0)
        vpocket13 = vpocket12.clone()
        vpocket13.move(200,0)
        vpocket14 = vpocket13.clone()
        vpocket14.move(200,0)
        vpocket15 = vpocket14.clone()
        vpocket15.move(200,0)
        vpocket16 = vpocket15.clone()
        vpocket16.move(200,0)
        vpocket21 = vpocket11.clone()
        vpocket21.move(0,200)
        vpocket22 = vpocket12.clone()
        vpocket22.move(0,200)
        vpocket23 = vpocket13.clone()
        vpocket23.move(0,200)
        vpocket24 = vpocket14.clone()
        vpocket24.move(0,200)
        vpocket25 = vpocket15.clone()
        vpocket25.move(0,200)
        vpocket26 = vpocket16.clone()
        vpocket26.move(0,200)
        vmancala1 = Oval(Point(0,100),Point(100,400))
        vmancala2 = vmancala1.clone()
        vmancala2.move(1400,0)

        vpocket11.draw(self.win)
        vpocket12.draw(self.win)
        vpocket13.draw(self.win)
        vpocket14.draw(self.win)
        vpocket15.draw(self.win)
        vpocket16.draw(self.win)
        vpocket21.draw(self.win)
        vpocket22.draw(self.win)
        vpocket23.draw(self.win)
        vpocket24.draw(self.win)
        vpocket25.draw(self.win)
        vpocket26.draw(self.win)
        vmancala1.draw(self.win)
        vmancala2.draw(self.win)

    def makePlayable(self, nextMove):
        if nextMove >= 0 and nextMove <= 13:
            nextMove = nextMove
        elif nextMove > 13:
            while nextMove > 13:
                nextMove = nextMove - 14
        else:
            while nextMove < 0:
                nextMove = nextMove +14
        return nextMove

    def compMoveMaker(self):
        b = [1,2,3,4,5,6,8,9,10,11,12,13,]
        x = choice(b)
        while self.board[x] < 1:
            x = choice(b)
        return x

    def click2list(self, vpoint):
        if 100 <= vpoint.getY() <= 200:
            if 0 <= vpoint.getX() <= 100:
                return 7
            if 200 <= vpoint.getX() <= 300:
                return 6
            if 400 <= vpoint.getX() <= 500:
                return 5
            if 600 <= vpoint.getX() <= 700:
                return 4
            if 800 <= vpoint.getX() <= 900:
                return 3
            if 1000 <= vpoint.getX() <= 1100:
                return 2
            if 1200 <= vpoint.getX() <= 1300:
                return 1
            if 1400 <= vpoint.getX() <= 1500:
                return 0 
            else:
                return False
        if 300 <= vpoint.getY() <= 400:
            if 0 <= vpoint.getX() <= 100:
                return 7
            if 200 <= vpoint.getX() <= 300:
                return 8
            if 400 <= vpoint.getX() <= 500:
                return 9
            if 600 <= vpoint.getX() <= 700:
                return 10
            if 800 <= vpoint.getX() <= 900:
                return 11
            if 1000 <= vpoint.getX() <= 1100:
                return 12
            if 1200 <= vpoint.getX() <= 1300:
                return 13
            if 1400 <= vpoint.getX() <= 1500:
                return 0
            else:
                return False
        if 100 <= vpoint.getY() <= 400:
            if 0 <= vpoint.getX() <= 100:
                return 7
            if 1400 <= vpoint.getX() <= 1500:
                return 0
            else:
                return False
        else:
            return False
    
    def drawStones(self):
        x = self.board
        
        z = Circle(Point(1450,250),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(1450,250), str(x[0]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(1250,350),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(1250,350), str(x[13]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(1050,350),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(1050,350), str(x[12]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(850,350),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(850,350), str(x[11]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(650,350),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(650,350), str(x[10]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(450,350),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(450,350), str(x[9]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(250,350),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(250,350), str(x[8]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(50,250),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(50,250), str(x[7]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(250,150),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(250,150), str(x[6]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(450,150),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(450,150), str(x[5]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(650,150),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(650,150), str(x[4]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(850,150),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(850,150), str(x[3]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(1050,150),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(1050,150), str(x[2]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

        z = Circle(Point(1250,150),49)
        z.setFill("white")
        z.draw(self.win)
        y = Text(Point(1250,150), str(x[1]))
        y.setSize(25)
        y.setFill("black")
        y.draw(self.win)

    def human1Play(self):
        if self.gameover() == True:
            return
        turnrect = Rectangle(Point(0,475),Point(1700,500))
        turnrect.setFill("blue")
        turnrect.draw(self.win)
        self.drawStones()
        firstMess = Text(Point(750,475), "Pick a pocket to start from!")
        firstMess.setSize(15)
        firstMess.setFill("black")
        firstMess.draw(self.win)
        if self.gameover == True:
            return
        lastPocket = self.click2list(self.win.getMouse())
        while lastPocket == False:
            lastPocket = self.click2list(self.win.getMouse())
        lastPocket = self.makePlayable(lastPocket)
        errorFor1 = False
        if self.board[lastPocket] == 1:
            errorFor1 = True
        firstMess.undraw()
        while lastPocket == 0 or lastPocket == 7 or self.board[lastPocket] == 0:
            if self.gameover() == True:
                return
            secondMess = Text(Point(750,475), "Pick again! You can not pick a Mancala to start from or a pocket with zero stones")
            secondMess.setSize(15)
            secondMess.setFill("black")
            secondMess.draw(self.win)
            if self.gameover == True:
                return
            lastPocket = self.click2list(self.win.getMouse())
            while lastPocket == False:
                lastPocket = self.click2list(self.win.getMouse())
            lastPocket = self.makePlayable(lastPocket)
            secondMess.undraw()
        while self.board[lastPocket] != 1 or errorFor1 == True:
            if self.gameover() == True:
                return
            errorFor1 = False
            moves = int(self.board[int(lastPocket)])
            self.board[lastPocket] = 0
            while moves > 0:
                lastPocket = lastPocket + 1
                lastPocket = self.makePlayable(lastPocket)
                if lastPocket == 7:
                    lastPocket = lastPocket + 1
                self.board[lastPocket] = self.board[lastPocket] + 1
                moves = moves - 1
            self.drawStones()
            self.win.getMouse()
            if lastPocket == 0:
                if self.gameover() == True:
                    return
                thirdMess = Text(Point(750,475), "You landed in your Mancala! Pick anywhere on the board, that isn't a mancala to play again from!")
                thirdMess.setSize(15)
                thirdMess.setFill("black")
                thirdMess.draw(self.win)
                if self.gameover == True:
                    return
                lastPocket = self.click2list(self.win.getMouse())
                while lastPocket == False:
                    lastPocket = self.click2list(self.win.getMouse())
                lastPocket = self.makePlayable(lastPocket)
                if self.board[lastPocket] == 1:
                    errorFor1 = True
                thirdMess.undraw()
                while lastPocket == 0 or lastPocket == 7:
                    if self.gameover() == True:
                        return
                    fourthMess = Text(Point(750,475), "You can not start from a Mancala or out of the index! Please select another pocket to play from!")
                    fourthMess.setSize(15)
                    fourthMess.setFill("black")
                    fourthMess.draw(self.win)
                    if self.gameover == True:
                        return
                    lastPocket = self.click2list(self.win.getMouse())
                    while lastPocket == False:
                        lastPocket = self.click2list(self.win.getMouse())
                    lastPocket = self.makePlayable(lastPocket)
                    if self.board[lastPocket] == 1:
                        errorFor1 = True
                    fourthMess.undraw()
                if self.gameover() == True:
                    return
                
        fifthMess = Text(Point(750,475), "Your turn is over!")
        fifthMess.setSize(15)
        fifthMess.setFill("black")
        fifthMess.draw(self.win)
        self.win.getMouse()        
        fifthMess.undraw()
        turnrect.undraw()

    def human2Play(self):
        if self.gameover() == True:
            return 
        turnrect = Rectangle(Point(0,0),Point(1700,50))
        turnrect.setFill("red")
        turnrect.draw(self.win)
        self.drawStones()
        firstMess = Text(Point(750,25), "Pick a pocket to start from!")
        firstMess.setSize(15)
        firstMess.setFill("black")
        firstMess.draw(self.win)
        if self.gameover == True:
            return
        lastPocket = self.click2list(self.win.getMouse())
        while lastPocket == False:
            lastPocket = self.click2list(self.win.getMouse())
        lastPocket = self.makePlayable(lastPocket)
        errorFor1 = False
        if self.board[lastPocket] == 1:
            errorFor1 = True
        firstMess.undraw()
        if self.gameover() == True:
            return 
        while lastPocket == 0 or lastPocket == 7 or self.board[lastPocket] == 0:
            if self.gameover() == True:
                return
            secondMess = Text(Point(750,25), "Pick again! You can not pick a Mancala to start from or a pocket with zero stones")
            secondMess.setSize(15)
            secondMess.setFill("black")
            secondMess.draw(self.win)
            if self.gameover == True:
                return
            lastPocket = self.click2list(self.win.getMouse())
            while lastPocket == False:
                lastPocket = self.click2list(self.win.getMouse())
            lastPocket = self.makePlayable(lastPocket)
            secondMess.undraw()
        while self.board[lastPocket] != 1 or errorFor1 == True:
            errorFor1 = False
            moves = int(self.board[int(lastPocket)])
            self.board[lastPocket] = 0
            while moves > 0:
                lastPocket = lastPocket + 1
                lastPocket = self.makePlayable(lastPocket)
                if lastPocket == 0:
                    lastPocket = lastPocket + 1
                self.board[lastPocket] = self.board[lastPocket] + 1
                moves = moves - 1
            if self.gameover() == True:
                return
            self.drawStones()
            self.win.getMouse()
            if lastPocket == 7:
                thirdMess = Text(Point(750,25), "You landed in your Mancala! Pick anywhere on the board, that isn't a mancala to play again from!")
                thirdMess.setSize(15)
                thirdMess.setFill("black")
                thirdMess.draw(self.win)
                if self.gameover == True:
                    return
                lastPocket = self.click2list(self.win.getMouse())
                if self.gameover() == True:
                    return
                while lastPocket == False:
                    lastPocket = self.click2list(self.win.getMouse())
                lastPocket = self.makePlayable(lastPocket)
                if self.board[lastPocket] == 1:
                    errorFor1 = True
                thirdMess.undraw()
                while lastPocket == 0 or lastPocket == 7:
                    fourthMess = Text(Point(750,475), "You can not start from a Mancala or out of the index! Please select another pocket to play from!")
                    fourthMess.setSize(15)
                    fourthMess.setFill("black")
                    fourthMess.draw(self.win)
                    if self.gameover == True:
                        return
                    lastPocket = self.click2list(self.win.getMouse())
                    while lastPocket == False:
                        lastPocket = self.click2list(self.win.getMouse())
                    lastPocket = self.makePlayable(lastPocket)
                    if self.board[lastPocket] == 1:
                        errorFor1 = True
                    fourthMess.undraw()
                if self.gameover() == True:
                    return
                
        fifthMess = Text(Point(750,25), "Your turn is over!")
        fifthMess.setSize(15)
        fifthMess.setFill("black")
        fifthMess.draw(self.win)
        self.win.getMouse()        
        fifthMess.undraw()
        turnrect.undraw()

    def comp2Play(self):
        if self.gameover() == True:
            return
        turnrect = Rectangle(Point(0,0),Point(1700,50))
        turnrect.setFill("red")
        turnrect.draw(self.win)
        self.drawStones()
        firstMess = Text(Point(750,25), "Pick a pocket to start from!")
        firstMess.setSize(15)
        firstMess.setFill("black")
        firstMess.draw(self.win)
        self.win.getMouse()
        firstMess.undraw()
        if self.gameover == True:
            return
        lastPocket = self.compMoveMaker()
        comp1Mess = Text(Point(750,25), "I pick the " + str(lastPocket) + "th " + "pocket!")
        comp1Mess.setSize(15)
        comp1Mess.setFill("black")
        comp1Mess.draw(self.win)
        self.win.getMouse()
        comp1Mess.undraw()
        errorFor1 = False
        if self.board[lastPocket] == 1:
            errorFor1 = True
        
        while self.board[lastPocket] != 1 or errorFor1 == True:
            if self.gameover() == True:
                return 
            errorFor1 = False
            moves = int(self.board[int(lastPocket)])
            self.board[lastPocket] = 0
            while moves > 0:
                if self.gameover == True:
                    return
                lastPocket = lastPocket + 1
                lastPocket = self.makePlayable(lastPocket)
                if lastPocket == 0:
                    lastPocket = lastPocket + 1
                self.board[lastPocket] = self.board[lastPocket] + 1
                moves = moves - 1
            self.drawStones()
            self.win.getMouse()
            if lastPocket == 7:
                thirdMess = Text(Point(750,25), "You landed in your Mancala! Pick anywhere on the board, that isn't a mancala to play again from!")
                thirdMess.setSize(15)
                thirdMess.setFill("black")
                thirdMess.draw(self.win)
                if self.gameover == True:
                    return
                lastPocket = self.compMoveMaker()
                lastPocket = self.makePlayable(lastPocket)
                if self.board[lastPocket] == 1:
                    errorFor1 = True
                thirdMess.undraw()
        
        turnrect.undraw()

    def gameover(self):
        count = 0
        for x in range(1,7):
            if self.board[x] == 0:
                count = count + 1
        for x in range(1,7):
            if self.board[x] == 0:
                count = count + 1
        if count >= 12:
            return True
        else:
            return False

    def whoWon(self):
        if self.board[0] > self.board[7]:
            zed = Text(Point(750,250), "Player 1 wins!")
            zed.setSize(15)
            zed.setFill("black")
            zed.draw(self.win)
            print("Player 1 wins")
        elif self.board[7] > self.board[0]:
            zed = Text(Point(750,250), "player 2 wins!")
            zed.setSize(15)
            zed.setFill("black")
            zed.draw(self.win)
            print("Player 2 wins")
        else:
            zed = Text(Point(750,250),"It's a TIE!")
            zed.setSize(15)
            zed.setFill("black")
            zed.draw(self.win)
            print("It's a tie!")

        self.win.close()

x = Mancala()
y = input("Do you want to play with a friend or a computer? (input F for friend and C for computer)")
if y == "F":
    x.intro()
    while x.gameover() == False:
        x.human1Play()
        if x.gameover() == True:
            break
        else:
            x.human2Play()
if y == "C":
    x.intro()
    while x.gameover() == False:
        x.human1Play()
        if x.gameover() == True:
            break
        else:
            x.comp2Play()

x.whoWon()

print("The game is over")
