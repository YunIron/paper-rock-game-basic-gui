from os import write
from tkinter import *
from tkinter import font

class paperTk():
    def __init__(self):
        self.os = __import__("os")
        self.time = __import__("time")
        self.random = __import__("random")
        tkinter = __import__("tkinter")
        self.gui = tkinter.Tk()
        self.gui.title("Paper Rock Game")
        self.guipencere = Frame(self.gui)
        self.guipencere.grid()
        self.PlayerScore = 0
        self.AIScore = 0
        self.gameNumber = 0
        self.Pchoice = ""
        if self.os.path.exists("bestscore.txt"):
            with open("bestscore.txt","r",encoding="utf-8") as file:
                file.seek(0)
                text = file.readline(1)
                self.bestScore = text
        else:
            with open("bestscore.txt","w",encoding="utf-8") as file:
                file.seek(0)
                file.write("0")
                self.bestScore = "0"
        self.login()
        self.gui.mainloop()

    def login(self):
        global Loglabel
        global LogScore
        global ButtonPlay
        self.gui.geometry("600x300")
        Loglabel = Label(self.guipencere, text="Paper and Rock Game", font=50)
        Loglabel.pack(side=TOP, padx=230)
        LogScore = Label(self.guipencere, text=f"Best Score : {self.bestScore}", font=10)
        LogScore.pack(side=TOP, padx=230, pady=20)
        ButtonPlay = Button(self.guipencere, text="Play", font=10, command=self.gamePanel)
        ButtonPlay.pack(side=BOTTOM, padx=100, pady=30)

    def logdestroy(self):
        Loglabel.destroy()
        LogScore.destroy()
        ButtonPlay.destroy()

    def addBestScore(self):
        with open("bestscore.txt","r",encoding="utf-8") as file:
                file.seek(0)
                text = file.readline(1)
                self.bestScore = text
                if int(self.bestScore) < self.PlayerScore:
                    with open("bestscore.txt","w",encoding="utf-8") as file:
                        file.seek(0)
                        file.write(str(self.PlayerScore))

    def gamePanel(self):
        self.logdestroy()
        self.addBestScore()
        global PlayerScore
        global AIScore
        global PlayerScoreL
        global AIScoreL
        global StartButton
        global backToLogin
        global backPanel
        self.gui.geometry("300x200")
        PlayerScoreL = Label(self.guipencere, text=F"Your Score : {str(self.PlayerScore)}", font=10)
        PlayerScoreL.place(x=100)
        AIScoreL = Label(self.guipencere, text=F"AI Score : {str(self.AIScore)}", font= 10)
        AIScoreL.place(x=100, y=50)
        StartButton = Button(self.guipencere, text="Start", font=10, command=self.StartPanel)
        StartButton.place(x=120, y=100)
        if self.gameNumber == 0:
            backToLogin = Button(self.guipencere, text="Back", font=20, command=self.backToLog)
            backToLogin.place(x=200, y=150)
        if self.gameNumber > 0:
            backPanel = Button(self.guipencere, text="Back", font=20, command=self.backToPanel)
            backPanel.place(x=200, y=150)
        self.time.sleep(0.30)

    def StartPanel(self):
        global TasButton
        global KagitButton
        global MakasButton
        StartButton.destroy()
        AIScoreL.destroy()
        PlayerScoreL.destroy()
        if self.gameNumber > 0:
            PlayerLabel.destroy()
            AILabel.destroy()
            Result.destroy()
            backToLogin.destroy()
            backPanel.destroy()
        self.gameNumber += 1
        TasButton = Button(self.guipencere, text="Tas", font=10, command=self.Tas)
        TasButton.place(x=30, y=100)
        KagitButton = Button(self.guipencere, text="Kagit", font=10, command=self.Kagit)
        KagitButton.place(x=200, y=100)
        MakasButton = Button(self.guipencere, text="Makas", font=10, command=self.Makas)
        MakasButton.place(x=110, y=100)

    def backToPanel(self):
        if self.gameNumber > 0:
            self.destroyButton()
            PlayerLabel.destroy()
            AILabel.destroy()
            Result.destroy()
        self.destroyButton()
        PlayerScoreL.destroy()
        AIScoreL.destroy()
        backToLogin.destroy()
        StartButton.destroy()
        self.gameNumber = 0
        backToLogin.destroy()
        backPanel.destroy()
        self.gamePanel()

    def backToLog(self):
        if self.gameNumber > 0:
            self.destroyButton()
            PlayerLabel.destroy()
            AILabel.destroy()
            Result.destroy()
        self.destroyButton()
        PlayerScoreL.destroy()
        AIScoreL.destroy()
        backToLogin.destroy()
        StartButton.destroy()
        self.login()

    def Tas(self):
        self.Pchoice = "Tas"
        self.Game()
        self.gamePanel()

    def Kagit(self):
        self.Pchoice = "Kagit"
        self.Game()
        self.gamePanel()

    def Makas(self):
        self.Pchoice = "Makas"
        self.Game()
        self.gamePanel()
        

    def destroyButton(self):
        TasButton.destroy()
        KagitButton.destroy()
        MakasButton.destroy()

    def Game(self):
        global clist
        global cRandom
        global PlayerLabel
        global AILabel
        global Result
        clist = ["Tas", "Kagit", "Makas"]
        cRandom = self.random.choice(clist)
        self.destroyButton()
        if self.Pchoice == "Tas":
            if cRandom == "Tas":
                PlayerLabel = Label(self.guipencere, text=F"Your : {self.Pchoice}")
                PlayerLabel.place(x=20, y=130)
                AILabel = Label(self.guipencere, text=F"AI : {cRandom}")
                AILabel.place(x=20, y=145)
                Result = Label(self.guipencere, text=F"Draw!")
                Result.place(x=100, y=135)
                self.time.sleep(0.5)

            elif cRandom == "Kagit":
                PlayerLabel = Label(self.guipencere, text=F"Your : {self.Pchoice}")
                PlayerLabel.place(x=100, y=20)
                AILabel = Label(self.guipencere, text=F"AI : {cRandom}")
                AILabel.place(x=100, y=70)
                Result = Label(self.guipencere, text=F"AI is won!", font=20)
                Result.place(x=100, y=130)
                self.AIScore += 1
                self.time.sleep(0.5)

            else:
                PlayerLabel = Label(self.guipencere, text=F"Your : {self.Pchoice}")
                PlayerLabel.place(x=100, y=20)
                AILabel = Label(self.guipencere, text=F"AI : {cRandom}")
                AILabel.place(x=100, y=70)
                Result = Label(self.guipencere, text=F"Player is won!", font=20)
                Result.place(x=100, y=130)
                self.PlayerScore += 1
                self.time.sleep(0.5)


        elif self.Pchoice == "Kagit":
            if cRandom == "Kagit":
                PlayerLabel = Label(self.guipencere, text=F"Your : {self.Pchoice}")
                PlayerLabel.place(x=100, y=20)
                AILabel = Label(self.guipencere, text=F"AI : {cRandom}")
                AILabel.place(x=100, y=70)
                Result = Label(self.guipencere, text=F"Draw!", font=20)
                Result.place(x=110, y=130)
                self.time.sleep(0.5)

            elif cRandom == "Makas":
                PlayerLabel = Label(self.guipencere, text=F"Your : {self.Pchoice}")
                PlayerLabel.place(x=100, y=20)
                AILabel = Label(self.guipencere, text=F"AI : {cRandom}")
                AILabel.place(x=100, y=70)
                Result = Label(self.guipencere, text=F"AI is won!", font=20)
                Result.place(x=110, y=130)
                self.AIScore += 1
                self.time.sleep(0.5)

            else:
                PlayerLabel = Label(self.guipencere, text=F"Your : {self.Pchoice}")
                PlayerLabel.place(x=100, y=20)
                AILabel = Label(self.guipencere, text=F"AI : {cRandom}")
                AILabel.place(x=100, y=70)
                Result = Label(self.guipencere, text=F"Player is won!",font=20)
                Result.place(x=110, y=130)
                self.PlayerScore += 1
                self.time.sleep(0.5)


        elif self.Pchoice == "Makas":
            if cRandom == "Makas":
                PlayerLabel = Label(self.guipencere, text=F"Your : {self.Pchoice}")
                PlayerLabel.place(x=100, y=20)
                AILabel = Label(self.guipencere, text=F"AI : {cRandom}")
                AILabel.place(x=100, y=70)
                Result = Label(self.guipencere, text=F"Draw!", font=20)
                Result.place(x=110, y=130)
                self.time.sleep(0.5)

            elif cRandom == "Tas":
                PlayerLabel = Label(self.guipencere, text=F"Your : {self.Pchoice}")
                PlayerLabel.place(x=100, y=20)
                AILabel = Label(self.guipencere, text=F"AI : {cRandom}")
                AILabel.place(x=100, y=70)
                Result = Label(self.guipencere, text=F"AI is won!",font=20)
                Result.place(x=110, y=130)
                self.AIScore += 1
                self.time.sleep(0.5)
            else:
                PlayerLabel = Label(self.guipencere, text=F"Your : {self.Pchoice}")
                PlayerLabel.place(x=100, y=20)
                AILabel = Label(self.guipencere, text=F"AI : {cRandom}")
                AILabel.place(x=100, y=70)
                Result = Label(self.guipencere, text=F"Player is won!",font=20)
                Result.place(x=110, y=130)
                self.PlayerScore += 1
                self.time.sleep(0.5)
        else:
            pass

paperTk()