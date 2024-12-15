import tkinter as tk
from tkinter import messagebox
import uji_hipotesis_ragam 
import uji_hipotesis_ragam_A
import pendugaan_titik_dan_interval_simpangan_baku_B
import pendugaan_titik_dan_interval_simpangan_baku_A
import pengujian_Hipotesis_Rataan_2_Populasi_B
import uji_proporsi
import uji_proporsi_B
import pendugaan_titik_dan_interval_rataan_B
import pendugaan_titik_dan_interval_rataan_A
import regresi_linier_A
import rekresi_linier_b
import pengujian_hipotesis_rataan_1_popolasi_B
import pengujian_rataan_1_populasi
import korelasi_A
import korelasi_B
import pengujian_Hipotesis_Rataan_2_Populasi_A


def handle_submenu(menu_name, submenu_name):
    """
    Menangani pemilihan submenu berdasarkan menu utama dan submenu yang dipilih.
    """
    new_frame = None
    if menu_name == "Regresi Linier" and submenu_name == f"{menu_name} B":
        new_frame = rekresi_linier_b.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pendugaan Titik dan Interval Simpangan Baku" and submenu_name == f"{menu_name} B":
        new_frame = pendugaan_titik_dan_interval_simpangan_baku_B.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pendugaan Titik dan Interval Simpangan Baku" and submenu_name == f"{menu_name} A":
        new_frame = pendugaan_titik_dan_interval_simpangan_baku_A.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pengujian Hipotesis Ragam" and submenu_name == f"{menu_name} B":
        new_frame = uji_hipotesis_ragam.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pengujian Hipotesis Ragam" and submenu_name == f"{menu_name} A":
        new_frame = uji_hipotesis_ragam_A.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pengujian Hipotesis Rataan 2 Populasi" and submenu_name == f"{menu_name} B":
        new_frame = pengujian_Hipotesis_Rataan_2_Populasi_B.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pengujian Hipotesis Rataan 2 Populasi" and submenu_name == f"{menu_name} A":
        new_frame = pengujian_Hipotesis_Rataan_2_Populasi_A.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pengujian Hipotesis Proporsi" and submenu_name == f"{menu_name} A":
        new_frame = uji_proporsi.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pengujian Hipotesis Proporsi" and submenu_name == f"{menu_name} B":
        new_frame = uji_proporsi_B.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pendugaan Titik dan Interval Rataan" and submenu_name == f"{menu_name} B":
        new_frame = pendugaan_titik_dan_interval_rataan_B.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pendugaan Titik dan Interval Rataan" and submenu_name == f"{menu_name} A":
        new_frame = pendugaan_titik_dan_interval_rataan_A.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Regresi Linier" and submenu_name == f"{menu_name} A":
        new_frame = regresi_linier_A.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pengujian Hipotesis Rataan 1 Populasi" and submenu_name == f"{menu_name} B":
        new_frame = pengujian_hipotesis_rataan_1_popolasi_B.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Pengujian Hipotesis Rataan 1 Populasi" and submenu_name == f"{menu_name} A":
        new_frame = pengujian_rataan_1_populasi.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Korelasi" and submenu_name == f"{menu_name} A":
        new_frame = korelasi_A.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    elif menu_name == "Korelasi" and submenu_name == f"{menu_name} B":
        new_frame = korelasi_B.tampilkan_aplikasi(root, lambda: tampilkan_frame(frame_menu))
    
    if new_frame:
        tampilkan_frame(new_frame)
    else:
        messagebox.showinfo("Menu Dipilih", f"Anda memilih: {menu_name} - {submenu_name}")


def tampilkan_frame(frame):
    """
    Menampilkan frame tertentu dan menyembunyikan frame lainnya.
    """
    for f in frames:
        f.pack_forget()
    frame.pack(fill="both", expand=True)


def tampilkan_submenu(menu_name, frame_submenu):
    """
    Menampilkan submenu untuk menu yang dipilih.
    """
    # Bersihkan isi frame submenu
    for widget in frame_submenu.winfo_children():
        widget.destroy()

    # Label judul submenu
    tk.Label(
        frame_submenu,
        text=f"Submenu untuk {menu_name}",
        font=("Arial", 16, "bold"),
        bg="#4682B4",
        fg="white"
    ).pack(pady=15, ipadx=10, ipady=5, fill="x")

    # Tombol untuk submenu A
    tk.Button(
        frame_submenu,
        text=f"{menu_name} A",
        font=("Arial", 12, "bold"),
        bg="#76c893",
        fg="black",
        command=lambda: handle_submenu(menu_name, f"{menu_name} A")
    ).pack(pady=10, ipadx=10, ipady=5)

    # Tombol untuk submenu B
    tk.Button(
        frame_submenu,
        text=f"{menu_name} B",
        font=("Arial", 12, "bold"),
        bg="#76c893",
        fg="black",
        command=lambda: handle_submenu(menu_name, f"{menu_name} B")
    ).pack(pady=10, ipadx=10, ipady=5)

    # Tombol kembali ke menu utama
    tk.Button(
        frame_submenu,
        text="Kembali ke Menu Utama",
        font=("Arial", 12, "bold"),
        bg="#ff6b6b",
        fg="white",
        command=lambda: tampilkan_frame(frame_menu)
    ).pack(pady=20)

    tampilkan_frame(frame_submenu)


def add_background(frame):
    """
    Menambahkan gambar latar belakang ke frame.
    """
    try:
        bg_label = tk.Label(frame, image=background_image)
        bg_label.place(relwidth=1, relheight=1)  # Membuat gambar memenuhi frame
        bg_label.lower()  # Letakkan di belakang semua widget
    except Exception as e:
        messagebox.showerror("Error", f"Gagal memuat gambar latar: {e}")


# Konfigurasi jendela utama
root = tk.Tk()
root.title("Projek Statistik Terapan")
root.geometry("1200x800")
root.resizable(True,True)


# Muat gambar background
try:
    background_image = tk.PhotoImage(file="background.png")  # Ganti dengan file gambar Anda
except Exception:
    background_image = None

# Header Frame
header_frame = tk.Frame(root, bg="#003566", pady=10)
header_frame.pack(fill="x")

# Judul Aplikasi
tk.Label(
    header_frame,
    text="Projek Statistik Terapan",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#003566"
).pack(side="left", padx=10)

# Tombol Keluar
tk.Button(
    header_frame,
    text="Keluar Aplikasi",
    font=("Arial", 12, "bold"),
    bg="#ff6b6b",
    fg="white",
    relief="ridge",
    command=root.quit
).pack(side="right", padx=10)

# Frame Menu Utama
frame_menu = tk.Frame(root, bg="#ffffff")
if background_image:
    add_background(frame_menu)

# Frame Submenu
frame_submenu = tk.Frame(root, bg="#F0F8FF")
if background_image:
    add_background(frame_submenu)

# Daftar menu utama
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

# Tambahkan tombol menu utama
for menu_name in menu_items:
    tk.Button(
        frame_menu,
        text=menu_name,
        font=("Arial", 14),
        bg="#76c893",
        fg="black",
        relief="groove",
        width=50, 
        pady=5,
        command=lambda m=menu_name: tampilkan_submenu(m, frame_submenu)
    ).pack(pady=10)

# Daftar semua frame untuk navigasi
frames = [frame_menu, frame_submenu]

# Tampilkan frame awal (menu utama)
tampilkan_frame(frame_menu)

# Jalankan aplikasi
root.mainloop()
