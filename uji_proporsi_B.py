import math
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung nilai Z-hitung
def calculate_z_score(p_sam, p0, n):
    if p0 <= 0 or p0 >= 1:
        raise ValueError("Proporsi populasi (p0) harus berada di antara 0 dan 1.")
    if n <= 0:
        raise ValueError("Ukuran sampel (n) harus lebih besar dari 0.")
    
    numerator = p_sam - p0
    denominator = math.sqrt(p0 * (1 - p0) / n)
    
    return numerator / denominator

# Fungsi distribusi normal kumulatif (CDF) untuk z
def normal_cdf(z):
    return (1.0 + math.erf(z / math.sqrt(2.0))) / 2.0

# Fungsi untuk menghitung nilai Z-kritis
def calculate_z_critical(alpha, direction):
    if direction == "two_sided":
        low, high = -10.0, 10.0
        target = 1 - alpha / 2
    elif direction == "right":
        low, high = 0.0, 10.0
        target = 1 - alpha
    elif direction == "left":
        low, high = -10.0, 0.0
        target = alpha
    else:
        raise ValueError("Jenis uji tidak valid.")
    
    while high - low > 1e-5:
        mid = (low + high) / 2
        if normal_cdf(mid) < target:
            low = mid
        else:
            high = mid
    return round(mid, 5)

# Fungsi untuk pengujian hipotesis
def perform_test(z_score, alpha, test_type):
    if test_type == "dua arah":
        z_critical = calculate_z_critical(alpha, "two_sided")
        decision = "Tolak H0" if abs(z_score) > z_critical else "Gagal menolak H0"
    elif test_type == "satu arah kanan":
        z_critical = calculate_z_critical(alpha, "right")
        decision = "Tolak H0" if z_score > z_critical else "Gagal menolak H0"
    elif test_type == "satu arah kiri":
        z_critical = calculate_z_critical(alpha, "left")
        decision = "Tolak H0" if z_score < z_critical else "Gagal menolak H0"
    else:
        raise ValueError("Jenis uji tidak valid.")
    return z_score, z_critical, decision

# Fungsi untuk aplikasi frame
def tampilkan_aplikasi(parent, on_back=None):
    frame = tk.Frame(parent, bg="#D6EAF8")

    # Input fields
    tk.Label(frame, text="Proporsi Populasi (p0):", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=5, padx=5)
    entry_p0 = tk.Entry(frame, font=("Helvetica", 12))
    entry_p0.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(frame, text="Proporsi Sampel (p_sam):", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", pady=5, padx=5)
    entry_psam = tk.Entry(frame, font=("Helvetica", 12))
    entry_psam.grid(row=1, column=1, pady=5, padx=5)

    tk.Label(frame, text="Ukuran Sampel (n):", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", pady=5, padx=5)
    entry_n = tk.Entry(frame, font=("Helvetica", 12))
    entry_n.grid(row=2, column=1, pady=5, padx=5)

    tk.Label(frame, text="Tingkat Signifikansi (α) (contoh 0.05):", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", pady=5, padx=5)
    entry_alpha = tk.Entry(frame, font=("Helvetica", 12))
    entry_alpha.grid(row=3, column=1, pady=5, padx=5)

    # Radio buttons for test type
    tk.Label(frame, text="Jenis Uji:", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=4, column=0, sticky="w", pady=5, padx=5)
    var_test_type = tk.StringVar(value="dua arah")
    tk.Radiobutton(frame, text="Dua Arah", variable=var_test_type, value="dua arah", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=4, column=1, sticky="w")
    tk.Radiobutton(frame, text="Satu Arah Kanan", variable=var_test_type, value="satu arah kanan", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=5, column=1, sticky="w")
    tk.Radiobutton(frame, text="Satu Arah Kiri", variable=var_test_type, value="satu arah kiri", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=6, column=1, sticky="w")

    # Fungsi untuk menghitung
    def calculate():
        try:
            p0 = float(entry_p0.get())
            p_sam = float(entry_psam.get())
            n = int(entry_n.get())
            alpha = float(entry_alpha.get())
            test_type = var_test_type.get()

            if not (0 < alpha < 1):
                raise ValueError("Alpha harus antara 0 dan 1.")

            z_score = calculate_z_score(p_sam, p0, n)
            z_score, z_critical, decision = perform_test(z_score, alpha, test_type)

            messagebox.showinfo(
                "Hasil",
                f"Nilai Z-hitung: {z_score}\n"
                f"Nilai Z-kritis: {z_critical}\n"
                f"Keputusan: {decision}"
            )
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Tombol Hitung
    tk.Button(
        frame, 
        text="Hitung", 
        command=calculate, 
        font=("Helvetica", 12), 
        bg="#5DADE2", 
        fg="white"
    ).grid(row=7, column=0, columnspan=2, pady=10)

    # Tombol Kembali
    if on_back:
        def handle_back():
            frame.pack_forget()  # Sembunyikan frame saat ini
            on_back()  # Panggil fungsi kembali ke menu utama

        tk.Button(
            frame, 
            text="Kembali", 
            command=handle_back, 
            font=("Helvetica", 12), 
            bg="#FF6B6B", 
            fg="white"
        ).grid(row=8, column=0, columnspan=2, pady=10)

    return frame
