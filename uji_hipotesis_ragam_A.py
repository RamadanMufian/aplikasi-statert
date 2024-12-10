import numpy as np
from scipy.stats import f
import tkinter as tk
from tkinter import ttk, messagebox

def test_equality_of_variances(entry_s1, entry_s2, entry_alpha):
    """
    Melakukan uji F untuk kesamaan ragam dua populasi.
    """
    try:
        # Mengonversi input string ke array float
        s1 = np.array([float(x) for x in entry_s1.get().split(",")])
        s2 = np.array([float(x) for x in entry_s2.get().split(",")])
        alpha = float(entry_alpha.get())

        # Menghitung nilai F-statistik
        f_stat = np.var(s1, ddof=1) / np.var(s2, ddof=1)
        df1 = len(s1) - 1
        df2 = len(s2) - 1

        # Menghitung p-value
        p_value = 2 * min(f.cdf(f_stat, df1, df2), 1 - f.cdf(f_stat, df1, df2))

        # Menentukan hasil berdasarkan nilai alpha
        if p_value > alpha:
            result = f"Terima H0: Ragam kedua populasi sama.\nF-statistik: {f_stat:.4f}\np-value: {p_value:.4f}\nDF1: {df1}, DF2: {df2}"
        else:
            result = f"Tolak H0: Ragam kedua populasi tidak sama.\nF-statistik: {f_stat:.4f}\np-value: {p_value:.4f}\nDF1: {df1}, DF2: {df2}"

        messagebox.showinfo("Hasil Uji F", result)
    except ValueError:
        messagebox.showerror("Kesalahan Input", "Masukkan angka yang valid dan pisahkan dengan koma.")

def tampilkan_aplikasi(root, kembali_ke_menu):
    """
    Menampilkan antarmuka untuk uji F kesamaan ragam.
    """
    frame = tk.Frame(root, bg="#E3F2FD")
    frame.pack(fill="both", expand=True)

    # Penyesuaian font dan tampilan
    label_font = ("Helvetica", 12, "bold")
    entry_font = ("Helvetica", 12)
    judul_font = ("Helvetica", 18, "bold")
    button_font = ("Helvetica", 12, "bold")

    # Membuat label judul
    judul = tk.Label(frame, text="Uji Kesamaan Ragam", font=judul_font, bg="#2196F3", fg="white")
    judul.pack(pady=15, ipadx=10, ipady=5, fill="x")

    # Frame untuk input data
    frame_input = tk.Frame(frame, bg="#BBDEFB", pady=10)
    frame_input.pack(padx=20, pady=20)

    # Label dan entry untuk populasi 1
    tk.Label(frame_input, text="Data Populasi 1 (pisahkan dengan koma):", font=label_font, bg="#BBDEFB").pack(anchor="w", pady=5)
    entry_s1 = tk.Entry(frame_input, width=50, font=entry_font)
    entry_s1.pack(pady=5)

    # Label dan entry untuk populasi 2
    tk.Label(frame_input, text="Data Populasi 2 (pisahkan dengan koma):", font=label_font, bg="#BBDEFB").pack(anchor="w", pady=5)
    entry_s2 = tk.Entry(frame_input, width=50, font=entry_font)
    entry_s2.pack(pady=5)

    # Label dan entry untuk alpha
    tk.Label(frame_input, text="Taraf Signifikansi (α):", font=label_font, bg="#BBDEFB").pack(anchor="w", pady=5)
    entry_alpha = tk.Entry(frame_input, width=50, font=entry_font)
    entry_alpha.pack(pady=5)

    # Tombol untuk menghitung uji F
    tk.Button(
        frame, text="Lakukan Uji F", font=button_font, bg="#2196F3", fg="white",
        activebackground="#1976D2", activeforeground="white",
        command=lambda: test_equality_of_variances(entry_s1, entry_s2, entry_alpha)
    ).pack(pady=20)

    # Tombol untuk kembali ke menu utama
    tk.Button(
        frame, text="Kembali ke Menu Utama", font=button_font, bg="#FF6B6B", fg="white",
        activebackground="#E74C3C", activeforeground="white",
        command=lambda: (frame.pack_forget(), kembali_ke_menu())
    ).pack(pady=10)

    return frame

# Contoh penggunaan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Aplikasi Statistik")
    root.geometry("600x400")
    root.configure(bg="#E3F2FD")

    def kembali_ke_menu():
        # Fungsi placeholder untuk kembali ke menu
        pass

    tampilkan_aplikasi(root, kembali_ke_menu)
    root.mainloop()
