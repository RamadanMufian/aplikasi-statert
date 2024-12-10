import tkinter as tk
from tkinter import ttk, messagebox
from scipy.stats import norm, t
import math

# Fungsi untuk menghitung rata-rata
def hitung_rata_rata(data):
    return sum(data) / len(data)

# Fungsi untuk menghitung simpangan baku
def hitung_simpangan_baku(data, rata_rata):
    jumlah = sum((nilai - rata_rata) ** 2 for nilai in data)
    return math.sqrt(jumlah / (len(data) - 1))

# Fungsi untuk menghitung statistik uji Z dua populasi
def hitung_statistik_z(rata1, rata2, sigma1, sigma2, n1, n2):
    return (rata1 - rata2) / math.sqrt((sigma1 ** 2 / n1) + (sigma2 ** 2 / n2))

# Fungsi untuk menghitung statistik uji t untuk varians sama
def hitung_statistik_t_sama(rata1, rata2, s1, s2, n1, n2):
    sp2 = ((n1 - 1) * s1 ** 2 + (n2 - 1) * s2 ** 2) / (n1 + n2 - 2)
    return (rata1 - rata2) / math.sqrt(sp2 * (1 / n1 + 1 / n2))

# Fungsi untuk menghitung statistik uji t untuk varians berbeda
def hitung_statistik_t_beda(rata1, rata2, s1, s2, n1, n2):
    pembilang = rata1 - rata2
    penyebut = math.sqrt((s1 ** 2 / n1) + (s2 ** 2 / n2))
    t_stat = pembilang / penyebut

    # Menghitung derajat bebas menggunakan rumus Welch-Satterthwaite
    df = ((s1 ** 2 / n1 + s2 ** 2 / n2) ** 2) / (
        ((s1 ** 2 / n1) ** 2 / (n1 - 1)) + ((s2 ** 2 / n2) ** 2 / (n2 - 1))
    )
    return t_stat, df

# Fungsi untuk menghitung statistik uji t untuk populasi dependen
def hitung_statistik_t_dependen(sebelum, sesudah):
    selisih = [sesudah[i] - sebelum[i] for i in range(len(sebelum))]
    rata_rata_d = hitung_rata_rata(selisih)
    simpangan_baku_d = hitung_simpangan_baku(selisih, rata_rata_d)
    return rata_rata_d / (simpangan_baku_d / math.sqrt(len(selisih)))

# Fungsi utama untuk menampilkan aplikasi dalam frame
# Fungsi utama untuk menampilkan aplikasi dalam frame
# Fungsi utama untuk menampilkan aplikasi dalam frame
def tampilkan_aplikasi(parent, kembali_ke_menu):
    frame = tk.Frame(parent, bg="#F8F9FA")
    frame.pack(fill="both", expand=True)
    
    # Judul Aplikasi
    tk.Label(
        frame, text="Pengujian Hipotesis Rataan 2 Populasi",
        font=("Arial", 18, "bold"), bg="#4682B4", fg="white", pady=10
    ).pack(fill="x")

    # Frame untuk input
    input_frame = tk.Frame(frame, bg="#F8F9FA")
    input_frame.place(relx=0.5, rely=0.3, anchor="center")  # Menempatkan input di tengah

    label_pilihan = tk.Label(input_frame, text="Pilih Jenis Uji:", bg="#F8F9FA")
    label_pilihan.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    pilihan_combobox = ttk.Combobox(
        input_frame, values=[
            "Uji Z (Ragam Populasi Diketahui)",
            "Uji T (Ragam Sama)",
            "Uji T (Ragam Berbeda)",
            "Uji T Dependen (Paired T-Test)"
        ], width=40
    )
    pilihan_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    # Tempat input data dinamis
    input_fields = {}

    def update_input_fields(event=None):
        for widget in input_frame.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.grid_forget()

        pilihan = pilihan_combobox.get()
        row = 1

        for label, var in {
            "Alpha (α)": "alpha",
            "Rata-rata Sampel 1 (X̄1)": "rata1",
            "Rata-rata Sampel 2 (X̄2)": "rata2",
            "Simpangan Baku Sampel 1 (σ1/S1)": "sigma1",
            "Simpangan Baku Sampel 2 (σ2/S2)": "sigma2",
            "Ukuran Sampel 1 (n1)": "n1",
            "Ukuran Sampel 2 (n2)": "n2",
            "Data Sebelum (Uji T Dependen)": "sebelum",
            "Data Sesudah (Uji T Dependen)": "sesudah",
        }.items():
            if pilihan == "Uji T Dependen (Paired T-Test)" and var not in {"sebelum", "sesudah", "alpha"}:
                continue
            if pilihan != "Uji T Dependen (Paired T-Test)" and var in {"sebelum", "sesudah"}:
                continue

            label_widget = tk.Label(input_frame, text=label, bg="#F8F9FA")
            entry_widget = tk.Entry(input_frame, width=30)
            label_widget.grid(row=row, column=0, padx=10, pady=5, sticky="w")
            entry_widget.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
            input_fields[var] = entry_widget
            row += 1

    pilihan_combobox.bind("<<ComboboxSelected>>", update_input_fields)

    # Frame untuk output hasil
    output_frame = tk.Frame(frame, bg="#F8F9FA")
    output_frame.place(relx=0.5, rely=0.7, anchor="center")  # Menempatkan output di bawah input

    result_text = tk.StringVar()
    result_label = tk.Label(output_frame, textvariable=result_text, bg="#F8F9FA", font=("Arial", 12), anchor="w")
    result_label.pack(pady=10, padx=10, fill="both")

    # Fungsi untuk menghitung hasil uji
    def hitung():
        try:
            pilihan = pilihan_combobox.get()
            alpha = float(input_fields["alpha"].get())
            hasil = ""

            if pilihan == "Uji Z (Ragam Populasi Diketahui)":
                rata1 = float(input_fields["rata1"].get())
                rata2 = float(input_fields["rata2"].get())
                sigma1 = float(input_fields["sigma1"].get())
                sigma2 = float(input_fields["sigma2"].get())
                n1 = int(input_fields["n1"].get())
                n2 = int(input_fields["n2"].get())
                z_stat = hitung_statistik_z(rata1, rata2, sigma1, sigma2, n1, n2)
                z_kritis = norm.ppf(1 - alpha / 2)
                hasil = f"Statistik Uji Z: {z_stat:.4f}\nZ-Kritis: ±{z_kritis:.4f}"
                hasil += "\nTolak H0: Ada perbedaan signifikan." if abs(z_stat) > z_kritis else "\nTerima H0: Tidak ada perbedaan signifikan."

            elif pilihan == "Uji T (Ragam Sama)":
                rata1 = float(input_fields["rata1"].get())
                rata2 = float(input_fields["rata2"].get())
                s1 = float(input_fields["sigma1"].get())
                s2 = float(input_fields["sigma2"].get())
                n1 = int(input_fields["n1"].get())
                n2 = int(input_fields["n2"].get())
                t_stat = hitung_statistik_t_sama(rata1, rata2, s1, s2, n1, n2)
                t_kritis = t.ppf(1 - alpha / 2, n1 + n2 - 2)
                hasil = f"Statistik Uji T: {t_stat:.4f}\nT-Kritis: ±{t_kritis:.4f}"
                hasil += "\nTolak H0: Ada perbedaan signifikan." if abs(t_stat) > t_kritis else "\nTerima H0: Tidak ada perbedaan signifikan."

            elif pilihan == "Uji T (Ragam Berbeda)":
                rata1 = float(input_fields["rata1"].get())
                rata2 = float(input_fields["rata2"].get())
                s1 = float(input_fields["sigma1"].get())
                s2 = float(input_fields["sigma2"].get())
                n1 = int(input_fields["n1"].get())
                n2 = int(input_fields["n2"].get())
                t_stat, df = hitung_statistik_t_beda(rata1, rata2, s1, s2, n1, n2)
                t_kritis = t.ppf(1 - alpha / 2, df)
                hasil = f"Statistik Uji T: {t_stat:.4f}\nT-Kritis: ±{t_kritis:.4f}\nDf: {df:.2f}"
                hasil += "\nTolak H0: Ada perbedaan signifikan." if abs(t_stat) > t_kritis else "\nTerima H0: Tidak ada perbedaan signifikan."

            elif pilihan == "Uji T Dependen (Paired T-Test)":
                sebelum = list(map(float, input_fields["sebelum"].get().split(',')))
                sesudah = list(map(float, input_fields["sesudah"].get().split(',')))
                t_stat = hitung_statistik_t_dependen(sebelum, sesudah)
                t_kritis = t.ppf(1 - alpha / 2, len(sebelum) - 1)
                hasil = f"Statistik Uji T Dependen: {t_stat:.4f}\nT-Kritis: ±{t_kritis:.4f}"
                hasil += "\nTolak H0: Ada perbedaan signifikan." if abs(t_stat) > t_kritis else "\nTerima H0: Tidak ada perbedaan signifikan."

            result_text.set(hasil)
        except Exception as e:
            messagebox.showerror("Error", f"Kesalahan: {e}")

    # Tombol hitung dan kembali
    button_frame = tk.Frame(frame, bg="#F8F9FA")
    button_frame.pack(pady=10)

    def kembali():
        frame.pack_forget()
        kembali_ke_menu()

    tk.Button(button_frame, text="Hitung", command=hitung, bg="#28A745", fg="white").pack(side="left", padx=5)
    tk.Button(button_frame, text="Kembali", command=kembali, bg="#DC3545", fg="white").pack(side="left", padx=5)

    return frame
