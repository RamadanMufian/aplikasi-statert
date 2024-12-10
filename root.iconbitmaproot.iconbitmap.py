import tkinter as tk
from tkinter import messagebox

# Fungsi untuk contoh
def tampilkan_pesan():
    messagebox.showinfo("Info", "Aplikasi dengan ikon!")

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi dengan Ikon")
root.geometry("300x200")

# Menambahkan ikon
root.iconbitmap("icon.ico")  # Ganti "icon.ico" dengan nama file ikon Anda

# Komponen GUI
label = tk.Label(root, text="Ini adalah aplikasi dengan ikon.", font=("Arial", 12))
label.pack(pady=20)

btn = tk.Button(root, text="Klik Saya", command=tampilkan_pesan, font=("Arial", 12))
btn.pack(pady=10)

# Menjalankan GUI
root.mainloop()
