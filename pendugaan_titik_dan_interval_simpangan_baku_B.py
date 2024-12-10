import tkinter as tk
from tkinter import messagebox
import math

# Fungsi untuk menghitung data tunggal
def hitung_data_tunggal(entry):
    try:
        data = list(map(float, entry.get().split(',')))
        n = len(data)
        
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std_deviation = math.sqrt(variance)

        hasil = f"Mean: {mean:.2f}\nVarian: {variance:.2f}\nSimpangan Baku: {std_deviation:.2f}"
        messagebox.showinfo("Hasil Perhitungan Data Tunggal", hasil)
    except ValueError:
        messagebox.showerror("Error", "Masukkan data dalam format yang benar (pisahkan dengan koma).")

# Fungsi untuk menghitung data kelompok
def hitung_data_kelompok(entry_lower, entry_upper, entry_freq):
    try:
        lower_bound = float(entry_lower.get())
        upper_bound = float(entry_upper.get())
        range_class = upper_bound - lower_bound

        frequencies = list(map(float, entry_freq.get().split(',')))
        n = len(frequencies)

        midpoints = []
        for i in range(n):
            mid = (lower_bound + upper_bound) / 2
            midpoints.append(mid)
            lower_bound = upper_bound
            upper_bound = lower_bound + range_class

        total_frequency = sum(frequencies)
        mean = sum(f * m for f, m in zip(frequencies, midpoints)) / total_frequency
        variance = sum(f * (m - mean) ** 2 for f, m in zip(frequencies, midpoints)) / total_frequency
        std_deviation = math.sqrt(variance)

        hasil = f"Mean: {mean:.2f}\nVarian: {variance:.2f}\nSimpangan Baku: {std_deviation:.2f}"
        messagebox.showinfo("Hasil Perhitungan Data Kelompok", hasil)
    except ValueError:
        messagebox.showerror("Error", "Masukkan data dalam format yang benar.")

# Fungsi untuk menampilkan aplikasi
def tampilkan_aplikasi(root, kembali_ke_menu):
    frame = tk.Frame(root, bg="#E8F6F3")
    frame.pack(fill="both", expand=True)

    # Gaya label dan entry
    label_font = ("Helvetica", 12, "bold")
    entry_font = ("Helvetica", 12)
    judul_font = ("Helvetica", 18, "bold")
    button_font = ("Helvetica", 12, "bold")

    # Judul
    judul = tk.Label(frame, text="pendugaan titik dan interval simpangan baku", font=judul_font, bg="#1ABC9C", fg="white")
    judul.pack(pady=15, ipadx=10, ipady=5, fill="x")

    # Tab untuk Data Tunggal
    frame_tunggal = tk.LabelFrame(frame, text="Data Tunggal", font=label_font, padx=10, pady=10, bg="#D4EFDF", fg="#34495E")
    frame_tunggal.pack(padx=10, pady=10, fill="both")

    label_data_tunggal = tk.Label(frame_tunggal, text="Masukkan data (pisahkan dengan koma):", font=label_font, bg="#D4EFDF")
    label_data_tunggal.pack()
    entry_data_tunggal = tk.Entry(frame_tunggal, width=50, font=entry_font, bg="white", relief="groove")
    entry_data_tunggal.pack(pady=5)
    btn_tunggal = tk.Button(frame_tunggal, text="Hitung", command=lambda: hitung_data_tunggal(entry_data_tunggal),
                            font=button_font, bg="#1ABC9C", fg="white", activebackground="#16A085",
                            activeforeground="white", padx=10, pady=5)
    btn_tunggal.pack(pady=5)

    # Tab untuk Data Kelompok
    frame_kelompok = tk.LabelFrame(frame, text="Data Kelompok", font=label_font, padx=10, pady=10, bg="#D4EFDF", fg="#34495E")
    frame_kelompok.pack(padx=10, pady=10, fill="both")

    label_lower_bound = tk.Label(frame_kelompok, text="Batas bawah kelas pertama:", font=label_font, bg="#D4EFDF")
    label_lower_bound.pack()
    entry_lower_bound = tk.Entry(frame_kelompok, width=20, font=entry_font, bg="white", relief="groove")
    entry_lower_bound.pack(pady=5)

    label_upper_bound = tk.Label(frame_kelompok, text="Batas atas kelas pertama:", font=label_font, bg="#D4EFDF")
    label_upper_bound.pack()
    entry_upper_bound = tk.Entry(frame_kelompok, width=20, font=entry_font, bg="white", relief="groove")
    entry_upper_bound.pack(pady=5)

    label_frequencies = tk.Label(frame_kelompok, text="Frekuensi setiap kelas (pisahkan dengan koma):", font=label_font, bg="#D4EFDF")
    label_frequencies.pack()
    entry_frequencies = tk.Entry(frame_kelompok, width=50, font=entry_font, bg="white", relief="groove")
    entry_frequencies.pack(pady=5)

    btn_kelompok = tk.Button(frame_kelompok, text="Hitung", command=lambda: hitung_data_kelompok(entry_lower_bound, entry_upper_bound, entry_frequencies),
                             font=button_font, bg="#1ABC9C", fg="white", activebackground="#16A085",
                             activeforeground="white", padx=10, pady=5)
    btn_kelompok.pack(pady=5)

    # Tombol kembali ke menu utama
    if kembali_ke_menu:
        btn_kembali = tk.Button(frame, text="Kembali ke Menu Utama", command=lambda: (frame.pack_forget(), kembali_ke_menu()),
                                font=button_font, bg="#FF6B6B", fg="white", activebackground="#E74C3C",
                                activeforeground="white", padx=10, pady=5)
        btn_kembali.pack(pady=10)

    return frame
