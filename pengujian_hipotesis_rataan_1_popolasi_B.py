import tkinter as tk
from tkinter import messagebox
import math

# Fungsi untuk menghitung Z dan T
def hitung_z_sigma_diketahui(x_bar, mu0, sigma, n):
    return (x_bar - mu0) / (sigma / math.sqrt(n))

def hitung_z_sigma_tidak_diketahui(x_bar, mu0, s, n):
    return (x_bar - mu0) / (s / math.sqrt(n))

def hitung_t_sigma_tidak_diketahui(x_bar, mu0, s, n):
    return (x_bar - mu0) / (s / math.sqrt(n))

def hitung_z_sigma_diketahui_sampel_kecil(x_bar, mu0, sigma, n):
    return (x_bar - mu0) / (sigma / math.sqrt(n))

# Fungsi untuk menampilkan aplikasi
def tampilkan_aplikasi(root, kembali_callback):
    """
    Menampilkan GUI aplikasi pengujian hipotesis rataan 1 populasi.

    Parameters:
        root: tk.Tk atau tk.Frame, frame root utama aplikasi.
        kembali_callback: fungsi untuk kembali ke menu utama.
    """
    # Buat frame baru untuk aplikasi
    frame = tk.Frame(root, bg="#f4f4f9")

    # Header
    tk.Label(frame, text="Pengujian Hipotesis Rataan 1 Populasi", font=("Arial", 16, "bold"), bg="#f4f4f9").pack(pady=10)

    # Frame pilihan jenis pengujian
    frame_pilihan = tk.Frame(frame, bg="#f4f4f9")
    frame_pilihan.pack(pady=10)

    var = tk.IntVar()
    tk.Label(frame_pilihan, text="Pilih jenis pengujian:", font=("Arial", 12), bg="#f4f4f9").pack(anchor="w")
    tk.Radiobutton(frame_pilihan, text="Sampel Besar (Sigma Diketahui)", variable=var, value=1, bg="#f4f4f9").pack(anchor="w")
    tk.Radiobutton(frame_pilihan, text="Sampel Besar (Sigma Tidak Diketahui)", variable=var, value=2, bg="#f4f4f9").pack(anchor="w")
    tk.Radiobutton(frame_pilihan, text="Sampel Kecil (Sigma Tidak Diketahui)", variable=var, value=3, bg="#f4f4f9").pack(anchor="w")
    tk.Radiobutton(frame_pilihan, text="Sampel Kecil (Sigma Diketahui)", variable=var, value=4, bg="#f4f4f9").pack(anchor="w")

    # Frame input
    frame_input = tk.Frame(frame, bg="#f4f4f9")
    frame_input.pack(pady=10)

    tk.Label(frame_input, text="Rata-rata sampel (x̄):", bg="#f4f4f9").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_xbar = tk.Entry(frame_input, width=30)
    entry_xbar.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Rata-rata populasi (μ0):", bg="#f4f4f9").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entry_mu0 = tk.Entry(frame_input, width=30)
    entry_mu0.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Ukuran sampel (n):", bg="#f4f4f9").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    entry_n = tk.Entry(frame_input, width=30)
    entry_n.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Simpangan baku populasi (σ):", bg="#f4f4f9").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    entry_sigma = tk.Entry(frame_input, width=30)
    entry_sigma.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Simpangan baku sampel (s):", bg="#f4f4f9").grid(row=4, column=0, sticky="w", padx=5, pady=5)
    entry_s = tk.Entry(frame_input, width=30)
    entry_s.grid(row=4, column=1, padx=5, pady=5)

    # Fungsi untuk menghitung hasil
    def hitung():
        try:
            x_bar = float(entry_xbar.get())
            mu0 = float(entry_mu0.get())
            n = int(entry_n.get())
            pilihan = var.get()

            if pilihan == 1:
                sigma = float(entry_sigma.get())
                hasil = hitung_z_sigma_diketahui(x_bar, mu0, sigma, n)
                label_hasil.config(text=f"Nilai Z-hitung: {hasil:.4f}", fg="blue")
            elif pilihan == 2:
                s = float(entry_s.get())
                hasil = hitung_z_sigma_tidak_diketahui(x_bar, mu0, s, n)
                label_hasil.config(text=f"Nilai Z-hitung: {hasil:.4f}", fg="blue")
            elif pilihan == 3:
                s = float(entry_s.get())
                hasil = hitung_t_sigma_tidak_diketahui(x_bar, mu0, s, n)
                label_hasil.config(text=f"Nilai T-hitung: {hasil:.4f}", fg="blue")
            elif pilihan == 4:
                sigma = float(entry_sigma.get())
                hasil = hitung_z_sigma_diketahui_sampel_kecil(x_bar, mu0, sigma, n)
                label_hasil.config(text=f"Nilai Z-hitung: {hasil:.4f}", fg="blue")
            else:
                messagebox.showerror("Error", "Pilih jenis pengujian terlebih dahulu!")
        except ValueError:
            messagebox.showerror("Error", "Harap masukkan nilai yang valid!")
            

    # Tombol untuk menghitung
    tk.Button(frame, text="Hitung", font=("Arial", 12), command=hitung).pack(pady=10)

    # Label hasil
    label_hasil = tk.Label(frame, text="Hasil akan ditampilkan di sini.", font=("Arial", 12), bg="#f4f4f9")
    label_hasil.pack(pady=10)
    

    # Tombol kembali
    def kembali():
        frame.pack_forget()  # Sembunyikan frame aplikasi
        kembali_callback()   # Kembali ke menu utama

    tk.Button(frame, text="Kembali ke Menu Utama", font=("Arial", 12), bg="#ff6b6b", fg="white", command=kembali).pack(pady=20)
    # Muat gambar background
    return frame
