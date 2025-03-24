import tkinter as tk
from tkinter import messagebox

class QueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue GUI")
        self.root.geometry("300x300")
        
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
    
    def update_display(self):
        """Memperbarui tampilan list."""
        self.label_display.config(text=str(self.data))
    
    # Operasi Queue
    def enqueue(self):
        value = self.entry.get()
        if value:
            self.data.append(value)
            self.entry.delete(0, tk.END)
            self.update_display()
        else:
            messagebox.showwarning("Peringatan", "Masukkan nilai untuk Enqueue")
    
    def dequeue(self):
        if self.data:
            self.data.pop(0)
            self.update_display()
        else:
            messagebox.showwarning("Peringatan", "Queue kosong")
    
    def front(self):
        if self.data:
            messagebox.showinfo("Front", f"Front: {self.data[0]}")
        else:
            messagebox.showwarning("Peringatan", "Queue kosong")
    
    def rear(self):
        if self.data:
            messagebox.showinfo("Rear", f"Rear: {self.data[-1]}")
        else:
            messagebox.showwarning("Peringatan", "Queue kosong")

if __name__ == "__main__":
    root = tk.Tk()
    app = QueueApp(root)
    root.mainloop()