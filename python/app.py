import tkinter as tk
from tkinter import messagebox, ttk
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Computer Quiz")
        self.root.geometry("500x500")

        # DITO PWEDE MAGDAGDAG NG QUESTIONS: (Tanong, Tama, [Lahat ng Options])
        self.questions = [
            ("What does CPU stand for?", "Central Processing Unit", 
             ["Central Processing Unit", "Computer Personal Unit", "Central Power User", "Core Processing Unit"]),
            
            ("What does GPU stand for?", "Graphics Processing Unit", 
             ["Graphics Processing Unit", "General Power Unit", "Gaming Power Unit", "Global Photo User"]),
            
            ("What does RAM stand for?", "Random Access Memory", 
             ["Random Access Memory", "Read Access Module", "Rapid Action Memory", "Remote Analytical Memory"]),
            
            ("What does PSU stand for?", "Power Supply Unit", 
             ["Power Supply Unit", "Personal System Unit", "Power Source Utility", "Primary Storage Unit"]),

            ("What is the main circuit board of a computer called?", "Motherboard", 
             ["Motherboard", "Mainframe", "Hard Drive", "CPU"]),

            ("Which of these is an Operating System?", "Windows", 
             ["Windows", "Google Chrome", "Microsoft Office", "Intel"]),

            ("What does SSD stand for?", "Solid State Drive", 
             ["Solid State Drive", "Super Speed Disk", "System Storage Device", "Soft State Drive"]),

            ("What is the brain of the computer?", "CPU", 
             ["CPU", "RAM", "Monitor", "Keyboard"]),

            ("What does HTTP stand for in website addresses?", "Hypertext Transfer Protocol", 
             ["Hypertext Transfer Protocol", "High Tech Transfer Process", "Hyperlink Text Test Protocol", "Home Tool Technology Process"]),

            ("Which component is used for long-term data storage?", "Hard Drive", 
             ["Hard Drive", "RAM", "CPU", "Power Supply"])
        ]
        
        # Shuffle questions para hindi laging pareho ang pagkakasunod-sunod
        random.shuffle(self.questions)
        
        self.score = 0
        self.current_q = 0
        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        # Progress Bar
        self.progress = ttk.Progressbar(self.root, length=350, mode="determinate")
        self.progress.pack(pady=20)
        self.progress["maximum"] = len(self.questions)

        # Question Number Label
        self.q_num_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.q_num_label.pack()

        # Question Text
        self.label = tk.Label(self.root, text="", font=("Arial", 12, "bold"), wraplength=450, height=4)
        self.label.pack(pady=10)

        # Answer Buttons
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", width=45, pady=8, font=("Arial", 10), command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

    def load_question(self):
        self.progress["value"] = self.current_q
        self.q_num_label.config(text=f"Question {self.current_q + 1} of {len(self.questions)}")
        
        q_data = self.questions[self.current_q]
        self.label.config(text=q_data[0])
        self.correct_answer = q_data[1]
        
        # Shuffle options
        options = list(q_data[2])
        random.shuffle(options)
        self.current_options = options

        for i in range(4):
            self.option_buttons[i].config(text=options[i], bg="SystemButtonFace")

    def check_answer(self, index):
        selected = self.current_options[index]
        if selected == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Galing! Tama ang sagot mo.")
        else:
            messagebox.showerror("Wrong", f"Mali! Ang tamang sagot ay:\n{self.correct_answer}")
        
        self.current_q += 1
        if self.current_q < len(self.questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Over", f"Tapos na ang Quiz!\n\nFinal Score: {self.score}/{len(self.questions)}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
