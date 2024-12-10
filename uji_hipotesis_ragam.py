import numpy as np
from scipy.stats import f
import tkinter as tk
from tkinter import messagebox

def uji_hipotesis_ragam(frame_utama, root):
    def lakukan_uji_hipotesis():
        try:
            # Ambil data dari input
            data1 = list(map(float, entry_data1.get().split(',')))
            data2 = list(map(float, entry_data2.get().split(',')))
            alpha = float(entry_alpha.get())

            # Hitung varians
            var1 = np.var(data1, ddof=1)
            var2 = np.var(data2, ddof=1)

            # Hitung statistik F
            if var1 > var2:
                F = var1 / var2
                dfn = len(data1) - 1
                dfd = len(data2) - 1
            else:
                F = var2 / var1
                dfn = len(data2) - 1
                dfd = len(data1) - 1

            # Hitung p-value
            if var1 > var2:
                p_value = 2 * (1 - f.cdf(F, dfn, dfd))  # Two-tailed test
            else:
                p_value = 2 * f.cdf(F, dfn, dfd)  # Two-tailed test

            # Tentukan hasil pengujian
            if p_value < alpha:
                keputusan = "Tolak hipotesis nol: Varians tidak sama."
            else:
                keputusan = "Terima hipotesis nol: Varians sama."

            # Tampilkan hasil
            hasil = f"Hasil Uji Hipotesis Ragam (Uji F)\nStatistik F: {F:.4f}\nP-Value: {p_value:.4f}\nKeputusan: {keputusan}"
            messagebox.showinfo("Hasil Pengujian", hasil)

        except ValueError:
            messagebox.showerror("Input Error", "Pastikan data dan alpha diisi dengan format yang benar.")

    # Buat frame untuk tampilan uji hipotesis
    frame = tk.Frame(root, bg="white")

    # Judul
    judul_font = ("Arial", 16, "bold")
    judul = tk.Label(frame, text="Uji Hipotesis Ragam (Uji F)", font=judul_font, bg="#4682B4", fg="white")
    judul.pack(pady=15, ipadx=10, ipady=5, fill="x")

    # Input Data Sampel 1
    label_data1 = tk.Label(frame, text="Data Sampel 1 (pisahkan dengan koma):", font=("Arial", 12, "bold"), bg="#F0F8FF")
    label_data1.pack(pady=5)
    entry_data1 = tk.Entry(frame, width=50, font=("Arial", 12))
    entry_data1.pack(pady=5)

    # Input Data Sampel 2
    label_data2 = tk.Label(frame, text="Data Sampel 2 (pisahkan dengan koma):", font=("Arial", 12, "bold"), bg="#F0F8FF")
    label_data2.pack(pady=5)
    entry_data2 = tk.Entry(frame, width=50, font=("Arial", 12))
    entry_data2.pack(pady=5)

    # Input Alpha
    label_alpha = tk.Label(frame, text="Tingkat Signifikansi (alpha):", font=("Arial", 12, "bold"), bg="#F0F8FF")
    label_alpha.pack(pady=5)
    entry_alpha = tk.Entry(frame, width=20, font=("Arial", 12))
    entry_alpha.pack(pady=5)

    # Tombol Uji
    btn_uji = tk.Button(
        frame,
        text="Lakukan Uji Hipotesis",
        command=lakukan_uji_hipotesis,
        font=("Arial", 12, "bold"),
        bg="#4682B4",
        fg="white",
        padx=10,
        pady=5
    )
    btn_uji.pack(pady=20)

    # Tombol Kembali ke Menu Utama
    btn_kembali = tk.Button(
        frame,
        text="Kembali ke Menu Utama",
        command=lambda: (frame.pack_forget(), frame_utama()),
        font=("Arial", 12, "bold"),
        bg="#ff6b6b",
        fg="white",
        padx=10,
        pady=5
    )
    btn_kembali.pack(pady=10)

    return frame

def tampilkan_aplikasi(root, frame_utama):
    frame = uji_hipotesis_ragam(frame_utama, root)
    return frame
