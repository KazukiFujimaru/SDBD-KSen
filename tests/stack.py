# Library yang diperlukan
import tkinter as tk
from tkinter import messagebox

# Pembuatan GUI
class StackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack GUI")
        self.root.geometry("300x300")
        
        # Array yang disesdiakan untuk aplikasi
        self.data = []  # List untuk menyimpan data
        
        # Label untuk menampilkan isi list secara real-time
        self.label_display = tk.Label(root, text=str(self.data), font=("Arial", 12))
        self.label_display.pack(pady=10)
        
        # Kolom Input untuk Push
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        # Frame untuk tombol
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        # Tombol untuk operasi Stack
        tk.Button(button_frame, text="Push", command=self.push, width=10).pack(pady=2)
        tk.Button(button_frame, text="Pop", command=self.pop, width=10).pack(pady=2)
        tk.Button(button_frame, text="Peek", command=self.peek, width=10).pack(pady=2)
    
    # Fungsi update array
    def update_display(self):
        self.label_display.config(text=str(self.data))
    
    # Fungsi Push
    def push(self):
        # Mendapatkan input
        value = self.entry.get()

        # Jika data ada
        if value:
            # Fungsi stack, silahkan isi
            self.update_display()
        else:
            messagebox.showwarning("Peringatan", "Masukkan nilai untuk Push")
    
    def pop(self):
        if self.data:
            # Fungsi stack, silahkan isi
            self.update_display()
        else:
            messagebox.showwarning("Peringatan", "Stack kosong")
    
    def peek(self):
        if self.data:
            messagebox.showinfo("Peek", "isi fungsi")
        else:
            messagebox.showwarning("Peringatan", "Stack kosong")

# Loop agar aplikasi tetap berjalan
if __name__ == "__main__":
    root = tk.Tk()
    app = StackApp(root)
    root.mainloop()