
import tkinter as tk
from tkinter import messagebox
import random
import statistics

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ==========================================
# ZADANIE 2 - PYTHON
# Autor: Martin Sabik
# ==========================================

class Aplikacia:

    def __init__(self, okno):
        self.okno = okno
        self.okno.title("Zadanie 2 - Python | Martin Sabik")
        self.okno.geometry("1100x780")
        self.okno.configure(bg="#edf2f7")

        self.hodnoty = []
        self.vypocitane = []

        # NADPIS
        hlavicka = tk.Frame(okno, bg="#183153", height=105)
        hlavicka.pack(fill="x")

        tk.Label(
            hlavicka,
            text="ZADANIE 2 – PYTHON",
            font=("Arial", 25, "bold"),
            bg="#183153",
            fg="white"
        ).pack(pady=(15, 3))

        tk.Label(
            hlavicka,
            text="Autor: Martin Sabik",
            font=("Arial", 13),
            bg="#183153",
            fg="#dce6f2"
        ).pack()

        # HLAVNÝ OBSAH
        obsah = tk.Frame(okno, bg="#edf2f7")
        obsah.pack(fill="both", expand=True, padx=20, pady=15)

        # TLAČIDLÁ
        ovladanie = tk.LabelFrame(
            obsah,
            text="Ovládanie aplikácie",
            font=("Arial", 12, "bold"),
            bg="#edf2f7",
            padx=12,
            pady=12
        )
        ovladanie.pack(fill="x", pady=5)

        tk.Button(
            ovladanie,
            text="Generovať 100 hodnôt",
            command=self.generovat,
            bg="#2878b5",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=12,
            pady=8
        ).grid(row=0, column=0, padx=8, pady=5)

        tk.Label(
            ovladanie,
            text="Zadaj vlastné číslo:",
            bg="#edf2f7",
            font=("Arial", 11)
        ).grid(row=0, column=1, padx=8)

        self.vstup = tk.Entry(
            ovladanie,
            font=("Arial", 12),
            width=15
        )
        self.vstup.grid(row=0, column=2, padx=8)

        tk.Button(
            ovladanie,
            text="Vypočítať",
            command=self.vypocitat,
            bg="#239b65",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8
        ).grid(row=0, column=3, padx=8)

        # VÝSLEDOK VLASTNÉHO VÝPOČTU
        self.vysledok = tk.Label(
            obsah,
            text="Výsledok vlastného výpočtu sa zobrazí tu.",
            font=("Arial", 12, "bold"),
            fg="#183153",
            bg="#edf2f7"
        )
        self.vysledok.pack(pady=8)

        # ŠTATISTIKY
        statistiky = tk.LabelFrame(
            obsah,
            text="Analýza vygenerovaných hodnôt",
            font=("Arial", 12, "bold"),
            bg="#edf2f7",
            padx=12,
            pady=8
        )
        statistiky.pack(fill="x", pady=5)

        self.info = tk.Label(
            statistiky,
            text="Najskôr klikni na tlačidlo Generovať 100 hodnôt.",
            font=("Arial", 11),
            bg="#edf2f7",
            justify="left",
            anchor="w"
        )
        self.info.pack(fill="x")

        # GRAF
        graf_frame = tk.LabelFrame(
            obsah,
            text="Grafické porovnanie hodnôt",
            font=("Arial", 12, "bold"),
            bg="#edf2f7"
        )
        graf_frame.pack(fill="both", expand=True, pady=8)

        self.fig, self.ax = plt.subplots(figsize=(9, 4))
        self.fig.tight_layout()

        self.canvas = FigureCanvasTkAgg(
            self.fig,
            master=graf_frame
        )
        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

        self.ax.set_title("Porovnanie pôvodných a vypočítaných hodnôt")
        self.ax.set_xlabel("Poradie hodnoty")
        self.ax.set_ylabel("Teplota / vypočítaná hodnota")
        self.ax.grid(True)
        self.canvas.draw()

        # SPODNÝ TEXT
        tk.Label(
            okno,
            text="Python | Generovanie údajov | Analýza | Matematický výpočet",
            font=("Arial", 9),
            bg="#edf2f7",
            fg="#555555"
        ).pack(pady=7)

    # 1. GENEROVANIE NÁHODNÝCH HODNÔT
    def generovat(self):

        self.hodnoty = [
            round(random.uniform(0, 40), 2)
            for i in range(100)
        ]

        # 2. VÝPOČET PODĽA VZORCA
        self.vypocitane = [
            round(1.2 * x + 5, 2)
            for x in self.hodnoty
        ]

        self.analyza()
        self.zobrazit_graf()

    # 3. ANALÝZA POĽA
    def analyza(self):

        priemer = statistics.mean(self.hodnoty)
        minimum = min(self.hodnoty)
        maximum = max(self.hodnoty)
        zoradene = sorted(self.hodnoty)

        text = (
            f"Počet vygenerovaných hodnôt: {len(self.hodnoty)}\n"
            f"Priemerná hodnota: {priemer:.2f}\n"
            f"Najmenšia hodnota: {minimum:.2f}\n"
            f"Najväčšia hodnota: {maximum:.2f}\n"
            f"Prvých 10 zoradených hodnôt: {zoradene[:10]}"
        )

        self.info.config(text=text)

    # 4. VÝPOČET PRE ĽUBOVOĽNÉ ČÍSLO
    def vypocitat(self):

        try:
            cislo = float(self.vstup.get().replace(",", "."))

            vysledok = 1.2 * cislo + 5

            self.vysledok.config(
                text=f"Výsledok: 1,2 × {cislo} + 5 = {vysledok:.2f}"
            )

        except ValueError:
            messagebox.showerror(
                "Chyba",
                "Zadaj platné číslo!"
            )

    # 5. ZOBRAZENIE GRAFU
    def zobrazit_graf(self):

        self.ax.clear()

        poradie = list(range(1, len(self.hodnoty) + 1))

        self.ax.plot(
            poradie,
            self.hodnoty,
            label="Pôvodné hodnoty",
            color="blue",
            linewidth=1.5
        )

        self.ax.plot(
            poradie,
            self.vypocitane,
            label="Vypočítané hodnoty",
            color="red",
            linewidth=1.5
        )

        self.ax.set_title("Porovnanie pôvodných a vypočítaných hodnôt")
        self.ax.set_xlabel("Poradie hodnoty")
        self.ax.set_ylabel("Hodnota")
        self.ax.legend()
        self.ax.grid(True, alpha=0.3)

        self.fig.tight_layout()
        self.canvas.draw()


# ==========================================
# SPUSTENIE APLIKÁCIE
# ==========================================

if __name__ == "__main__":
    okno = tk.Tk()
    aplikacia = Aplikacia(okno)
    okno.mainloop()
