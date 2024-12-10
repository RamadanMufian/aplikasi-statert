import tkinter as tk
from tkinter import messagebox
import math
from scipy.stats import norm, t

# Fungsi Z-test (Varians Populasi Diketahui)
def z_test(x1, x2, mu_diff, sigma1, sigma2, n1, n2):
    numerator = (x1 - x2) - mu_diff
    denominator = math.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
    return numerator / denominator

# Fungsi T-test dengan pooled variance (Varians Populasi Tidak Diketahui dan Sama)
def t_test_pooled(x1, x2, mu_diff, s1, s2, n1, n2):
    sp2 = ((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2)
    numerator = (x1 - x2) - mu_diff
    denominator = math.sqrt(sp2 * (1 / n1 + 1 / n2))
    return numerator / denominator

# Fungsi Welch's T-test (Varians Populasi Tidak Diketahui dan Tidak Sama)
def welch_t_test(x1, x2, mu_diff, s1, s2, n1, n2):
    numerator = (x1 - x2) - mu_diff
    var1 = s1**2 / n1
    var2 = s2**2 / n2
    denominator = math.sqrt(var1 + var2)
    t_stat = numerator / denominator

    # Derajat kebebasan Welch-Satterthwaite
    df = ((var1 + var2)**2) / ((var1**2) / (n1 - 1) + (var2**2) / (n2 - 1))
    return t_stat, df

# Fungsi Paired T-test (Pasangan Dependen)
def paired_t_test(d_mean, d0, sd, n):
    return (d_mean - d0) / (sd / math.sqrt(n))

# Fungsi untuk menentukan keputusan berdasarkan hipotesis
def uji_hipotesis(statistik, df, alpha, hipotesis):
    if hipotesis == "Kanan":
        kritis = t.ppf(1 - alpha, df) if df else norm.ppf(1 - alpha)
        keputusan = "Menolak H0" if statistik > kritis else "Gagal Menolak H0"
    elif hipotesis == "Kiri":
        kritis = t.ppf(alpha, df) if df else norm.ppf(alpha)
        keputusan = "Menolak H0" if statistik < kritis else "Gagal Menolak H0"
    else:  # Dua sisi
        kritis = t.ppf(1 - alpha / 2, df) if df else norm.ppf(1 - alpha / 2)
        keputusan = "Menolak H0" if abs(statistik) > kritis else "Gagal Menolak H0"
    return kritis, keputusan

# Fungsi untuk menampilkan frame GUI
def tampilkan_aplikasi(root, kembali_ke_menu):
    frame = tk.Frame(root, bg="#FAF3E3")
    frame.pack(fill="both", expand=True)

    # Judul aplikasi
    tk.Label(frame, text="Pengujian Hipotesis Rataan 2 Populasi", font=("Arial", 18, "bold"), bg="#FFB700").pack(pady=15, ipadx=10, ipady=5, fill="x")

    # Fungsi untuk memproses pengujian statistik
    def lakukan_uji(uji_type, entries, alpha, hipotesis):
        try:
            alpha = float(alpha)
            if uji_type == "Varians Populasi Diketahui (Z-test)":
               x1, x2, mu_diff, sigma1, sigma2, n1, n2 = map(float, entries)
               hasil = z_test(x1, x2, mu_diff, sigma1, sigma2, int(n1), int(n2))
               kritis, keputusan = uji_hipotesis(hasil, None, alpha, hipotesis)
               messagebox.showinfo("Hasil Z-test", f"Statistik Z: {hasil:.4f}\nNilai kritis: {kritis:.4f}\nKeputusan: {keputusan}\n\nDegrees of Freedom: N/A")

            elif uji_type == "Varians Populasi Tidak Diketahui dan Sama (T-test Pooled Variance)":
                x1, x2, mu_diff, s1, s2, n1, n2 = map(float, entries)
                df = int(n1 + n2 - 2)
                hasil = t_test_pooled(x1, x2, mu_diff, s1, s2, int(n1), int(n2))
                kritis, keputusan = uji_hipotesis(hasil, df, alpha, hipotesis)
                messagebox.showinfo("Hasil T-test (Pooled Variance)", f"Statistik T: {hasil:.4f}\nNilai kritis: {kritis:.4f}\nKeputusan: {keputusan}\n\nDegrees of Freedom: {df}")
  
            elif uji_type == "Varians Populasi Tidak Diketahui dan Tidak Sama (Welch's T-test)":
                x1, x2, mu_diff, s1, s2, n1, n2 = map(float, entries)
                hasil, df = welch_t_test(x1, x2, mu_diff, s1, s2, int(n1), int(n2))
                kritis, keputusan = uji_hipotesis(hasil, int(df), alpha, hipotesis)
                messagebox.showinfo("Hasil Welch's T-test", f"Statistik T: {hasil:.4f}\nNilai kritis: {kritis:.4f}\nKeputusan: {keputusan}\n\nDegrees of Freedom: {df:.2f}")

            elif uji_type == "Pasangan Dependen (Paired T-test)":
                d_mean, d0, sd, n = map(float, entries)
                df = int(n - 1)
                hasil = paired_t_test(d_mean, d0, sd, int(n))
                kritis, keputusan = uji_hipotesis(hasil, df, alpha, hipotesis)
                messagebox.showinfo("Hasil Paired T-test", f"Statistik T: {hasil:.4f}\nNilai kritis: {kritis:.4f}\nKeputusan: {keputusan}\n\nDegrees of Freedom: {df}")

        except ValueError:
            messagebox.showerror("Error", "Pastikan semua input valid.")

    # Fungsi untuk menampilkan input sesuai jenis uji
    def tampilkan_frame(uji_type, fields):
        for widget in frame.winfo_children():
            widget.destroy()

        tk.Label(frame, text=f"{uji_type}", font=("Arial", 14, "bold"), bg="#FAF3E3", fg="#4C4C4C").pack(pady=10, ipadx=10, ipady=5, fill="x")

        entries = []
        for field in fields:
            tk.Label(frame, text=field, font=("Arial", 10), bg="#FAF3E3").pack(pady=3)
            entry = tk.Entry(frame, width=35, font=("Arial", 10))
            entry.pack(pady=3, ipady=3)
            entries.append(entry)

        tk.Label(frame, text="Tingkat Signifikansi (α)", font=("Arial", 10), bg="#FAF3E3").pack(pady=3)
        alpha_entry = tk.Entry(frame, width=35, font=("Arial", 10))
        alpha_entry.pack(pady=3, ipady=3)

        tk.Label(frame, text="Hipotesis", font=("Arial", 10), bg="#FAF3E3").pack(pady=3)
        hipotesis_var = tk.StringVar(value="Hipotesis")
        tk.OptionMenu(frame, hipotesis_var, "Kanan", "Kiri", "Dua sisi").pack(pady=5)

        tk.Button(frame, text="Hitung", bg="#A3D8F4", fg="black", font=("Arial", 10, "bold"),
                  command=lambda: lakukan_uji(uji_type, [e.get() for e in entries], alpha_entry.get(), hipotesis_var.get())).pack(pady=15)

        tk.Button(frame, text="Kembali ke Menu", bg="#FFC3A1", fg="black", font=("Arial", 10, "bold"), command=tampilkan_menu).pack(pady=10)

    # Menu utama pengujian
    def tampilkan_menu():
        for widget in frame.winfo_children():
            widget.destroy()

        tk.Label(frame, text="Aplikasi Pengujian Statistik", font=("Arial", 16, "bold"), bg="#FFB700", fg="#4C4C4C").pack(pady=10, ipadx=10, ipady=5, fill="x")

        tk.Button(frame, text="1. Varians Populasi Diketahui (Z-test)", bg="#A3D8F4", fg="black", font=("Arial", 10, "bold"),
                  command=lambda: tampilkan_frame("Varians Populasi Diketahui (Z-test)", ["X1", "X2", "Perbedaan rata-rata (mu_diff)", "Sigma1", "Sigma2", "Ukuran sampel N1", "Ukuran sampel N2"])).pack(pady=5)

        tk.Button(frame, text="2. Varians Populasi Tidak Diketahui dan Sama (T-test Pooled Variance)", bg="#A3D8F4", fg="black", font=("Arial", 10, "bold"),
                  command=lambda: tampilkan_frame("Varians Populasi Tidak Diketahui dan Sama (T-test Pooled Variance)", ["X1", "X2", "Perbedaan rata-rata (mu_diff)", "S1", "S2", "Ukuran sampel N1", "Ukuran sampel N2"])).pack(pady=5)

        tk.Button(frame, text="3. Varians Populasi Tidak Diketahui dan Tidak Sama (Welch's T-test)", bg="#A3D8F4", fg="black", font=("Arial", 10, "bold"),
                  command=lambda: tampilkan_frame("Varians Populasi Tidak Diketahui dan Tidak Sama (Welch's T-test)", ["X1", "X2", "Perbedaan rata-rata (mu_diff)", "S1", "S2", "Ukuran sampel N1", "Ukuran sampel N2"])).pack(pady=5)

        tk.Button(frame, text="4. Pasangan Dependen (Paired T-test)", bg="#A3D8F4", fg="black", font=("Arial", 10, "bold"),
                  command=lambda: tampilkan_frame("Pasangan Dependen (Paired T-test)", ["Rata-rata perbedaan (d_mean)", "Nilai d0", "Standar deviasi perbedaan (Sd)", "Ukuran sampel N"])).pack(pady=5)
        
        tk.Button(frame, text="Kembali ke Menu Utama", bg="#FFC3A1", fg="black", font=("Arial", 10, "bold"), command=kembali_ke_menu_fully).pack(pady=15)
    
    # Fungsi untuk kembali ke menu utama dengan menghapus frame sepenuhnya
    def kembali_ke_menu_fully():
        frame.destroy()  # Hapus frame sepenuhnya
        kembali_ke_menu()  # Panggil menu utama

    tampilkan_menu()
    return frame
