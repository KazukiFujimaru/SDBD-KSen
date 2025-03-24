#Berikut adalah salah satu contoh bagaimana ADT diguunakan pada suatu program :
#<pre class="code-box"><code class="language-python">class Stack:
#def __init__(self):
#self.stack = []  # Menggunakan list untuk menyimpan elemen stack

#def push(self, data):
# Menambahkan elemen ke dalam stack
#self.stack.append(data)

#def pop(self):
# Menghapus dan mengembalikan elemen teratas dari stack
#if not self.is_empty():
#return self.stack.pop()
#return "Stack kosong"

#def peek(self):
# Mengembalikan elemen teratas tanpa menghapusnya
#if not self.is_empty():
#return self.stack[-1]
#return "Stack kosong"

#def is_empty(self):
# Mengecek apakah stack kosong
#return len(self.stack) == 0

#def size(self):
# Mengembalikan jumlah elemen dalam stack
#return len(self.stack)

#def display(self):
# Menampilkan elemen stack
#print(self.stack[::-1])  # Menampilkan dalam urutan terbalik (elemen teratas dulu)

# Contoh penggunaan
#s = Stack()
#s.push(10)
#s.push(20)
#s.push(30)
#s.display()  # Output: [30, 20, 10]

#print(s.pop())  # Output: 30
#print(s.peek())  # Output: 20
#print(s.is_empty())  # Output: False</code></pre>
#</div>