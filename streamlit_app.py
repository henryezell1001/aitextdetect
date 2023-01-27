import tkinter as tk
import numpy as np
from nltk.util import ngrams
from collections import Counter

def calculate_perplexity(text):
    # function that calculate perplexity of the input text
    # You could put the code of your perplexity calculation script here
    pass

def calculate_burstiness(text):
    # function that calculate burstiness of the input text
    # You could put the code of your burstiness calculation script here
    pass

# Create GUI window
window = tk.Tk()
window.title("Text Input")

# Create text box
text_box = tk.Text(window, height=5, width=30)
text_box.pack()

# Create submit button
def on_submit():
    text = text_box.get("1.0", "end")
    # remove newline character
    text = text.rstrip()
    perplexity = calculate_perplexity(text)
    burstiness = calculate_burstiness(text)
    print("Text submitted: ", text)
    print("Perplexity: ", perplexity)
    print("Burstiness: ", burstiness)

submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.pack()

# Create clear button
def on_clear():
    text_box.delete("1.0", "end")

clear_button = tk.Button(window, text="Clear", command=on_clear)
clear_button.pack()

window.mainloop()
