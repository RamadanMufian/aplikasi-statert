# pengujian_rataan_1_populasi.py

import tkinter as tk
from tkinter import ttk, messagebox

# Tabel distribusi z
z_table = {
    0.10: 1.282,
    0.05: 1.645,
    0.025: 1.960,
    0.01: 2.326,
    0.005: 2.576
}

# Tabel distribusi t
t_table = {
    2: {0.10: 1.886, 0.05: 2.920, 0.025: 4.303, 0.01: 6.965, 0.005: 9.925},
    3: {0.10: 1.638, 0.05: 2.353, 0.025: 3.182, 0.01: 4.541, 0.005: 6.208},
    4: {0.10: 1.533, 0.05: 2.132, 0.025: 2.776, 0.01: 3.747, 0.005: 4.604},
    5: {0.10: 1.476, 0.05: 2.015, 0.025: 2.571, 0.01: 3.365, 0.005: 4.032},
    6: {0.10: 1.440, 0.05: 1.943, 0.025: 2.447, 0.01: 3.143, 0.005: 3.707},
    7: {0.10: 1.415, 0.05: 1.895, 0.025: 2.365, 0.01: 2.998, 0.005: 3.499},
    8: {0.10: 1.397, 0.05: 1.860, 0.025: 2.306, 0.01: 2.896, 0.005: 3.355},
    9: {0.10: 1.383, 0.05: 1.833, 0.025: 2.262, 0.01: 2.821, 0.005: 3.249},
    10: {0.10: 1.372, 0.05: 1.812, 0.025: 2.228, 0.01: 2.764, 0.005: 3.169},
    11: {0.10: 1.363, 0.05: 1.796, 0.025: 2.201, 0.01: 2.819, 0.005: 3.106},
    12: {0.10: 1.356, 0.05: 1.782, 0.025: 2.179, 0.01: 2.681, 0.005: 3.055},
    13: {0.10: 1.350, 0.05: 1.771, 0.025: 2.160, 0.01: 2.650, 0.005: 3.012},
    14: {0.10: 1.345, 0.05: 1.761, 0.025: 2.145, 0.01: 2.624, 0.005: 2.977},
    15: {0.10: 1.341, 0.05: 1.753, 0.025: 2.131, 0.01: 2.602, 0.005: 2.947},
    16: {0.10: 1.337, 0.05: 1.746, 0.025: 2.120, 0.01: 2.583, 0.005: 2.921},
    17: {0.10: 1.333, 0.05: 1.740, 0.025: 2.110, 0.01: 2.567, 0.005: 2.898},
    18: {0.10: 1.330, 0.05: 1.734, 0.025: 2.101, 0.01: 2.552, 0.005: 2.878},
    19: {0.10: 1.328, 0.05: 1.729, 0.025: 2.093, 0.01: 2.539, 0.005: 2.861},
    20: {0.10: 1.325, 0.05: 1.725, 0.025: 2.086, 0.01: 2.528, 0.005: 2.845},
    21: {0.10: 1.323, 0.05: 1.721, 0.025: 2.080, 0.01: 2.518, 0.005: 2.831},
    22: {0.10: 1.321, 0.05: 1.717, 0.025: 2.074, 0.01: 2.508, 0.005: 2.819},
    23: {0.10: 1.319, 0.05: 1.714, 0.025: 2.069, 0.01: 2.500, 0.005: 2.807},
    24: {0.10: 1.318, 0.05: 1.711, 0.025: 2.064, 0.01: 2.492, 0.005: 2.797},
    25: {0.10: 1.316, 0.05: 1.708, 0.025: 2.060, 0.01: 2.485, 0.005: 2.787},
    26: {0.10: 1.315, 0.05: 1.706, 0.025: 2.056, 0.01: 2.479, 0.005: 2.778},
    27: {0.10: 1.314, 0.05: 1.703, 0.025: 2.052, 0.01: 2.473, 0.005: 2.769},
    28: {0.10: 1.313, 0.05: 1.701, 0.025: 2.048, 0.01: 2.467, 0.005: 2.761},
    29: {0.10: 1.312, 0.05: 1.699, 0.025: 2.045, 0.01: 2.462, 0.005: 2.753},
    30: {0.10: 1.310, 0.05: 1.697, 0.025: 2.042, 0.01: 2.450, 0.005: 2.745}
}

def tampilkan_aplikasi(root, return_to_menu):
    """
    Membuat dan mengembalikan frame untuk pengujian rataan 1 populasi.
    """
    frame = tk.Frame(root, bg="#f0f4f8", padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Memastikan frame berada di tengah layar

    # Header
    header_label = tk.Label(frame, text="Pengujian Rataan 1 Populasi", font=("Arial", 18, "bold"), bg="#4682B4", fg="white")
    header_label.grid(row=0, column=0, columnspan=2, pady=10, ipadx=5, ipady=5)

    # Input rata-rata populasi
    tk.Label(frame, text="Masukkan rata-rata populasi (mu):", font=("Arial", 12), bg="#f0f4f8").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entry_mu = tk.Entry(frame, font=("Arial", 12), bd=2)
    entry_mu.grid(row=1, column=1, pady=5, padx=10)

    # Pilihan jenis hipotesis
    tk.Label(frame, text="Pilih jenis hipotesis:", font=("Arial", 12), bg="#f0f4f8").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    radio_hypothesis = tk.StringVar(value="!=")
    tk.Radiobutton(frame, text="H1: mu < mu0", variable=radio_hypothesis, value="<", font=("Arial", 12), bg="#f0f4f8").grid(row=3, column=0, sticky="w", padx=10)
    tk.Radiobutton(frame, text="H1: mu > mu0", variable=radio_hypothesis, value=">", font=("Arial", 12), bg="#f0f4f8").grid(row=4, column=0, sticky="w", padx=10)
    tk.Radiobutton(frame, text="H1: mu != mu0", variable=radio_hypothesis, value="!=", font=("Arial", 12), bg="#f0f4f8").grid(row=5, column=0, sticky="w", padx=10)

    # Pilihan simpangan baku
    tk.Label(frame, text="Apakah simpangan baku populasi tersedia?", font=("Arial", 12), bg="#f0f4f8").grid(row=6, column=0, sticky="w", padx=10, pady=5)
    radio_std = tk.StringVar(value="pop")
    tk.Radiobutton(frame, text="Ya", variable=radio_std, value="pop", font=("Arial", 12), bg="#f0f4f8").grid(row=7, column=0, sticky="w", padx=10)
    tk.Radiobutton(frame, text="Tidak", variable=radio_std, value="sample", font=("Arial", 12), bg="#f0f4f8").grid(row=7, column=1, sticky="w", padx=10)

    # Input simpangan baku
    tk.Label(frame, text="Simpangan baku populasi:", font=("Arial", 12), bg="#f0f4f8").grid(row=8, column=0, sticky="w", padx=10, pady=5)
    entry_std_pop = tk.Entry(frame, font=("Arial", 12), bd=2)
    entry_std_pop.grid(row=8, column=1, pady=5, padx=10)

    tk.Label(frame, text="Simpangan baku sampel:", font=("Arial", 12), bg="#f0f4f8").grid(row=9, column=0, sticky="w", padx=10, pady=5)
    entry_std_sample = tk.Entry(frame, font=("Arial", 12), bd=2)
    entry_std_sample.grid(row=9, column=1, pady=5, padx=10)

    # Input tingkat signifikansi
    tk.Label(frame, text="Tingkat signifikansi (alpha):", font=("Arial", 12), bg="#f0f4f8").grid(row=10, column=0, sticky="w", padx=10, pady=5)
    entry_alpha = tk.Entry(frame, font=("Arial", 12), bd=2)
    entry_alpha.grid(row=10, column=1, pady=5, padx=10)

    # Input jumlah data
    tk.Label(frame, text="Jumlah data (n):", font=("Arial", 12), bg="#f0f4f8").grid(row=11, column=0, sticky="w", padx=10, pady=5)
    entry_n = tk.Entry(frame, font=("Arial", 12), bd=2)
    entry_n.grid(row=11, column=1, pady=5, padx=10)

    # Pilihan input data atau rata-rata
    tk.Label(frame, text="Apakah Anda ingin memasukkan data sampel atau rata-rata?", font=("Arial", 12), bg="#f0f4f8").grid(row=12, column=0, sticky="w", padx=10, pady=5)
    radio_data = tk.StringVar(value="data")
    tk.Radiobutton(frame, text="Data Sampel", variable=radio_data, value="data", font=("Arial", 12), bg="#f0f4f8").grid(row=13, column=0, sticky="w", padx=10)
    tk.Radiobutton(frame, text="Langsung Rata-rata", variable=radio_data, value="mean", font=("Arial", 12), bg="#f0f4f8").grid(row=13, column=1, sticky="w", padx=10)

    # Input data sampel atau rata-rata
    tk.Label(frame, text="Masukkan data sampel (pisahkan dengan koma):", font=("Arial", 12), bg="#f0f4f8").grid(row=14, column=0, sticky="w", padx=10, pady=5)
    entry_data = tk.Entry(frame, font=("Arial", 12), bd=2)
    entry_data.grid(row=14, column=1, pady=5, padx=10)

    tk.Label(frame, text="Rata-rata sampel (x̄):", font=("Arial", 12), bg="#f0f4f8").grid(row=15, column=0, sticky="w", padx=10, pady=5)
    entry_x_bar = tk.Entry(frame, font=("Arial", 12), bd=2)
    entry_x_bar.grid(row=15, column=1, pady=5, padx=10)

    # Tombol untuk hitung
    tk.Button(frame, text="Hitung", command=lambda: calculate(entry_mu, entry_alpha, entry_n, entry_data, entry_x_bar, entry_std_pop, entry_std_sample, radio_hypothesis, radio_data, radio_std),
              font=("Arial", 12, "bold"), bg="#4682B4", fg="white", relief="raised").grid(row=16, column=0, columnspan=2, pady=15)

    # Tombol kembali ke menu utama
    tk.Button(frame, text="Kembali ke Menu Utama", command=lambda: [frame.destroy(), return_to_menu()],
              font=("Arial", 12, "bold"), bg="#ff6b6b", fg="white", relief="raised").grid(row=17, column=0, columnspan=2, pady=10)

    # Fungsi untuk mengatur tampilan input data dan simpangan baku
    def toggle_inputs():
        if radio_data.get() == "data":
            entry_data.config(state="normal")
            entry_x_bar.config(state="disabled")
        else:
            entry_data.config(state="disabled")
            entry_x_bar.config(state="normal")

    def toggle_std_input():
        if radio_std.get() == "pop":
            entry_std_pop.config(state="normal")
            entry_std_sample.config(state="disabled")
        else:
            entry_std_pop.config(state="disabled")
            entry_std_sample.config(state="normal")

    radio_data.trace("w", lambda *args: toggle_inputs())
    radio_std.trace("w", lambda *args: toggle_std_input())

    toggle_inputs()
    toggle_std_input()

    return frame

def calculate(entry_mu, entry_alpha, entry_n, entry_data, entry_x_bar, entry_std_pop, entry_std_sample, radio_hypothesis, radio_data, radio_std):
    """
    Fungsi untuk melakukan perhitungan uji hipotesis.
    """
    try:
        mu = float(entry_mu.get())
        alpha = float(entry_alpha.get())
        n = int(entry_n.get())
        hypothesis = radio_hypothesis.get()

        if radio_data.get() == "data":
            data = list(map(float, entry_data.get().split(',')))
            x_bar = sum(data) / len(data)
        else:
            x_bar = float(entry_x_bar.get())

        if radio_std.get() == "pop":
            std = float(entry_std_pop.get())
        else:
            std = float(entry_std_sample.get())

        stat = (x_bar - mu) / (std / (n**0.5))

        if n <= 30 and radio_std.get() == "sample":
            df = n - 1
            critical = t_table.get(df, {}).get(alpha)
            if critical is None:
                critical = t_table.get(30, {}).get(alpha)
            if hypothesis == "<":
                critical = -critical
            elif hypothesis == "!=":
                critical_positive = critical
                critical_negative = -critical
                critical = (critical_negative, critical_positive)
        else:
            if hypothesis == "!=":
                critical_positive = z_table[alpha / 2]
                critical_negative = -critical_positive
                critical = (critical_negative, critical_positive)
            elif hypothesis == "<":
                critical = -z_table[alpha]
            elif hypothesis == ">":
                critical = z_table[alpha]

        if hypothesis == "!=":
            decision = "Tolak H0" if abs(stat) > abs(critical[1]) else "Terima H0"
        elif hypothesis == "<":
            decision = "Tolak H0" if stat < critical else "Terima H0"
        elif hypothesis == ">":
            decision = "Tolak H0" if stat > critical else "Terima H0"

        if hypothesis == "!=":
            messagebox.showinfo(
                "Hasil",
                f"Statistik: {stat:.4f}\nNilai kritis: ±{critical[1]:.4f}\nKeputusan: {decision}"
            )
        else:
            messagebox.showinfo(
                "Hasil",
                f"Statistik: {stat:.4f}\nNilai kritis: {critical:.4f}\nKeputusan: {decision}"
            )

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
