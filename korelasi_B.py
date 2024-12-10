import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import math
from scipy.stats import t, norm

def tampilkan_aplikasi(root, kembali_ke_menu):
    X, Y = [], []

    def korelasiKoefisien(X, Y, n):
        sum_X = sum(X)
        sum_Y = sum(Y)
        sum_XY = sum(x * y for x, y in zip(X, Y))
        squareSum_X = sum(x**2 for x in X)
        squareSum_Y = sum(y**2 for y in Y)

        penyebut_X = math.sqrt(n * squareSum_X - sum_X**2)
        penyebut_Y = math.sqrt(n * squareSum_Y - sum_Y**2)

        if penyebut_X == 0 or penyebut_Y == 0:
            return float('nan')

        corr = (n * sum_XY - sum_X * sum_Y) / (penyebut_X * penyebut_Y)
        return corr

    def analisisKorelasi(X, Y, alpha=0.05):
        n = len(X)

        if n < 3:
            raise ValueError("Jumlah sampel harus minimal 3")

        r = korelasiKoefisien(X, Y, n)
        df = n - 2

        correlation_statistic = r * math.sqrt(n - 2) / math.sqrt(1 - r**2)

        if n > 30:
            z_critical_lower = norm.ppf(alpha / 2)
            z_critical_upper = norm.ppf(1 - alpha / 2)
            is_rejected = (correlation_statistic < z_critical_lower) or (correlation_statistic > z_critical_upper)
            test_type = "Z-test (n > 30)"
            critical_lower = z_critical_lower
            critical_upper = z_critical_upper
        else:
            t_critical_lower = -t.ppf(alpha / 2, df)
            t_critical_upper = t.ppf(alpha / 2, df)
            is_rejected = (correlation_statistic < t_critical_lower) or (correlation_statistic > t_critical_upper)
            test_type = "T-test (n ≤ 30)"
            critical_lower = t_critical_lower
            critical_upper = t_critical_upper

        return {
            'korelasiKoefisien': r,
            'test_statistic': correlation_statistic,
            'test_type': test_type,
            'critical_value_lower': critical_lower,
            'critical_value_upper': critical_upper,
            'sample_size': n,
            'degrees_of_freedom': df,
            'alpha': alpha,
            'hypothesis_rejected': is_rejected,
            'interpretation': (
                "Tolak H0: Terdapat bukti statistik adanya hubungan linear"
                if is_rejected else
                "Terima H0: Tidak cukup bukti untuk menyatakan adanya hubungan linear"
            )
        }

    def add_list_to_table():
        try:
            x_values = list(map(int, entry_list_X.get().split()))
            y_values = list(map(int, entry_list_Y.get().split()))

            if len(x_values) != len(y_values):
                raise ValueError("Jumlah elemen X dan Y harus sama.")

            for i in range(len(x_values)):
                X.append(x_values[i])
                Y.append(y_values[i])
                table.insert("", "end", values=(len(X), x_values[i], y_values[i], x_values[i] * y_values[i], x_values[i]**2, y_values[i]**2))

            entry_list_X.delete(0, tk.END)
            entry_list_Y.delete(0, tk.END)

        except ValueError as e:
            messagebox.showerror("Kesalahan", f"Input tidak valid: {e}")

    def calculate():
        try:
            if len(X) < 3:
                raise ValueError("Jumlah data harus minimal 3 untuk analisis korelasi.")

            result = analisisKorelasi(X, Y)

            result_text.set(
                f"Ukuran Sampel: {result['sample_size']}\n"
                f"Jenis Uji: {result['test_type']}\n"
                f"Koefisien Korelasi (r): {result['korelasiKoefisien']:.4f}\n"
                f"Statistik Uji: {result['test_statistic']:.4f}\n"
                f"Derajat Kebebasan: {result['degrees_of_freedom']}\n"
                f"Tingkat Signifikansi: {result['alpha']}\n"
                f"Nilai Kritis Bawah: {result['critical_value_lower']:.4f}\n"
                f"Nilai Kritis Atas: {result['critical_value_upper']:.4f}\n"
                f"Kesimpulan: {result['interpretation']}"
            )
        except ValueError as e:
            messagebox.showerror("Kesalahan", str(e))

    # Membuat frame utama dengan scrollbar
    main_frame = tk.Frame(root, bg="#f0f8ff")
    canvas = tk.Canvas(main_frame, bg="#f0f8ff")
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f0f8ff")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    main_frame.place(relx=0.5, rely=0.5, anchor="center", width=800, height=600)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Judul Aplikasi
    title = tk.Label(scrollable_frame, text="Analisis Korelasi Pearson", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="#000080")
    title.grid(row=0, column=0, columnspan=2, pady=20)

    # Input Nilai List
    tk.Label(scrollable_frame, text="Masukkan daftar nilai X (pisahkan dengan spasi):", font=("Arial", 14), bg="#f0f8ff", fg="#000080").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_list_X = tk.Entry(scrollable_frame, width=50, font=("Arial", 12), bg="#ffffff", fg="#000080")
    entry_list_X.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(scrollable_frame, text="Masukkan daftar nilai Y (pisahkan dengan spasi):", font=("Arial", 14), bg="#f0f8ff", fg="#000080").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry_list_Y = tk.Entry(scrollable_frame, width=50, font=("Arial", 12), bg="#ffffff", fg="#000080")
    entry_list_Y.grid(row=2, column=1, padx=10, pady=10)

    btn_add_list = tk.Button(scrollable_frame, text="Tambah ke Tabel", font=("Arial", 14), command=add_list_to_table, bg="#add8e6", fg="#000080")
    btn_add_list.grid(row=3, column=0, columnspan=2, pady=10)

    # Tabel
    columns = ("No", "X", "Y", "X*Y", "X^2", "Y^2")
    table = ttk.Treeview(scrollable_frame, columns=columns, show="headings", height=10)
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100)
    table.grid(row=4, column=0, columnspan=2, pady=10)

    # Tombol Hitung
    btn_calculate = tk.Button(scrollable_frame, text="Hitung Analisis", font=("Arial", 14), command=calculate, bg="#add8e6", fg="#000080")
    btn_calculate.grid(row=5, column=0, columnspan=2, pady=10)

    # Hasil
    result_text = tk.StringVar()
    result_label = tk.Label(scrollable_frame, textvariable=result_text, font=("Arial", 14), justify=tk.LEFT, wraplength=600, bg="#f0f8ff", fg="#000080")
    result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Tombol Kembali
    tk.Button(scrollable_frame, text="Kembali ke Menu Utama", font=("Arial", 14), bg="#ff6b6b", fg="white", command=lambda: (main_frame.destroy(), kembali_ke_menu())).grid(row=7, column=0, columnspan=2, pady=20)

    return main_frame
