import tkinter as tk
from tkinter import messagebox

def hitung_regresi(entry_x, entry_y):
    try:
        x = list(map(float, entry_x.get().split(',')))
        y = list(map(float, entry_y.get().split(',')))
        if len(x) != len(y):
            raise ValueError("Jumlah data X dan Y harus sama.")
        
        # Proses perhitungan regresi sederhana
        n = len(x)
        x_mean = sum(x) / n
        y_mean = sum(y) / n
        b1 = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / sum((xi - x_mean) ** 2 for xi in x)
        b0 = y_mean - b1 * x_mean

        hasil = f"Persamaan Regresi: Y = {b0:.2f} + {b1:.2f}X"
        messagebox.showinfo("Hasil Regresi Linier", hasil)
    except ValueError as e:
        messagebox.showerror("Error", f"Kesalahan Input: {e}")

def tampilkan_aplikasi(root, kembali_ke_menu):
    frame = tk.Frame(root, bg="#E8F6F3")
    frame.pack(fill="both", expand=True)

    label_font = ("Helvetica", 12, "bold")
    entry_font = ("Helvetica", 12)
    judul_font = ("Helvetica", 18, "bold")
    button_font = ("Helvetica", 12, "bold")

    judul = tk.Label(frame, text="Regresi Linier Sederhana", font=judul_font, bg="#1ABC9C", fg="white")
    judul.pack(pady=15, ipadx=10, ipady=5, fill="x")

    frame_input = tk.Frame(frame, bg="#D4EFDF", pady=10)
    frame_input.pack(padx=10, pady=10)

    tk.Label(frame_input, text="Masukkan nilai X (pisahkan dengan koma):", font=label_font, bg="#D4EFDF").pack()
    entry_x = tk.Entry(frame_input, width=50, font=entry_font)
    entry_x.pack(pady=5)

    tk.Label(frame_input, text="Masukkan nilai Y (pisahkan dengan koma):", font=label_font, bg="#D4EFDF").pack()
    entry_y = tk.Entry(frame_input, width=50, font=entry_font)
    entry_y.pack(pady=5)

    tk.Button(
        frame, text="Hitung Regresi", font=button_font, bg="#1ABC9C", fg="white",
        command=lambda: hitung_regresi(entry_x, entry_y)
    ).pack(pady=20)

    tk.Button(
        frame, text="Kembali ke Menu Utama", font=button_font, bg="#FF6B6B", fg="white",
        command=lambda: (frame.pack_forget(), kembali_ke_menu())
    ).pack(pady=10)

    return frame
