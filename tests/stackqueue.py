import tkinter as tk
from tkinter import messagebox

class StackQueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack & Queue GUI")
        self.root.geometry("400x400")
        
        self.data = []  # List untuk menyimpan data
        
        # Label untuk menampilkan isi list secara real-time
        self.label_display = tk.Label(root, text=str(self.data), font=("Arial", 12))
        self.label_display.pack(pady=10)
        
        # Input untuk Push dan Enqueue
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        # Tombol untuk operasi Stack
        tk.Button(root, text="Push", command=self.push).pack(pady=2)
        tk.Button(root, text="Pop", command=self.pop).pack(pady=2)
        tk.Button(root, text="Peek", command=self.peek).pack(pady=2)
        
        # Tombol untuk operasi Queue
        tk.Button(root, text="Enqueue", command=self.enqueue).pack(pady=2)
        tk.Button(root, text="Dequeue", command=self.dequeue).pack(pady=2)
        tk.Button(root, text="Front", command=self.front).pack(pady=2)
        tk.Button(root, text="Rear", command=self.rear).pack(pady=2)
    
    def update_display(self):
        self.label_display.config(text=str(self.data))
    
    # Operasi Stack
    def push(self):
        value = self.entry.get()
        if value:
            self.data.append(value)
            self.entry.delete(0, tk.END)
            self.update_display()
        else:
            messagebox.showwarning("Peringatan", "Masukkan nilai untuk Push")
    
    def pop(self):
        if self.data:
            self.data.pop()
            self.update_display()
        else:
            messagebox.showwarning("Peringatan", "Stack kosong")
    
    def peek(self):
        if self.data:
            messagebox.showinfo("Peek", f"Top: {self.data[-1]}")
        else:
            messagebox.showwarning("Peringatan", "Stack kosong")
    
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
    app = StackQueueApp(root)
    root.mainloop()
