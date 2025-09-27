import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x500")
root.config(bg="#1E1E1E")
root.resizable(False, False)

user_score = 0
computer_score = 0

def update_scores():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    
    if user_choice == computer_choice:
        return "It's a Tie!", "gray"
    
    winning_combinations = {
        "rock": "scissors",
        "paper": "rock", 
        "scissors": "paper"
    }
    
    if winning_combinations[user_choice] == computer_choice:
        user_score += 1
        return "You Win!", "#4ECDC4"
    else:
        computer_score += 1
        return "Computer Wins!", "#FF6B6B"

def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    user_choice_label.config(text=f"Your Choice: {user_choice.title()}")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice.title()}")
    
    result, color = determine_winner(user_choice, computer_choice)
    result_label.config(text=result, fg=color)
    
    update_scores()
    
    if user_choice == "rock":
        user_display.config(text="✊")
    elif user_choice == "paper":
        user_display.config(text="✋")
    else:
        user_display.config(text="✌️")
    
    if computer_choice == "rock":
        computer_display.config(text="✊")
    elif computer_choice == "paper":
        computer_display.config(text="✋")
    else:
        computer_display.config(text="✌️")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scores()
    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer Choice: ")
    result_label.config(text="Make Your Choice!", fg="white")
    user_display.config(text="?")
    computer_display.config(text="?")

heading = tk.Label(root, text="Rock Paper Scissors", bg="#1E1E1E", fg="#FFA500",
                  font=("Arial", 20, "bold"))
heading.pack(pady=15)

score_frame = tk.Frame(root, bg="#1E1E1E")
score_frame.pack(pady=10)

user_score_label = tk.Label(score_frame, text="Your Score: 0", fg="white", bg="#1E1E1E",
                           font=("Arial", 12, "bold"))
user_score_label.pack(side="left", padx=20)

computer_score_label = tk.Label(score_frame, text="Computer Score: 0", fg="white", bg="#1E1E1E",
                               font=("Arial", 12, "bold"))
computer_score_label.pack(side="right", padx=20)

display_frame = tk.Frame(root, bg="#1E1E1E")
display_frame.pack(pady=20)

user_frame = tk.Frame(display_frame, bg="#1E1E1E")
user_frame.pack(side="left", padx=30)

user_title = tk.Label(user_frame, text="YOU", fg="#4ECDC4", bg="#1E1E1E",
                     font=("Arial", 14, "bold"))
user_title.pack()

user_display = tk.Label(user_frame, text="?", fg="#4ECDC4", bg="#1E1E1E",
                       font=("Arial", 40), width=3, height=2)
user_display.pack(pady=5)

user_choice_label = tk.Label(user_frame, text="Your Choice: ", fg="white", bg="#1E1E1E",
                            font=("Arial", 10))
user_choice_label.pack()

vs_label = tk.Label(display_frame, text="VS", fg="#FFA500", bg="#1E1E1E",
                   font=("Arial", 20, "bold"))
vs_label.pack(side="left", padx=20)

computer_frame = tk.Frame(display_frame, bg="#1E1E1E")
computer_frame.pack(side="left", padx=30)

computer_title = tk.Label(computer_frame, text="COMPUTER", fg="#FF6B6B", bg="#1E1E1E",
                         font=("Arial", 14, "bold"))
computer_title.pack()

computer_display = tk.Label(computer_frame, text="?", fg="#FF6B6B", bg="#1E1E1E",
                           font=("Arial", 40), width=3, height=2)
computer_display.pack(pady=5)

computer_choice_label = tk.Label(computer_frame, text="Computer Choice: ", fg="white", bg="#1E1E1E",
                                font=("Arial", 10))
computer_choice_label.pack()

result_label = tk.Label(root, text="Make Your Choice!", fg="white", bg="#1E1E1E",
                       font=("Arial", 16, "bold"))
result_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#1E1E1E")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock ✊", bg="#2D2D2D", fg="#4ECDC4",
                    font=("Arial", 12, "bold"), width=8, height=2,
                    command=lambda: play_game("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper ✋", bg="#2D2D2D", fg="#FFA500",
                     font=("Arial", 12, "bold"), width=8, height=2,
                     command=lambda: play_game("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors ✌️", bg="#2D2D2D", fg="#FF6B6B",
                        font=("Arial", 12, "bold"), width=8, height=2,
                        command=lambda: play_game("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

control_frame = tk.Frame(root, bg="#1E1E1E")
control_frame.pack(pady=10)

reset_btn = tk.Button(control_frame, text="Reset Game", bg="#FFA500", fg="black",
                     font=("Arial", 10, "bold"), command=reset_game)
reset_btn.pack(side="left", padx=10)

quit_btn = tk.Button(control_frame, text="Quit", bg="#FF6B6B", fg="black",
                    font=("Arial", 10, "bold"), command=root.quit)
quit_btn.pack(side="left", padx=10)

root.mainloop()