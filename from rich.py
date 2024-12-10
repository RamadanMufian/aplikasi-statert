from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Inisialisasi console Rich
console = Console()

def main_menu():
    # Header
    header = Panel(
        "[bold yellow]Projek Statistik Terapan[/bold yellow]",
        border_style="bright_blue",
        expand=False,
    )
    
    # Daftar menu
    table = Table(title="Menu Utama", title_style="bold green", border_style="cyan")
    table.add_column("No.", justify="center", style="bright_magenta", width=5)
    table.add_column("Deskripsi", style="bold white")

    menu_items = [
        "Pendugaan Titik dan Interval Rataan",
        "Pendugaan Titik dan Interval Simpangan Baku",
        "Pengujian Hipotesis Rataan 1 Populasi",
        "Pengujian Hipotesis Ragam",
        "Pengujian Hipotesis Proporsi",
        "Pengujian Hipotesis Rataan 2 Populasi",
        "Regresi Linier",
        "Korelasi"
    ]

    # Tambahkan menu ke tabel
    for idx, item in enumerate(menu_items, 1):
        table.add_row(f"[bold blue]{idx}[/bold blue]", f"[cyan]{item}[/cyan]")

    # Tampilkan header dan tabel
    console.print(header)
    console.print(table)
    
    # Footer dan input pilihan
    console.print("[bold green]Pilih nomor menu untuk melanjutkan (atau ketik '0' untuk keluar):[/bold green]")
    try:
        choice = int(console.input("[bold yellow]>>> [/bold yellow]"))
        return choice
    except ValueError:
        console.print("[bold red]Input tidak valid. Masukkan nomor menu![/bold red]")
        return -1

# Program utama
while True:
    choice = main_menu()
    if choice == 0:
        console.print("[bold yellow]Terima kasih telah menggunakan Projek Statistik Terapan![/bold yellow]")
        break
    elif 1 <= choice <= 8:
        console.print(f"[bold green]Anda memilih menu nomor {choice}[/bold green]")
    else:
        console.print("[bold red]Pilihan tidak valid! Silakan coba lagi.[/bold red]")
