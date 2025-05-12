import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
DATA_FILE = "data.txt"
class DataApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Sender App")
        self.geometry("400x400")
        self.resizable(False, False)
        # Load data from file
        self.data = self.load_data()
        # Display loaded data
        self.lbl_loaded = tk.Label(self, text="Loaded Data:")
        self.lbl_loaded.pack(pady=(10, 0))
        self.txt_data = scrolledtext.ScrolledText(self, width=45, height=10, state='disabled')
        self.txt_data.pack(pady=(0, 10))
        self.display_data()
        # Input label
        self.lbl_input = tk.Label(self, text="Enter Data to Send:")
        self.lbl_input.pack()
        # Input text box
        self.entry_data = tk.Text(self, width=45, height=5)
        self.entry_data.pack(pady=(0, 10))
        # Send button
        self.btn_send = tk.Button(self, text="Send", command=self.send_data)
        self.btn_send.pack()
    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return [line.strip() for line in lines]
    def display_data(self):
        self.txt_data.config(state='normal')
        self.txt_data.delete(1.0, tk.END)
        if self.data:
            self.txt_data.insert(tk.END, "\n".join(self.data))
        else:
                        self.txt_data.insert(tk.END, "(No data loaded)")
        self.txt_data.config(state='disabled')
    def send_data(self):
        new_data = self.entry_data.get(1.0, tk.END).strip()
        if not new_data:
            messagebox.showwarning("Warning", "Please enter data before sending.")
            return
        # Append new data to file and internal list
        try:
            with open(DATA_FILE, "a", encoding="utf-8") as f:
                f.write(new_data + "\n")
            self.data.append(new_data)
            self.display_data()
            self.entry_data.delete(1.0, tk.END)
            messagebox.showinfo("Success", "Data sent and saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")
if __name__ == "__main__":
    app = DataApp()
    app.mainloop()