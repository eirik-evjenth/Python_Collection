import tkinter as tk
import random as r
import pyperclip as pc
from collections import defaultdict

class Wordle:
    def __init__(self, dictionary, maxGuess = 6):
        with open(dictionary) as w: 
            self.words = [i.strip() for i in w.readlines()]

        self.secretWord = r.choice(self.words)
        
        self.MAXGUESSCOUNT = maxGuess
        self.root = tk.Tk()
        self.root.title("Wordle")
        self.root.geometry("800x1000")

        self.canvas = tk.Canvas(self.root, width=800, height=1200)
        self.canvas.pack()

        self.reset()

    def reset(self): 
        self.guesses = 0
        self.word = r.choice(self.words)

        for widget in self.root.winfo_children():
            if widget != self.canvas:
                widget.destroy()

        self.createRows()
        self.createAlphabet()
        self.buffer = ""
        self.score = []
        self.letterRows = defaultdict(list)
        self.attemptedGuesses = []
        
    def checkGuess(self, guess):
        if guess == self.word:
            self.running = False
            self.win()
        else:
            self.guesses += 1
            if self.guesses >= self.MAXGUESSCOUNT:
                self.running = False
                self.lose()

    def createRows(self):
        self.rows = []
        
        for i in range(6): 
            self.rows.append([self.canvas.create_rectangle(100 + j*60, 100 + i*60, 160 + j*60, 160 + i*60, fill="white") for j in range(5)])

    def createAlphabet(self): 
        self.alphabet = []
        alphabetList = [[i for i in "qwertyuiop"], [i for i in "asdfghjkl"], [i for i in "zxcvbnm"]]

        for i in range(len(alphabetList)):
            for j in range(len(alphabetList[i])):
                button = tk.Button(self.root, text=alphabetList[i][j], font=("Arial", 24), bg="lightgrey", command=lambda letter=alphabetList[i][j]: self.addLetter(letter))
                button.place(x = 100 + j * 40, y = 475 + i*75)
                self.root.update_idletasks()
                self.alphabet.append(button)

        enterButton = tk.Button(self.root, text = "Enter", command = self.checkGuess)
        enterButton.place(x = 100 + 11 * 40, y = 475 + 2 * 75)
        backspaceButton = tk.Button(self.root, text = "<--", command = self.backspace)
        backspaceButton.place(x = 100 + 11 * 40, y = 575)

        resetButton = tk.Button(self.root, text = "Reset game", command = self.reset)
        resetButton.place(x = 100 + 11 * 40, y = 700)

    def addLetter(self, letter):
        if len(self.buffer) > 4:
            pass
        else: 
            self.buffer += letter

        self.displayGuess()

    def clear(self): 
        self.buffer = ""

    def displayGuess(self):
        for index, letter in enumerate(self.buffer): 
            label = tk.Label(self.root, text=letter, font = ("Arial", 25))
            label.place(x = 110 + index * 60, y = 110 + self.guesses * 60)
            self.letterRows[self.guesses].append(label)

    def checkGuess(self):
        if self.buffer not in self.words:
            for widget in self.letterRows[self.guesses]:
                if isinstance(widget, tk.Label):
                    widget.destroy()

            self.buffer = ""
            return
        
        self.guesses += 1
        self.attemptedGuesses.append(self.buffer)
        timesLettersFound = defaultdict(int)
        guessScore = {}

        for index, letter in enumerate(self.buffer):
            if self.secretWord[index] == letter: 
                guessScore[index] = chr(0x1F7E9)
                timesLettersFound[letter] += 1
                self.canvas.itemconfig(self.rows[self.guesses - 1][index], fill="green")

                for button in self.alphabet:
                    if button["text"] == letter:
                        button.config(bg="green")
        
        for index, letter in enumerate(self.buffer):
            if self.secretWord[index] == letter: 
                continue

            elif letter in self.secretWord and timesLettersFound[letter] < self.secretWord.count(letter):
                guessScore[index] = chr(0x01F7E8)
                timesLettersFound[letter] += 1
                self.canvas.itemconfig(self.rows[self.guesses - 1][index], fill="yellow")
                
                for button in self.alphabet:
                    if button["text"] == letter and button["bg"] != "green":
                        button.config(bg="yellow")

            else:
                guessScore[index] = chr(0x2B1B)
                self.canvas.itemconfig(self.rows[self.guesses - 1][index], fill="grey")

                for button in self.alphabet:
                    if button["text"] == letter and button["bg"] == "lightgrey":
                        button.config(bg="grey")

        sortedGuessScore = {key: guessScore[key] for key in sorted(guessScore.keys())}
        buffer = ""
        
        for i in sortedGuessScore.values(): 
            buffer += i

        self.score.append(buffer)

        if self.buffer == self.secretWord:
            self.win()

        if self.guesses == self.MAXGUESSCOUNT: 
            self.lose()

        self.buffer = ""

    def backspace(self): 
        if len(self.buffer) == 0:
            return
        
        self.buffer = self.buffer[:-1]
        
        # Clear the previous labels for the current guess
        for widget in self.letterRows[self.guesses]:
            if isinstance(widget, tk.Label):
                widget.destroy()
        self.letterRows[self.guesses] = []

        # Re-display the updated buffer
        self.displayGuess()

    def win(self): 
        self.endScreen = tk.Toplevel()
        winMessage = tk.Label(self.endScreen, text=f"Congratulations! You won in {self.guesses} guesses.")
        winMessage.grid(row = 1, columnspan=2)

        copyScoreButton = tk.Button(self.endScreen, text = "Copy score", command = self.copyScore)
        copyScoreAndWordsButton = tk.Button(self.endScreen, text = "Copy score with words", command = lambda x = False: self.copyScore(x))

        copyScoreButton.grid(row = 2, column = 0)
        copyScoreAndWordsButton.grid(row = 2, column = 1)

    def lose(self): 
        self.endScreen = tk.Toplevel()
        loseMessage = tk.Label(self.endScreen, text=f"You lost. The secret word was {self.secretWord}")
        loseMessage.grid(row = 1, columnspan=3)

        copyScoreButton = tk.Button(self.endScreen, text = "Copy score", command = self.copyScore)
        copyScoreAndWordsButton = tk.Button(self.endScreen, text = "Copy score with words", command = lambda x = False: self.copyScore(x))

        copyScoreButton.grid(row = 2, column = 1)
        copyScoreAndWordsButton.grid(row = 2, column = 2)

    def play(self):
        self.reset()
        self.root.mainloop()

    def copyScore(self, secret = True):
        buffer = ""
        
        if not secret:
            for i in self.attemptedGuesses: 
                buffer += i
                buffer += "\n"

        for i in self.score:
            buffer += i
            buffer += "\n"

        pc.copy(buffer)

if __name__ == "__main__":
    game = Wordle("words.txt")
    game.play()