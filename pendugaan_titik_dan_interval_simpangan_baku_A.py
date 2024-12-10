import math
import tkinter as tk
from tkinter import messagebox

# Menghitung variansi sampel
def variance_sample(data):
    n = len(data)
    if n <= 1:
        return 0.0

    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    return variance

# Menghitung variansi populasi
def variance_population(data):
    n = len(data)
    if n == 0:
        return 0.0

    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    return variance

# Menentukan apakah dataset termasuk ragam
def is_variance_or_not(variance):
    # Variansi valid jika tidak negatif
    return variance >= 0

class VarianceCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Variansi Sampel/Populasi")
        self.master.geometry("500x300")
        self.master.configure(bg="#D6EAF8")  # Latar belakang biru muda

        self.is_population = tk.IntVar()
        self.n = tk.IntVar()

        self.options_frame = tk.Frame(self.master, bg="#D6EAF8")
        self.options_frame.pack(pady=10)
        tk.Radiobutton(
            self.options_frame, 
            text="Populasi", 
            variable=self.is_population, 
            value=1, 
            bg="#D6EAF8", 
            fg="#154360", 
            font=("Helvetica", 12)
        ).pack(anchor=tk.W)
        tk.Radiobutton(
            self.options_frame, 
            text="Sampel", 
            variable=self.is_population, 
            value=2, 
            bg="#D6EAF8", 
            fg="#154360", 
            font=("Helvetica", 12)
        ).pack(anchor=tk.W)

        self.n_label = tk.Label(self.master, text="Masukkan jumlah sampel:", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12))
        self.n_label.pack()
        self.n_entry = tk.Entry(self.master, textvariable=self.n, font=("Helvetica", 12))
        self.n_entry.pack(pady=5)

        self.data_label = tk.Label(self.master, text="Masukkan angka-angka (pisahkan dengan spasi):", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12))
        self.data_label.pack()
        self.data_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.data_entry.pack(pady=5)

        self.calculate_button = tk.Button(
            self.master, 
            text="Hitung", 
            command=self.calculate, 
            bg="#5DADE2", 
            fg="white", 
            font=("Helvetica", 12),
            activebackground="#3498DB", 
            activeforeground="white"
        )
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12))
        self.result_label.pack()

    def calculate(self):
        try:
            n = self.n.get()
            data = [float(x) for x in self.data_entry.get().split()]
            if len(data) != n:
                raise ValueError
        except ValueError:
            self.result_label.config(text="[ERROR] Input tidak valid. Harap masukkan angka yang dipisahkan dengan spasi.", fg="red")
            return

        if self.is_population.get() == 1:
            variance = variance_population(data)
        else:
            variance = variance_sample(data)

        self.result_label.config(
            text=f"Variansi: {variance:.4f}\nStandar Deviasi: {math.sqrt(variance):.4f}",
            fg="#154360"
        )
        if is_variance_or_not(variance):
            self.result_label.config(
                text=self.result_label.cget("text") + "\nDataset ini termasuk ragam (variansi).",
                fg="#154360"
            )
        else:
            self.result_label.config(
                text=self.result_label.cget("text") + "\nDataset ini tidak termasuk ragam (variansi).",
                fg="#154360"
            )

# Fungsi untuk menampilkan aplikasi dalam sebuah frame
def tampilkan_aplikasi(parent, on_back=None):
    frame = tk.Frame(parent, bg="#D6EAF8")  # Latar belakang biru muda

    # Label dan input pilihan
    tk.Label(frame, text="Pilih Jenis Data:", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=5, padx=5)
    is_population = tk.IntVar(value=1)
    tk.Radiobutton(frame, text="Populasi", variable=is_population, value=1, bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=0, column=1, sticky="w")
    tk.Radiobutton(frame, text="Sampel", variable=is_population, value=2, bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=1, column=1, sticky="w")

    # Input jumlah data
    tk.Label(frame, text="Jumlah Data:", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", pady=5, padx=5)
    entry_n = tk.Entry(frame, font=("Helvetica", 12))
    entry_n.grid(row=2, column=1, pady=5, padx=5)

    # Input data
    tk.Label(frame, text="Masukkan Data (pisahkan dengan spasi):", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", pady=5, padx=5)
    entry_data = tk.Entry(frame, font=("Helvetica", 12))
    entry_data.grid(row=3, column=1, pady=5, padx=5)

    # Label hasil
    result_label = tk.Label(frame, text="", bg="#D6EAF8", fg="#154360", font=("Helvetica", 12))
    result_label.grid(row=5, column=0, columnspan=2, pady=5)

    # Fungsi untuk menghitung variansi
    def calculate():
        try:
            n = int(entry_n.get())
            data = [float(x) for x in entry_data.get().split()]
            if len(data) != n:
                raise ValueError
        except ValueError:
            result_label.config(text="[ERROR] Input tidak valid. Harap masukkan angka yang dipisahkan dengan spasi.", fg="red")
            return

        if is_population.get() == 1:
            variance = variance_population(data)
        else:
            variance = variance_sample(data)

        result = f"Variansi: {variance:.4f}\nStandar Deviasi: {math.sqrt(variance):.4f}"
        if is_variance_or_not(variance):
            result += "\nDataset ini termasuk ragam (variansi)."
        else:
            result += "\nDataset ini tidak termasuk ragam (variansi)."
        result_label.config(text=result, fg="#154360")

    # Tombol Hitung
    tk.Button(
        frame,
        text="Hitung",
        command=calculate,
        font=("Helvetica", 12),
        bg="#5DADE2",
        fg="white",
        activebackground="#3498DB",
        activeforeground="white"
    ).grid(row=4, column=0, columnspan=2, pady=10)

    # Tombol Kembali
    if on_back:
        def handle_back():
            frame.pack_forget()  # Sembunyikan frame
            on_back()  # Panggil fungsi untuk kembali ke menu utama

        tk.Button(
            frame,
            text="Kembali",
            command=handle_back,
            font=("Helvetica", 12),
            bg="#FF6B6B",
            fg="white",
            activebackground="#E74C3C",
            activeforeground="white"
        ).grid(row=6, column=0, columnspan=2, pady=10)

    return frame
