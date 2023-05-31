import random
from customtkinter import CTk ,CTkLabel, CTkEntry, CTkButton

words = ["vidro","local","grave"]

class mensagemtexto:
    def __init__(self, master, title, message):
        self.master = master
        self.master.title(title)
        self.label = CTkLabel(self.master, text=message, width=300, height=100)
        self.label.pack()
        self.ok_button = CTkButton(self.master, text="OK", command=self.master.destroy)
        self.ok_button.pack()

class Termo:
    def __init__(self, master):
        self.master = master
        self.master.title("Termo")
        self.word = random.choice(words)
        self.guesses = []
        self.menu()

    def menu(self):
        self.label = CTkLabel(self.master, text="Advinhe a palavra:")
        self.label.pack()

        self.entry = CTkEntry(self.master)
        self.entry.pack()

        self.button = CTkButton(self.master, text="Advinhar", command=self.advinhar)
        self.button.pack()

    def advinhar(self):
        guess = self.entry.get()
        self.guesses.append(guess)

        if guess == self.word:
            message = f"Parabens! Voce advinhou a palavra '{self.word}' em {len(self.guesses)} tentativas."
            mensagem("Termo", message)
            self.master.destroy()
        else:
            feedback = self.dica(guess)
            mensagem("Termo", feedback)

    def dica(self, guess):
        feedback = ""
        for i in range(len(guess)):
            if guess[i] == self.word[i]:
                feedback += guess[i]
            elif guess[i] in self.word:
                feedback += "?"
            else:
                feedback += "*"
        return feedback

def mensagem(title, message):
    root = CTk()
    dialog = mensagemtexto(root, title, message)
    root.mainloop()

if __name__ == "__main__":
    root = CTk()
    root.geometry("400x200")
    game = Termo(root)
    root.mainloop()
