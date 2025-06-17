import tkinter as tk

# --- The list of questions you want to ask ---
# You can easily add, remove, or change questions here.
QUESTIONS = [
    "Think of your favorite color.",
    "What is the name of your first pet?",
    "Imagine your favorite fruit.",
    "What city would you most like to visit?",
    "Think of a song that makes you happy.",
    "What is your favorite season of the year?",
    "Your Password is insecure. The probability of being hacked is very high."
]

class QuestionApp:
    def __init__(self, root):
        """
        Sets up the main application window and its widgets.
        """
        self.root = root
        self.root.title("Question Game")
        self.root.geometry("400x200") # Set the window size (width x height)

        # A variable to keep track of which question we are on
        self.current_question_index = 0

        # Create a tkinter String Variable to hold the question text.
        # This allows us to easily update the label's text.
        self.question_text = tk.StringVar()
        self.question_text.set(QUESTIONS[self.current_question_index])

        # --- Create the Widgets ---

        # The label that will display the current question
        question_label = tk.Label(
            self.root,
            textvariable=self.question_text,
            font=("Helvetica", 14),
            wraplength=380, # Makes the text wrap if it's too long
            pady=20
        )
        question_label.pack(expand=True)

        # The button to advance to the next question
        next_button = tk.Button(
            self.root,
            text="Next ->",
            font=("Helvetica", 12),
            command=self.show_next_question
        )
        next_button.pack(pady=20)


    def show_next_question(self):
        """
        This method is called when the 'Next' button is clicked.
        It updates the label to show the next question or closes the app.
        """
        # Move to the next question index
        self.current_question_index += 1

        # Check if we have run out of questions
        if self.current_question_index < len(QUESTIONS):
            # If there are more questions, update the text
            self.question_text.set(QUESTIONS[self.current_question_index])
        else:
            # If we're at the end, close the window
            self.root.destroy()


# --- Main entry point of the program ---
if __name__ == "__main__":
    # Create the main window
    main_window = tk.Tk()
    
    # Create an instance of our app
    app = QuestionApp(main_window)
    
    # Start the tkinter event loop. This keeps the window open and responsive.
    main_window.mainloop()