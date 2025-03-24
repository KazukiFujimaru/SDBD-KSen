# Library yang diperlukan
import tkinter as tk
from tkinter import messagebox

# Pembuatan GUI
class QueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue GUI")
        self.root.geometry("300x300")
        
        # Array yang disesdiakan untuk aplikasi
        self.data = []  # List untuk menyimpan data
        
        # Label untuk menampilkan isi list secara real-time
        self.label_display = tk.Label(root, text=str(self.data), font=("Arial", 12))
        self.label_display.pack(pady=10)
        
        # Input untuk Enqueue
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        # Frame untuk tombol
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        # Tombol untuk operasi Queue
        tk.Button(button_frame, text="Enqueue", command=self.enqueue, width=10).pack(pady=2)
        tk.Button(button_frame, text="Dequeue", command=self.dequeue, width=10).pack(pady=2)
        tk.Button(button_frame, text="Front", command=self.front, width=10).pack(pady=2)
        tk.Button(button_frame, text="Rear", command=self.rear, width=10).pack(pady=2)
    
    # Fungsi update array
    def update_display(self):
        self.label_display.config(text=str(self.data))
    
    # Fungsi Queue
    def enqueue(self):
        # Mendapatkan input
        value = self.entry.get()

        # Jika data ada
        if value:
            # Fungsi Queue, silahkan isi

        else:
            messagebox.showwarning("Peringatan", "Masukkan nilai untuk Enqueue")
    
    def dequeue(self):
        if self.data:
            # Fungsi Dequeue, silahkan isi

        else:
            messagebox.showwarning("Peringatan", "Queue kosong")
    
    def front(self):
        if self.data:
            messagebox.showinfo("Front", isi fungsi)
        else:
            messagebox.showwarning("Peringatan", "Queue kosong")
    
    def rear(self):
        if self.data:
            messagebox.showinfo("Rear", isi fungsi)
        else:
            messagebox.showwarning("Peringatan", "Queue kosong")

# Loop agar aplikasi tetap berjalan
if __name__ == "__main__":
    root = tk.Tk()
    app = QueueApp(root)
    root.mainloop()