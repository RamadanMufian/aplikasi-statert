import tkinter as tk
from tkinter import messagebox
import math

# Fungsi untuk menghitung dan menampilkan hasil uji proporsi
def hitung_ujian(entry_p0, entry_x, entry_n, entry_alpha):
    try:
        p0 = float(entry_p0.get())
        x = int(entry_x.get())
        n = int(entry_n.get())
        alpha = float(entry_alpha.get())

        # Validasi input
        if p0 < 0 or p0 > 1:
            raise ValueError("Proporsi populasi hipotesis (p0) harus antara 0 dan 1.")
        if x < 0:
            raise ValueError("Jumlah keberhasilan (x) harus positif atau nol.")
        if n <= 0 or x > n:
            raise ValueError("Ukuran sampel (n) harus positif dan x tidak boleh lebih besar dari n.")
        if alpha <= 0 or alpha >= 1:
            raise ValueError("Tingkat signifikansi (alpha) harus antara 0 dan 1.")

        # Hitung proporsi sampel
        phat = x / n

        # Tentukan jenis uji
        if phat < p0:
            test_type = 'l'  # Uji satu arah kiri
            test_desc = "Uji satu arah kiri (Left-Tailed Test)"
        elif phat > p0:
            test_type = 'r'  # Uji satu arah kanan
            test_desc = "Uji satu arah kanan (Right-Tailed Test)"
        else:
            test_type = 't'  # Uji dua arah
            test_desc = "Uji dua arah (Two-Tailed Test)"

        # Hitung statistik uji
        z = (phat - p0) / math.sqrt(p0 * (1 - p0) / n)

        # Tentukan nilai kritis
        if test_type == 't':
            zCritical = 1.96 if alpha == 0.05 else 2.58 if alpha == 0.01 else 0
        else:
            zCritical = 1.645 if alpha == 0.05 else 2.33 if alpha == 0.01 else 0

        # Tentukan keputusan pengujian
        if test_type == 't':
            keputusan = "Tolak H0" if abs(z) > zCritical else "Gagal menolak H0"
        elif test_type == 'l':
            keputusan = "Tolak H0" if z < -zCritical else "Gagal menolak H0"
        elif test_type == 'r':
            keputusan = "Tolak H0" if z > zCritical else "Gagal menolak H0"

        # Tampilkan hasil
        hasil = f"""
        Proporsi sampel (phat): {phat:.4f}
        Statistik uji (z): {z:.4f}
        Nilai z kritis: {zCritical:.4f}
        Jenis uji: {test_desc}
        Keputusan: {keputusan}
        """
        messagebox.showinfo("Hasil Uji Proporsi", hasil)

    except ValueError as e:
        messagebox.showerror("Kesalahan", str(e))


# Fungsi untuk menampilkan aplikasi dalam sebuah frame
def tampilkan_aplikasi(parent, on_back=None):
    frame = tk.Frame(parent, bg="#E8F6F3")

    # Judul
    judul = tk.Label(frame, text="Uji Proporsi Sampel", font=("Helvetica", 18, "bold"), bg="#1ABC9C", fg="white")
    judul.pack(pady=15, ipadx=10, ipady=5, fill="x")

    # Frame untuk input data
    frame_input = tk.LabelFrame(frame, text="Masukkan Data", font=("Helvetica", 12, "bold"), padx=10, pady=10, bg="#D4EFDF", fg="#34495E")
    frame_input.pack(padx=10, pady=10, fill="both")

    # Input data
    labels = [
        "Proporsi populasi hipotesis (p0):",
        "Jumlah keberhasilan dalam sampel (x):",
        "Ukuran sampel (n):",
        "Tingkat signifikansi (alpha):"
    ]
    entries = []
    for text in labels:
        label = tk.Label(frame_input, text=text, font=("Helvetica", 12, "bold"), bg="#D4EFDF")
        label.pack()
        entry = tk.Entry(frame_input, width=20, font=("Helvetica", 12), bg="white", relief="groove")
        entry.pack(pady=5)
        entries.append(entry)

    # Tombol Hitung
    btn_hitung = tk.Button(
        frame_input,
        text="Hitung",
        command=lambda: hitung_ujian(*entries),
        font=("Helvetica", 12, "bold"),
        bg="#1ABC9C",
        fg="white",
        activebackground="#16A085",
        activeforeground="white",
        padx=10,
        pady=5
    )
    btn_hitung.pack(pady=10)

    # Tombol Kembali
    if on_back:
        btn_back = tk.Button(
            frame,
            text="Kembali ke Menu Utama",
            command=lambda: (frame.pack_forget(), on_back()),  # Menyembunyikan frame ini
            font=("Helvetica", 12, "bold"),
            bg="#FF6B6B",
            fg="white",
            activebackground="#E74C3C",
            activeforeground="white",
            padx=10,
            pady=5
        )
        btn_back.pack(pady=10)

    return frame
