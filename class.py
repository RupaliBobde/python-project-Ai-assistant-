import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

# Define the main window
root = tk.Tk()
root.title("YOUR AI ASSISTANT")
root.configure(bg='steelblue')

# Create the input field
entry = Entry(root, width=50)
entry.pack(pady=10)

# Define a function to automate YouTube search
def search_youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

# Define a function to automate Google search
def search_google():
    query = entry.get()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Define a function to automate Instagram search
def search_instagram():
    username = entry.get().replace('@', "")
    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)

# Add label and buttons
Label(root, text="Enter your command:", bg='steelblue', fg='white').pack(pady=10)
Button(root, text="Search on Youtube", command=search_youtube).pack(pady=5)
Button(root, text="Search on Google", command=search_google).pack(pady=5)
Button(root, text="Search on Instagram", command=search_instagram).pack(pady=5)

# Run the GUI
root.mainloop()