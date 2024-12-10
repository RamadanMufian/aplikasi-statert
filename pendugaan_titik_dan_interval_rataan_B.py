import tkinter as tk
from tkinter import messagebox
import math
import scipy.stats as stats

# Fungsi Kalkulasi
def hitung_mean(data):
    return sum(data) / len(data)

def hitung_interval_satu_rata_diketahui(mean, sigma, n, alpha_percent):
    alpha = 1 - (alpha_percent / 100)
    z = stats.norm.ppf(1 - alpha / 2)
    margin_of_error = z * (sigma / math.sqrt(n))
    return mean - margin_of_error, mean + margin_of_error

def hitung_interval_satu_rata_tidak_diketahui(mean, s, n, alpha_percent):
    alpha = 1 - (alpha_percent / 100)
    z = stats.norm.ppf(1 - alpha / 2)
    margin_of_error = z * (s / math.sqrt(n))
    return mean - margin_of_error, mean + margin_of_error

def hitung_interval_satu_rata_t_dengan_sampel_kecil(mean, s, n, alpha_percent):
    alpha = 1 - (alpha_percent / 100)
    t = stats.t.ppf(1 - alpha / 2, df=n - 1)
    margin_of_error = t * (s / math.sqrt(n))
    return mean - margin_of_error, mean + margin_of_error

def hitung_interval_dua_rata_diketahui(mean1, mean2, sigma1, sigma2, n1, n2, alpha_percent):
    alpha = 1 - (alpha_percent / 100)
    z = stats.norm.ppf(1 - alpha / 2)
    margin_of_error = z * math.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
    diff = mean1 - mean2
    return diff - margin_of_error, diff + margin_of_error

def hitung_interval_dua_rata_tidak_diketahui_sama(mean1, mean2, s1, s2, n1, n2, alpha_percent):
    alpha = 1 - (alpha_percent / 100)
    t = stats.t.ppf(1 - alpha / 2, df=n1 + n2 - 2)
    pooled_variance = ((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2)
    margin_of_error = t * math.sqrt(pooled_variance * (1/n1 + 1/n2))
    diff = mean1 - mean2
    return diff - margin_of_error, diff + margin_of_error

def hitung_interval_dua_rata_tidak_diketahui_berbeda(mean1, mean2, s1, s2, n1, n2, alpha_percent):
    alpha = 1 - (alpha_percent / 100)
    dof = ((s1**2 / n1) + (s2**2 / n2))**2 / (((s1**2 / n1)**2 / (n1 - 1)) + ((s2**2 / n2)**2 / (n2 - 1)))
    t = stats.t.ppf(1 - alpha / 2, df=dof)
    margin_of_error = t * math.sqrt((s1**2 / n1) + (s2**2 / n2))
    diff = mean1 - mean2
    return diff - margin_of_error, diff + margin_of_error

def hitung_interval_dua_rata_saling_tidak_bebas_kecil(d_mean, s_d, n, alpha_percent):
    alpha = 1 - (alpha_percent / 100)
    t = stats.t.ppf(1 - alpha / 2, df=n - 1)
    margin_of_error = t * s_d / math.sqrt(n)
    return d_mean - margin_of_error, d_mean + margin_of_error

def hitung_interval_dua_rata_saling_tidak_bebas_besar(d_mean, s_d, n, alpha_percent):
    alpha = 1 - (alpha_percent / 100)
    z = stats.norm.ppf(1 - alpha / 2)
    margin_of_error = z * s_d / math.sqrt(n)
    return d_mean - margin_of_error, d_mean + margin_of_error

def hitung_interval_dua_proporsi(p1, p2, n1, n2, alpha_percent):
    p = (p1 * n1 + p2 * n2) / (n1 + n2)
    alpha = 1 - (alpha_percent / 100)
    z = stats.norm.ppf(1 - alpha / 2)
    margin_of_error = z * math.sqrt(p * (1 - p) * (1/n1 + 1/n2))
    return (p1 - p2) - margin_of_error, (p1 - p2) + margin_of_error


# Fungsi untuk membersihkan frame
def kosongkan_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Fungsi untuk menampilkan hasil dalam messagebox
def tampilkan_hasil(hasil):
    messagebox.showinfo("Hasil", f"Hasil: {hasil}")

# Fungsi untuk menampilkan menu utama
def tampilkan_menu(frame):
    kosongkan_frame(frame)
    tk.Label(frame, text="Pilih jenis kalkulasi:", font=("Helvetica", 14)).pack(pady=10)

    # Daftar menu
    menus = [
        ("1. Hitung Mean dari Data", menu_hitung_mean),
        ("2. Satu Rata-Rata (σ² diketahui)", menu_satu_rata_diketahui),
        ("3. Satu Rata-Rata (σ² tidak diketahui)", menu_satu_rata_tidak_diketahui),
        ("4. Satu Rata-Rata (σ² tidak diketahui dan n < 30)", menu_satu_rata_t_kecil),
        ("5. Dua Rata-Rata (kedua σ² diketahui)", menu_dua_rata_diketahui),
        ("6. Dua Rata-Rata (kedua σ² tidak diketahui, tetapi sama n1+n2 < 30)", menu_dua_rata_sama),
        ("7. Dua Rata-Rata (kedua σ² tidak diketahui, dan berbeda n1+n2 < 30)", menu_dua_rata_berbeda),
        ("8. Dua Rata-Rata Saling Tidak Bebas (n kecil (<=30))", menu_dua_rata_tidak_bebas_kecil),
        ("9. Dua Rata-Rata Saling Tidak Bebas (n besar (>30))", menu_dua_rata_tidak_bebas_besar),
        ("10. Dua Proporsi", menu_dua_proporsi),
    ]

    for title, command in menus:
        tk.Button(frame, text=title, command=lambda c=command: c(frame), font=("Helvetica", 12)).pack(pady=5)

    # Tambahkan tombol keluar yang mengarahkan ke menu utama
    tk.Button(frame, text="Keluar", command=frame.destroy, font=("Helvetica", 12)).pack(pady=10)

# Menu untuk menghitung rata-rata dari data
def menu_hitung_mean(frame):
    kosongkan_frame(frame)
    tk.Label(frame, text="Masukkan Data (pisahkan dengan koma):", font=("Helvetica", 12)).pack(pady=10)
    entry_data = tk.Entry(frame, width=50)
    entry_data.pack()
    def hitung():
        try:
            data = list(map(float, entry_data.get().split(",")))
            hasil = hitung_mean(data)
            tampilkan_hasil(hasil)
        except Exception as e:
            messagebox.showerror("Error", f"Input salah: {e}")
    tk.Button(frame, text="Hitung", command=hitung, font=("Helvetica", 12)).pack(pady=10)
    # Tombol kembali selalu ditampilkan
    tk.Button(frame, text="Kembali ke Menu Utama", command=lambda: tampilkan_menu(frame), font=("Helvetica", 12)).pack(pady=5)

    

def menu_satu_rata_diketahui(frame):
    buat_menu_fungsi(frame, "Satu Rata-rata dengan Simpangan Baku Diketahui",
                     ["Mean", "Simpangan Baku", "n", "Tingkat Kepercayaan (%)"], hitung_interval_satu_rata_diketahui)

def menu_satu_rata_tidak_diketahui(frame):
    buat_menu_fungsi(frame, "Satu Rata-rata dengan Simpangan Baku Tidak Diketahui",
                     ["Mean", "Simpangan Baku Sampel", "n", "Tingkat Kepercayaan (%)"], hitung_interval_satu_rata_tidak_diketahui)

def menu_satu_rata_t_kecil(frame):
    buat_menu_fungsi(frame, "Satu Rata-rata (n kecil)",
                     ["Mean", "Simpangan Baku Sampel", "n", "Tingkat Kepercayaan (%)"], hitung_interval_satu_rata_t_dengan_sampel_kecil)

def menu_dua_rata_diketahui(frame):
    buat_menu_fungsi(frame, "Dua Rata-rata dengan Simpangan Baku Diketahui",
                     ["Mean1", "Mean2", "Simpangan Baku1", "Simpangan Baku2", "n1", "n2", "Tingkat Kepercayaan (%)"], hitung_interval_dua_rata_diketahui)

def menu_dua_rata_sama(frame):
    buat_menu_fungsi(frame, "Dua Rata-rata dengan Simpangan Baku Tidak Diketahui (sama)",
                     ["Mean1", "Mean2", "Simpangan Baku1", "Simpangan Baku2", "n1", "n2", "Tingkat Kepercayaan (%)"], hitung_interval_dua_rata_tidak_diketahui_sama)

def menu_dua_rata_berbeda(frame):
    buat_menu_fungsi(frame, "Dua Rata-rata dengan Simpangan Baku Tidak Diketahui (berbeda)",
                     ["Mean1", "Mean2", "Simpangan Baku1", "Simpangan Baku2", "n1", "n2", "Tingkat Kepercayaan (%)"], hitung_interval_dua_rata_tidak_diketahui_berbeda)

def menu_dua_rata_tidak_bebas_kecil(frame):
    buat_menu_fungsi(frame, "Dua Rata-rata Saling Tidak Bebas (n kecil)",
                     ["Mean Selisih", "Simpangan Baku Selisih", "n", "Tingkat Kepercayaan (%)"], hitung_interval_dua_rata_saling_tidak_bebas_kecil)

def menu_dua_rata_tidak_bebas_besar(frame):
    buat_menu_fungsi(frame, "Dua Rata-rata Saling Tidak Bebas (n besar)",
                     ["Mean Selisih", "Simpangan Baku Selisih", "n", "Tingkat Kepercayaan (%)"], hitung_interval_dua_rata_saling_tidak_bebas_besar)

def menu_dua_proporsi(frame):
    buat_menu_fungsi(frame, "Dua Proporsi",
                     ["Proporsi1", "Proporsi2", "n1", "n2", "Tingkat Kepercayaan (%)"], hitung_interval_dua_proporsi)



def buat_menu_fungsi(frame, judul, fields, fungsi):
    kosongkan_frame(frame)
    tk.Label(frame, text=judul, font=("Helvetica", 12)).pack(pady=10)
    
    entries = []
    for field in fields:
        tk.Label(frame, text=f"{field}:", font=("Helvetica", 12)).pack(pady=5)
        entry = tk.Entry(frame, width=30)
        entry.pack(pady=2)
        entries.append(entry)
        
    def hitung():
        try:
            values = [float(entry.get()) for entry in entries]
            hasil = fungsi(*values)
            tampilkan_hasil(hasil)
        except Exception as e:
            messagebox.showerror("Error", f"Input salah: {e}")
    
    tk.Button(frame, text="Hitung", command=hitung, font=("Helvetica", 12)).pack(pady=10)
    
    # Tombol kembali selalu ditampilkan
    tk.Button(frame, text="Kembali ke Menu Utama", command=lambda: tampilkan_menu(frame), font=("Helvetica", 12)).pack(pady=5)


# Fungsi untuk menampilkan aplikasi di frame root
def tampilkan_aplikasi(root, kembali_ke_menu_utama):
    """
    Menampilkan antarmuka dari aplikasi pendugaan titik dan interval rataan B.
    """
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    def kembali():
        frame.destroy()
        kembali_ke_menu_utama()
    tampilkan_menu(frame)
    tk.Button(frame, text="Kembali ke Menu Utama", command=kembali, font=("Helvetica", 12)).pack(pady=10)
    return frame
