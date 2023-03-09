from tkinter import *
import mysql.connector
from sql_connector import my_connect
from tkinter import messagebox, ttk


query="SELECT  * FROM categorii"
cursor=my_connect.cursor()
cursor.execute(query)
tables = [row[0] for row in cursor]
print(tables)


def add_frame():
    nume_p=nume_produs.get()
    cantitate_p=cantitate_produs.get()
    #price = pret.get()
    #categorie=categorie_produs.get()
    #applying empty validation
    if nume_p=='' or cantitate_p=='':
        message.set("Introduceti datele")
    else:
      sql = "INSERT INTO Produse (Nume,Cantitate,Pret,categorie) VALUES ('%s','%s','%s','%s')" % (nume_produs.get(),cantitate_produs.get(),pret.get(),categorie_produs.get())
      print(sql)
      cursor.execute(sql)
      my_connect.commit()
      message.set("Produs Adaugat")

def main():
    global Interfata_produse
    Interfata_produse = Toplevel()
    Interfata_produse.title("Adaugare Produse")
    Interfata_produse.geometry("300x250")
    #declaring variable
    global  message;
    global nume_produs
    global cantitate_produs
    global categorie_produs
    global pret
    nume_produs = StringVar()
    cantitate_produs = StringVar()
    message = StringVar()
    categorie_produs = StringVar()
    pret = StringVar()
    #Variabile si functii pentru  introducerea produselor in DB.
    Label(Interfata_produse,width="700", text="Introduceti detaliile produsului", bg="orange",fg="white").pack()
    Label(Interfata_produse, text="Nume Produs  ").place(x=5,y=40)
    Entry(Interfata_produse, textvariable=nume_produs).place(x=105,y=42)
    Label(Interfata_produse, text="Cantitate").place(x=20,y=80)
    Entry(Interfata_produse, textvariable=cantitate_produs).place(x=105,y=82)
    Label(Interfata_produse, text="Pret Total (lei)").place(x=20,y=120)
    Entry(Interfata_produse, textvariable=pret).place(x=105,y=120)
    Label(Interfata_produse, text="Categorie",).place(x=20,y=150)
    cb1 = ttk.Combobox(Interfata_produse,text="Selecteaza*",values=tables,textvariable=categorie_produs).place(x=105,y=150)
    Label(Interfata_produse, text="",textvariable=message).place(x=90,y=210)
    Button(Interfata_produse, text="Adauga", width=10, height=1, bg="orange",command=add_frame).place(x=105,y=180)
    Interfata_produse.mainloop()
    ###

if __name__ == "__main__":
    main()