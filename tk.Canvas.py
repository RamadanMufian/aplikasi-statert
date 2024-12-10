import tkinter as tk
from tkinter import PhotoImage

# Buat jendela utama
root = tk.Tk()
root.title("Aplikasi dengan Background Gambar")
root.geometry("1200x800")  # Sesuaikan ukuran jendela

# Tambahkan canvas untuk latar belakang
canvas = tk.Canvas(root, width=1200, height=800, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Tambahkan gambar sebagai latar belakang
background_image = PhotoImage(file="background.png")  # Ganti dengan nama file gambar Anda
canvas.create_image(0, 0, anchor="nw", image=background_image)

# Tambahkan frame atau widget di atas latar belakang
frame_menu = tk.Frame(canvas, bg="white", padx=20, pady=20)
canvas.create_window(600, 400, window=frame_menu)  # Atur posisi frame di tengah jendela

# Tambahkan contoh widget ke dalam frame
label = tk.Label(frame_menu, text="Selamat Datang di Aplikasi", font=("Arial", 16), bg="white")
label.pack(pady=10)

btn_exit = tk.Button(frame_menu, text="Keluar", command=root.quit, font=("Arial", 14), bg="red", fg="white")
btn_exit.pack(pady=10)

# Jalankan aplikasi
root.mainloop()
