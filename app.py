import tkinter as tk
import random

def generate():
    return random.randint(1, 100)

def compare(number, entry):
    if number == entry:
        return "Correct"
    return "Too high" if number < entry else "Too low"

class GuessGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Guess the Number Game")
        self.window.geometry("500x500")
        self.window.resizable(True, True)
        
        self.console = tk.Text(self.window, state='disabled', wrap='word', height=20)
        self.console.pack(fill=tk.BOTH, expand=True)
        self.console.config(state=tk.NORMAL)
        
        self.mode_var = tk.StringVar(value="Facile")
        easy_radio = tk.Radiobutton(self.window, text="Mode Facile (Essais infinis)",
                                    variable=self.mode_var, value="Facile", command=self.reset_game)
        easy_radio.pack(side=tk.TOP, padx=10, pady=2)
        hard_radio = tk.Radiobutton(self.window, text="Mode Difficile (5 essais)",
                                    variable=self.mode_var, value="Difficile", command=self.reset_game)
        hard_radio.pack(side=tk.TOP, padx=10, pady=2)
        
        self.entry = tk.Entry(self.window)
        self.entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=(0, 10))
        
        self.guess_button = tk.Button(self.window, text="Guess", command=self.attempt_guess)
        self.guess_button.pack(pady=(0, 10))
        
        self.reset_game()
        self.window.mainloop()

    def reset_game(self):
        self.number = generate()
        self.attempts = 0
        self.console.config(state=tk.NORMAL)
        self.console.delete(1.0, tk.END)
        self.console.insert(tk.END, "A number between 1 and 100 has been generated. Start guessing!\n")
        self.console.config(state='disabled')

    def attempt_guess(self):
        user_entry = self.entry.get()
        try:
            user_guess = int(user_entry)
            result = compare(self.number, user_guess)
            self.attempts += 1
            self.console.config(state=tk.NORMAL)
            
            if result == "Correct":
                self.console.insert(tk.END, f"Correct! You guessed the number in {self.attempts} attempts.\n")
                self.reset_game()
            else:
                self.console.insert(tk.END, f"{result}. Try again.\n")
                if self.mode_var.get() == "Difficile" and self.attempts >= 5:
                    self.console.insert(tk.END, f"Game over! The number was: {self.number}\n")
                    self.reset_game()
            self.console.config(state='disabled')
            self.entry.delete(0, tk.END)
        except ValueError:
            self.console.config(state=tk.NORMAL)
            self.console.insert(tk.END, "Please enter a valid integer.\n")
            self.console.config(state='disabled')
        self.console.see(tk.END)

if __name__ == "__main__":
    GuessGame()