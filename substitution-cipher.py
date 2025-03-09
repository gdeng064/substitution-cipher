import tkinter as tk
from tkinter import filedialog, messagebox
import random
import string
import os

KEY_FILE = "encryption_key.txt"

# Encryption & Decryption Functions
def encrypt(text, key):
    """Encrypts the given text using a substitution cipher based on the provided key."""
    all_chars = string.printable
    translation_table = str.maketrans(all_chars, key)
    return text.translate(translation_table)

def decrypt(ciphertext, key):
    """Decrypts the given ciphertext using the provided key by reversing the encryption process."""
    all_chars = string.printable
    decryption_table = str.maketrans(key, all_chars)
    return ciphertext.translate(decryption_table)

def generate_key():
    """Generates a random key by shuffling all printable characters."""
    all_chars = list(string.printable)
    random.shuffle(all_chars)
    return ''.join(all_chars)

def save_key(key):
    """Saves the encryption key to a file for future use."""
    with open(KEY_FILE, "w") as file:
        file.write(key)
    messagebox.showinfo("Success", "Encryption key saved successfully.")

def load_key():
    """Loads the encryption key from a file if it exists."""
    if not os.path.exists(KEY_FILE):
        messagebox.showwarning("Error", "No saved key found!")
        return None
    with open(KEY_FILE, "r") as file:
        return file.read()

def encrypt_text():
    """Encrypts the input text using the provided or loaded key and displays the result."""
    text = input_text.get("1.0", tk.END).strip()
    key = key_entry.get()
    if not key:
        messagebox.showwarning("Error", "Please generate or load a key first!")
        return
    ciphertext = encrypt(text, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, ciphertext)

def decrypt_text():
    """Decrypts the input ciphertext using the provided or loaded key and displays the result."""
    ciphertext = input_text.get("1.0", tk.END).strip()
    key = key_entry.get()
    if not key:
        messagebox.showwarning("Error", "Please generate or load a key first!")
        return
    plaintext = decrypt(ciphertext, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, plaintext)

def generate_and_display_key():
    """Generates a new encryption key, displays it, and saves it to a file."""
    key = generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)
    save_key(key)

def load_and_display_key():
    """Loads an encryption key from a file and displays it in the key entry field."""
    key = load_key()
    if key:
        key_entry.delete(0, tk.END)
        key_entry.insert(0, key)
def copy_to_clipboard(text):
    """Copies the provided text to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    messagebox.showinfo("Copied", "Text copied to clipboard!")

def copy_ciphertext():
    """Copies the ciphertext from the output box to the clipboard."""
    text = output_text.get("1.0", tk.END).strip()
    if text:
        copy_to_clipboard(text)

def copy_key():
    """Copies the encryption key to the clipboard."""
    key = key_entry.get()
    if key:
        copy_to_clipboard(key)
        
# GUI Setup
root = tk.Tk()
root.title("Text Encryptor & Decryptor")
root.geometry("1920x1080")

tk.Label(root, text="Input Text:").pack()
input_text = tk.Text(root, height=30, width=180)
input_text.pack()

tk.Label(root, text="Encryption Key:").pack()
key_entry = tk.Entry(root, width=180)
key_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Generate Key", command=generate_and_display_key).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Load Key", command=load_and_display_key).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Encrypt", command=encrypt_text).grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="Decrypt", command=decrypt_text).grid(row=0, column=3, padx=5, pady=5)
tk.Button(button_frame, text="Copy Ciphertext", command=copy_ciphertext).grid(row=0, column=4, padx=5, pady=5)
tk.Button(button_frame, text="Copy Key", command=copy_key).grid(row=0, column=5, padx=5, pady=5)

tk.Label(root, text="Output:").pack()
output_text = tk.Text(root, height=30, width=180)
output_text.pack()

root.mainloop()
