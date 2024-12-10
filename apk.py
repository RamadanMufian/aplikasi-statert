import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Untuk memproses gambar

def handle_menu_selection(menu_name):
    # Tampilkan pesan ketika tombol menu diklik
    messagebox.showinfo("Menu Dipilih", f"Anda memilih: {menu_name}")

# Buat jendela utama
root = tk.Tk()
root.title("Projek Statistik Terapan")
root.geometry("800x600")  # Lebar x Tinggi
root.resizable(False, False)

# Tambahkan gambar latar belakang
bg_image_path = "background.jpg"  # Ganti dengan path gambar Anda
try:
    bg_image = Image.open(bg_image_path)  # Buka gambar
    bg_image = bg_image.resize((800, 600), Image.ANTIALIAS)  # Sesuaikan ukuran gambar
    bg_photo = ImageTk.PhotoImage(bg_image)  # Konversi ke format Tkinter
    bg_label = tk.Label(root, image=bg_photo)  # Buat label dengan gambar
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Tempatkan di latar belakang
except FileNotFoundError:
    messagebox.showerror("Error", f"Gambar '{bg_image_path}' tidak ditemukan.")
    bg_label = None
except PermissionError:
    messagebox.showerror("Error", f"Izin ditolak untuk membuka gambar '{bg_image_path}'.")
    bg_label = None
except Exception as e:
    messagebox.showerror("Error", f"Gagal memuat gambar latar belakang:\n{e}")
    bg_label = None

# Tambahkan judul
title_label = tk.Label(
    root,
    text="Projek Statistik Terapan",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="black",
    relief="ridge"
)
title_label.pack(pady=20)

# Daftar menu
menu_items = [
    "Pendugaan Titik dan Interval Rataan",
    "Pendugaan Titik dan Interval Simpangan Baku",
    "Pengujian Hipotesis Rataan 1 Populasi",
    "Pengujian Hipotesis Ragam",
    "Pengujian Hipotesis Proporsi",
    "Pengujian Hipotesis Rataan 2 Populasi",
    "Regresi Linier",
    "Korelasi"
]

# Tambahkan frame untuk menampung tombol menu
menu_frame = tk.Frame(root, bg="lightblue", relief="ridge")
menu_frame.pack(pady=20, padx=50, fill="both", expand=True)

# Buat tombol untuk setiap menu
for menu_name in menu_items:
    button = tk.Button(
        menu_frame,
        text=menu_name,
        font=("Arial", 12),
        bg="lightgreen",
        fg="black",
        relief="raised",
        width=40,
        command=lambda m=menu_name: handle_menu_selection(m)
    )
    button.pack(pady=5)

# Tambahkan tombol keluar
exit_button = tk.Button(
    root,
    text="Keluar",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    relief="ridge",
    width=40,
    command=root.quit
)
exit_button.pack(pady=20)

# Jalankan aplikasi
root.mainloop()
