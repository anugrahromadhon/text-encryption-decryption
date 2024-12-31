import tkinter as tk
from tkinter import messagebox

class TextEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Encryption and Decryption")
        self.root.geometry("500x400")
        self.root.configure(bg="#f4f4f4")

        # Title Label
        self.title_label = tk.Label(root, text="Text Encryption and Decryption", font=("Arial", 16, "bold"), bg="#4caf50", fg="white", pady=10)
        self.title_label.pack(fill=tk.X)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#f4f4f4", pady=10)
        self.input_frame.pack(fill=tk.X, padx=20)

        self.text_label = tk.Label(self.input_frame, text="Enter Text", bg="#f4f4f4", font=("Arial", 12))
        self.text_label.pack(anchor="w")
        self.text_entry = tk.Entry(self.input_frame, font=("Arial", 12), width=50)
        self.text_entry.pack(pady=5)

        self.shift_label = tk.Label(self.input_frame, text="Shift Value (Key)", bg="#f4f4f4", font=("Arial", 12))
        self.shift_label.pack(anchor="w")
        self.shift_entry = tk.Entry(self.input_frame, font=("Arial", 12), width=10)
        self.shift_entry.pack(pady=5)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg="#f4f4f4", pady=10)
        self.button_frame.pack(fill=tk.X, padx=20)

        self.encrypt_button = tk.Button(self.button_frame, text="Encrypt", bg="#4caf50", fg="white", font=("Arial", 12), command=self.encrypt_text)
        self.encrypt_button.grid(row=0, column=0, padx=5, pady=5)

        self.decrypt_button = tk.Button(self.button_frame, text="Decrypt", bg="#2196f3", fg="white", font=("Arial", 12), command=self.decrypt_text)
        self.decrypt_button.grid(row=0, column=1, padx=5, pady=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear", bg="#ff9800", fg="white", font=("Arial", 12), command=self.clear_fields)
        self.clear_button.grid(row=1, column=0, padx=5, pady=5)

        self.exit_button = tk.Button(self.button_frame, text="Exit", bg="#9e9e9e", fg="white", font=("Arial", 12), command=root.quit)
        self.exit_button.grid(row=1, column=1, padx=5, pady=5)

        # Result Frame
        self.result_frame = tk.Frame(root, bg="#f4f4f4", pady=10)
        self.result_frame.pack(fill=tk.X, padx=20)

        self.result_label = tk.Label(self.result_frame, text="Result", bg="#f4f4f4", font=("Arial", 12))
        self.result_label.pack(anchor="w")
        self.result_text = tk.Text(self.result_frame, font=("Arial", 12), height=5, wrap=tk.WORD)
        self.result_text.pack(fill=tk.X, pady=5)

    def caesar_cipher(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                result += char
        return result

    def encrypt_text(self):
        text = self.text_entry.get()
        try:
            shift = int(self.shift_entry.get())
            encrypted = self.caesar_cipher(text, shift)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, encrypted)
            messagebox.showinfo("Success", "Text encrypted successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid shift value. Please enter a number.")

    def decrypt_text(self):
        text = self.text_entry.get()
        try:
            shift = int(self.shift_entry.get())
            decrypted = self.caesar_cipher(text, -shift)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, decrypted)
            messagebox.showinfo("Success", "Text decrypted successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid shift value. Please enter a number.")

    def clear_fields(self):
        self.text_entry.delete(0, tk.END)
        self.shift_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEncryptionApp(root)
    root.mainloop()
