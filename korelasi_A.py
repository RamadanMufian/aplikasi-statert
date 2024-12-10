import tkinter as tk
from tkinter import ttk, messagebox
import math

def tampilkan_aplikasi(root, kembali_ke_menu):
    def cetak_komponen(X, Y, n):
        sumX = sumY = sumXY = sumX2 = sumY2 = 0
        tabel = []

        for i in range(n):
            XY = X[i] * Y[i]
            X2 = X[i] ** 2
            Y2 = Y[i] ** 2

            sumX += X[i]
            sumY += Y[i]
            sumXY += XY
            sumX2 += X2
            sumY2 += Y2

            tabel.append((i + 1, X[i], Y[i], XY, X2, Y2))

        tabel.append(("TOT", sumX, sumY, sumXY, sumX2, sumY2))
        return tabel

    def hitung_korelasi(X, Y, n):
        sumX = sumY = sumXY = sumX2 = sumY2 = 0

        for i in range(n):
            sumX += X[i]
            sumY += Y[i]
            sumXY += X[i] * Y[i]
            sumX2 += X[i] ** 2
            sumY2 += Y[i] ** 2

        numerator = n * sumXY - (sumX * sumY)
        denominator = math.sqrt((n * sumX2 - sumX ** 2) * (n * sumY2 - sumY ** 2))

        if denominator == 0:
            messagebox.showerror("Error", "Pembagi adalah nol. Tidak dapat menghitung korelasi.")
            return None, None, None

        return numerator, denominator, numerator / denominator

    def uji_hipotesis(r, n, alpha):
        if n <= 2:
            return "Data tidak cukup untuk uji hipotesis (n harus lebih besar dari 2)."

        t = (r * math.sqrt(n - 2)) / math.sqrt(1 - r ** 2)
        t_krit = 2.306  # Contoh nilai kritis untuk alpha = 0.05 dan df = 10

        if abs(t) > t_krit:
            return f"Tolak H0. Terdapat hubungan linear signifikan antara X dan Y. (t = {t:.4f})"
        else:
            return f"Gagal menolak H0. Tidak terdapat hubungan linear signifikan antara X dan Y. (t = {t:.4f})"

    def proses_data():
        try:
            X = list(map(int, entry_X.get().split()))
            Y = list(map(int, entry_Y.get().split()))
            n = len(X)

            if n != len(Y):
                messagebox.showerror("Error", "Jumlah elemen X dan Y harus sama.")
                return

            if n <= 1:
                messagebox.showerror("Error", "Jumlah data harus lebih dari 1 untuk menghitung korelasi.")
                return

            tabel = cetak_komponen(X, Y, n)
            tabel_tree.delete(*tabel_tree.get_children())
            for row in tabel:
                tabel_tree.insert("", "end", values=row)

            numerator, denominator, r = hitung_korelasi(X, Y, n)
            if r is not None:
                hasil_korelasi.set(f"Koefisien Korelasi (r): {r:.4f}")
                interpretasi = "Positif" if r > 0 else "Negatif" if r < 0 else "Tidak ada hubungan linear"
                hasil_interpretasi.set(f"Hubungan: {interpretasi}")
                hasil_hipotesis.set(uji_hipotesis(r, n, 0.05))

                hasil_numerator.set(f"Numerator: {numerator:.4f}")
                hasil_denominator.set(f"Denominator: {denominator:.4f}")

        except ValueError:
            messagebox.showerror("Error", "Pastikan input hanya berupa angka yang dipisahkan spasi.")

    # Membuat frame untuk aplikasi
    frame = tk.Frame(root, bg="#F8F9FA")

    # Judul
    tk.Label(frame, text="Kalkulator Korelasi", font=("Arial", 16, "bold"), bg="#F8F9FA").pack(pady=10)

    # Input Data X
    frame_X = tk.Frame(frame, bg="#F8F9FA")
    frame_X.pack(pady=5)
    tk.Label(frame_X, text="Masukkan nilai X (pisahkan dengan spasi):", font=("Arial", 10), bg="#F8F9FA").pack(side=tk.LEFT, padx=5)
    entry_X = tk.Entry(frame_X, width=50)
    entry_X.pack(side=tk.LEFT)

    # Input Data Y
    frame_Y = tk.Frame(frame, bg="#F8F9FA")
    frame_Y.pack(pady=5)
    tk.Label(frame_Y, text="Masukkan nilai Y (pisahkan dengan spasi):", font=("Arial", 10), bg="#F8F9FA").pack(side=tk.LEFT, padx=5)
    entry_Y = tk.Entry(frame_Y, width=50)
    entry_Y.pack(side=tk.LEFT)

    # Tombol Hitung
    tk.Button(frame, text="Hitung Korelasi", font=("Arial", 12), bg="#4CAF50", fg="white", command=proses_data).pack(pady=10)

    # Tabel Komponen
    tk.Label(frame, text="Komponen Perhitungan:", font=("Arial", 12, "bold"), bg="#F8F9FA").pack(pady=5)
    columns = ("No.", "X", "Y", "XY", "X^2", "Y^2")
    tabel_tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
    for col in columns:
        tabel_tree.heading(col, text=col)
        tabel_tree.column(col, anchor=tk.CENTER, width=100)
    tabel_tree.pack(pady=5)

    # Hasil Korelasi
    hasil_korelasi = tk.StringVar()
    tk.Label(frame, textvariable=hasil_korelasi, font=("Arial", 12), fg="#333", bg="#F8F9FA").pack(pady=5)

    # Interpretasi Korelasi
    hasil_interpretasi = tk.StringVar()
    tk.Label(frame, textvariable=hasil_interpretasi, font=("Arial", 12), fg="#333", bg="#F8F9FA").pack(pady=5)

    # Uji Hipotesis
    hasil_hipotesis = tk.StringVar()
    tk.Label(frame, textvariable=hasil_hipotesis, font=("Arial", 12), fg="#333", bg="#F8F9FA").pack(pady=5)

    # Hasil Numerator dan Denominator
    hasil_numerator = tk.StringVar()
    tk.Label(frame, textvariable=hasil_numerator, font=("Arial", 12), fg="#333", bg="#F8F9FA").pack(pady=5)

    hasil_denominator = tk.StringVar()
    tk.Label(frame, textvariable=hasil_denominator, font=("Arial", 12), fg="#333", bg="#F8F9FA").pack(pady=5)

    # Tombol Kembali
    def kembali():
        frame.destroy()  # Menghapus frame ini
        kembali_ke_menu()  # Menampilkan kembali menu utama

    tk.Button(frame, text="Kembali ke Menu Utama", font=("Arial", 12), bg="#ff6b6b", fg="white", command=kembali).pack(pady=20)

    return frame
