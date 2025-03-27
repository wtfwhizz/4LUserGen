import tkinter as tk
import random
import string

# Function to generate a random 4-letter username
def generate_username():
    characters = string.ascii_lowercase  # Pool of characters (lowercase letters)
    username = ''.join(random.choice(characters) for _ in range(4))  # Generate username
    username_label.config(text=f"Your random 4-letter username is: {username}")  # Display username

# Create the main window
root = tk.Tk()
root.title("Random Username Generator")
root.geometry("400x200")  # Size of the window
root.configure(bg='#f0f0f0')

# Create a label for the username output
username_label = tk.Label(root, text="Your random 4-letter username will appear here", 
                          font=("Helvetica", 14), bg='#f0f0f0', fg='#333')
username_label.pack(pady=20)

# Create a button to generate the username
generate_button = tk.Button(root, text="Generate Username", font=("Helvetica", 12), 
                            command=generate_username, bg='#4CAF50', fg='white', relief="raised")
generate_button.pack(pady=10)

# Run the GUI
root.mainloop()
