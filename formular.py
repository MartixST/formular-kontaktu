import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Formulař')

def hello():
    print("Ahoj!")
    
def zrusitVyber():
    jmenoIn.delete(0, tk.END)
    prijmeniIn.delete(0, tk.END)
    rodneCisloIn.delete(0, tk.END)
    uliceIn.delete(0, tk.END)
    cpIn.delete(0, tk.END)
    mestoIn.delete(0, tk.END)
    pscIn.delete(0, tk.END)
    poznamkaIn.delete('1.0', tk.END)
    
def novyZaznam():
    tree.insert('', tk.END, values=(jmenoIn.get(), prijmeniIn.get(), rodneCisloIn.get(), uliceIn.get(),
                                    cpIn.get(), mestoIn.get(), pscIn.get(), poznamkaIn.get('1.0', tk.END)))
    zrusitVyber()
    
def treeSelection(event):
    global selectedItemId
    selectedItem = tree.selection()
    
    if selectedItem:
        selectedItemId = selectedItem[0]
        item = tree.item(selectedItem)
        record = item['values']
        zrusitVyber()
        jmenoIn.insert(0, record[0])
        prijmeniIn.insert(0, record[1])
        rodneCisloIn.insert(0, record[2])
        uliceIn.insert(0, record[3])
        cpIn.insert(0, record[4])
        mestoIn.insert(0, record[5])
        pscIn.insert(0, record[6])
        poznamkaIn.insert('1.0', record[7])
        
        
def updateSelection():
    if selectedItemId:
        tree.item(selectedItemId, values=(jmenoIn.get(), prijmeniIn.get(), rodneCisloIn.get(), uliceIn.get(),
                                          cpIn.get(), mestoIn.get(), pscIn.get(), poznamkaIn.get()))
        zrusitVyber()
        



hlavniMenu = tk.Menu(root)
menuSoubor = tk.Menu(hlavniMenu, tearoff=0)
menuUpravy = tk.Menu(hlavniMenu, tearoff=0)
menuNapoveda = tk.Menu(hlavniMenu, tearoff=0)

tree = ttk.Treeview(root, columns=('first_name', 'last_name', 'birth_number', 'ulice', 'cp', 
                                   'mesto', 'psc', 'poznamka'), show='headings')

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)

celeJmeno = ttk.Frame(root)
jmeno = tk.Label(celeJmeno, text='Jmeno:')
jmenoIn = tk.Entry(celeJmeno, width=20)
prijmeni = tk.Label(celeJmeno, text='Prijmeni:')
prijmeniIn = tk.Entry(celeJmeno, width=20)
rodneCislo = tk.Label(celeJmeno, text='Rodne cislo:')
rodneCisloIn = tk.Entry(celeJmeno, width=20)

notebook = ttk.Notebook(root)
adresaFrame = ttk.Frame(notebook, height=90)
labelAdresa = ttk.LabelFrame(adresaFrame, text="Adresa",)
midLabelAdresa = tk.Frame(labelAdresa)
ulice = tk.Label(midLabelAdresa, text='Ulice:')
uliceIn = tk.Entry(midLabelAdresa, width=13)
cp = tk.Label(midLabelAdresa, text='č.p.:')
cpIn = tk.Entry(midLabelAdresa, width=7)
mesto = tk.Label(midLabelAdresa, text='Město:')
mestoIn = tk.Entry(midLabelAdresa, width=25)
psc = tk.Label(midLabelAdresa, text='PSČ:')
pscIn = tk.Entry(midLabelAdresa, width=8)
poznamkaFrame = ttk.Frame(notebook, height=90)
labelPoznamka = ttk.LabelFrame(poznamkaFrame, text="Poznámka",)
poznamkaIn = tk.Text(labelPoznamka, height=4, width=70)

buttonsAndLogin = ttk.Frame(root)
buttonsFrame = ttk.Frame(buttonsAndLogin)
loginFrame = ttk.Frame(buttonsAndLogin)
buttonZrusit = ttk.Button(buttonsFrame, text="Zrušit", command=zrusitVyber)
buttonNovyZaz = ttk.Button(buttonsFrame, text="Nový záznam", command=novyZaznam)
buttonUlozitZaz = ttk.Button(buttonsFrame, text="Uložit záznam", command=updateSelection)

login = ttk.Label(loginFrame, text="Vladislav Shumilin, SHU0020")

#------------------------------MENU----------------------------------------#

menuSoubor.add_command(label="Otevřít", command=hello)
menuSoubor.add_command(label="Uložit", command=hello)
menuSoubor.add_separator()
menuSoubor.add_command(label="Pryč", command=root.quit)
hlavniMenu.add_cascade(label="Soubor", menu=menuSoubor)


menuUpravy.add_command(label="Vyjmout", command=hello)
menuUpravy.add_command(label="Kopírovat", command=hello)
menuUpravy.add_command(label="Vložit", command=hello)
hlavniMenu.add_cascade(label="Nastavení", menu=menuUpravy)


menuNapoveda.add_command(label="O aplikaci", command=hello)
hlavniMenu.add_cascade(label="Nápověda", menu=menuNapoveda)

root.config(menu=hlavniMenu)

#-------------------------------TABLE---------------------------------------#

tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('birth_number', text='Birth Number')

tree.insert('', tk.END, values=("John", "Roe", "045216/1512", "17.listopadu", "15", "Ostrava", "70800", 'Dobrý'))
tree.insert('', tk.END, values=("Jane", "Doe", "901121/7238", "Kounicova", "296/36", "Brno", "60200", 'Zlá'))

tree.column('ulice', width=0, stretch=False)
tree.column('cp', width=0, stretch=False)
tree.column('mesto', width=0, stretch=False)
tree.column('psc', width=0, stretch=False)
tree.column('poznamka', width=0, stretch=False)

tree.grid(row=0, column=0, sticky='nsew')

tree.configure(yscroll=scrollbar.set)
tree.bind('<<TreeviewSelect>>', treeSelection)  

scrollbar.grid(row=0, column=1, sticky='ns')

#--------------------------------FULL NAME INFO--------------------------------------#

celeJmeno.grid()

jmeno.grid(row=0, column=0, sticky='e')
jmenoIn.grid(row=0, column=1)
prijmeni.grid(row=1, column=0, sticky='e')
prijmeniIn.grid(row=1, column=1)
rodneCislo.grid(row=2, column=0, sticky='e')
rodneCisloIn.grid(row=2, column=1)

#----------------------------------ADRESS INFO------------------------------------#

notebook.grid(row=2, column=0, sticky='nsew')

notebook.add(adresaFrame, text='Adresa')
labelAdresa.pack(expand=1, fill='both')
midLabelAdresa.pack(side='bottom')
ulice.grid(row=0, column=0, sticky='e')
uliceIn.grid(row=0, column=1, sticky='w')
cp.grid(row=0, column=2, sticky='w')
cpIn.grid(row=0, column=3)
mesto.grid(row=1, column=0, sticky='e')
mestoIn.grid(row=1, column=1, columnspan=3, sticky='w')
psc.grid(row=2, column=0, sticky='e')
pscIn.grid(row=2, column=1, sticky='w')

notebook.add(poznamkaFrame, text='Poznámka')
labelPoznamka.pack(expand=1, fill='both')
poznamkaIn.pack()


#-------------------------------BUTTONS---------------------------------------#

buttonsAndLogin.grid(sticky='nwse', pady=10)

loginFrame.pack(side='right')
buttonsFrame.pack(side='right', padx=30)
buttonZrusit.pack(side='left')
buttonNovyZaz.pack(side='left')
buttonUlozitZaz.pack(side='left')
login.pack(side='right')

root.mainloop()