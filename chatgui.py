import tkinter as tk
import openai

# Set up OpenAI API credentials
openai.api_key = "nv-30bVqUG136OK8PmNbXrkN0V4x0SSacDnnBprfvIe1rO2gh6l"

# Function to handle sending a message
def send_message():
    message = entry.get()
    if message.strip() != "":
        chat_box.insert(tk.END, "User: " + message + "\n")
        response = generate_response(message)
        chat_box.insert(tk.END, "ChatGPT: " + response + "\n")
        entry.delete(0, tk.END)

# Function to generate a response using ChatGPT model
def generate_response(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=50,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Create the main window
window = tk.Tk()
window.title("ChatGPT GUI")

# Create a chat box
chat_box = tk.Text(window, width=50, height=20)
chat_box.grid(column=0, row=0, padx=10, pady=10)

# Create an entry field for user input
entry = tk.Entry(window, width=40)
entry.grid(column=0, row=1, padx=10, pady=10)

# Create a button to send the message
button = tk.Button(window, text="Send", command=send_message)
button.grid(column=1, row=1, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
