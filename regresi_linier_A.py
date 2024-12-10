import tkinter as tk
from tkinter import messagebox

def hitung_regresi(entry_x, entry_y):
    """
    Menghitung regresi linier sederhana berdasarkan input X dan Y dari pengguna.
    """
    try:
        # Mengonversi input string ke list float
        x = list(map(float, entry_x.get().split(',')))
        y = list(map(float, entry_y.get().split(',')))

        # Validasi jumlah data X dan Y
        if len(x) != len(y):
            raise ValueError("Jumlah data X dan Y harus sama.")
        
        # Perhitungan regresi sederhana
        n = len(x)
        x_mean = sum(x) / n
        y_mean = sum(y) / n
        b1 = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / sum((xi - x_mean) ** 2 for xi in x)
        b0 = y_mean - b1 * x_mean

        # Menampilkan hasil regresi
        hasil = f"Persamaan Regresi: Y = {b0:.2f} + {b1:.2f}X"
        messagebox.showinfo("Hasil Regresi Linier", hasil)
    except ValueError as e:
        # Menampilkan error yang lebih informatif
        messagebox.showerror("Kesalahan Input", f"Kesalahan: {e}\n\nPastikan Anda memasukkan nilai numerik yang dipisahkan dengan koma.")
    except Exception as e:
        # Menangani kesalahan lain
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def tampilkan_aplikasi(root, kembali_ke_menu):
    """
    Menampilkan antarmuka untuk menghitung regresi linier.
    """
    frame = tk.Frame(root, bg="#E3F2FD")
    frame.pack(fill="both", expand=True)

    # Penyesuaian font dan tampilan
    label_font = ("Helvetica", 12, "bold")
    entry_font = ("Helvetica", 12)
    judul_font = ("Helvetica", 18, "bold")
    button_font = ("Helvetica", 12, "bold")

    # Membuat label judul
    judul = tk.Label(frame, text="Regresi Linier Sederhana", font=judul_font, bg="#2196F3", fg="white")
    judul.pack(pady=15, ipadx=10, ipady=5, fill="x")

    # Frame untuk input data
    frame_input = tk.Frame(frame, bg="#BBDEFB", pady=10)
    frame_input.pack(padx=20, pady=20)

    # Label dan entry untuk X
    tk.Label(frame_input, text="Masukkan nilai X (pisahkan dengan koma):", font=label_font, bg="#BBDEFB").pack(anchor="w", pady=5)
    entry_x = tk.Entry(frame_input, width=50, font=entry_font)
    entry_x.pack(pady=5)

    # Label dan entry untuk Y
    tk.Label(frame_input, text="Masukkan nilai Y (pisahkan dengan koma):", font=label_font, bg="#BBDEFB").pack(anchor="w", pady=5)
    entry_y = tk.Entry(frame_input, width=50, font=entry_font)
    entry_y.pack(pady=5)

    # Tombol untuk menghitung regresi
    tk.Button(
        frame, text="Hitung Regresi", font=button_font, bg="#2196F3", fg="white",
        activebackground="#1976D2", activeforeground="white",
        command=lambda: hitung_regresi(entry_x, entry_y)
    ).pack(pady=20)

    # Tombol untuk kembali ke menu utama
    tk.Button(
        frame, text="Kembali ke Menu Utama", font=button_font, bg="#FF6B6B", fg="white",
        activebackground="#E74C3C", activeforeground="white",
        command=lambda: (frame.pack_forget(), kembali_ke_menu())
    ).pack(pady=10)

    return frame
