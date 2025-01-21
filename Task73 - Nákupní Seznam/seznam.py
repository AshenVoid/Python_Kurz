import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import pickle


class SeznamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seznam")
        self.seznam = []

    #GUI
        #INPUT
        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row = 0, column = 0, padx = 10, pady = 10)

        #ADD
        self.add_button = tk.Button(root, text="Přidat položku", command=self.pridat_polozku)
        self.add_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        #LIST
        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        #EDIT
        self.edit_button = tk.Button(root, text="Upravit položku", command= self.upravit_polozku)
        self.edit_button.grid(row = 2, column = 0, pady = 10)

        #DEL
        self.delete_button = tk.Button(root, text="Smazat položku", command=self.smazat_polozku)
        self.delete_button.grid(row = 2, column = 1, pady = 10)

        #SAVE_CSV
        self.save_button = tk.Button(root, text="Uložit do CSV", command=self.ulozit_csv)
        self.save_button.grid(row = 3, column = 0, pady = 10)

        #LOAD_CSV
        self.load_button = tk.Button(root, text="Načíst z CSV", command=self.nacist_csv)
        self.load_button.grid(row = 3, column = 1, pady = 10)

        #SAVE_PICKLE
        self.save_pickle_button = tk.Button(root, text="Uložit do Pickle", command=self.ulozit_pickle)
        self.save_pickle_button.grid(row=4, column=0, pady=10)

        #LOAD_PICKLE
        self.load_pickle_button = tk.Button(root, text="Načíst z Pickle", command=self.nacist_pickle)
        self.load_pickle_button.grid(row=4, column=1, pady=10)

        #SAVE_JSON

        #LOAD_JSON


    def pridat_polozku(self):
        polozka = self.entry.get()
        if polozka:
            self.seznam.append(polozka)
            self.listbox.insert(tk.END, polozka)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Chyba", "Nelze přidat prázdnou položku!")

    def upravit_polozku(self):
        try:
            index = self.listbox.curselection()[0]
            nova_hodnota = self.entry.get()
            if nova_hodnota:
                self.seznam[index] = nova_hodnota
                self.listbox.delete(index)
                self.listbox.insert(index, nova_hodnota)
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Chyba", "Nelze nastavit prázdnou hodnotu.")
        except IndexError:
            messagebox.showwarning("Chyba", "Vyberte položku k úpravě.")

    def smazat_polozku(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            del self.seznam[index]
        except IndexError:
            messagebox.showwarning("Chyba", "Vyberte položku ke smazání.")

    def ulozit_csv(self):
        soubor = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if soubor:
            with open(soubor, "w", newline="") as f:
                writer = csv.writer(f)
                for polozka in self.seznam:
                    writer.writerow([polozka])
            messagebox.showinfo("Uloženo", "Seznam byl uložen do CSV souboru.")

    def nacist_csv(self):
        soubor = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if soubor:
            with open(soubor, "r") as f:
                reader = csv.reader(f)
                self.seznam = [row[0] for row in reader]
                self.listbox.delete(0, tk.END)
                for polozka in self.seznam:
                    self.listbox.insert(tk.END, polozka)
            messagebox.showinfo("Načteno", "Seznam byl načten z CSV souboru.")

    def ulozit_pickle(self):
        soubor = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle", "*.pkl")])
        if soubor:
            with open(soubor, "wb") as f:
                pickle.dump(self.seznam, f)
            messagebox.showinfo("Uloženo", "Seznam byl uložen do Pickle souboru.")

    def nacist_pickle(self):
        soubor = filedialog.askopenfilename(filetypes=[("Pickle", "*.pkl")])
        if soubor:
            with open(soubor, "rb") as f:
                self.seznam = pickle.load(f)
                self.listbox.delete(0, tk.END)
                for polozka in self.seznam:
                    self.listbox.insert(tk.END, polozka)
            messagebox.showinfo("Načteno", "Seznam byl načten z Pickle souboru.")



if __name__ == "__main__":
    root = tk.Tk()
    app = SeznamApp(root)
    root.mainloop()

