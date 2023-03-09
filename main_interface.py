from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
import mysql.connector
from add_window import *
from sql_connector import my_connect


def total_sum():
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT SUM(pret) FROM produse")
    x = my_conn.fetchone()
    for value in x:
        return value


def run_add_window():
    main()


def refresh_tables():
    total_sum()
    my_list()
    my_list_2()
    my_list_3()
    totalLabel.config(text="Pret Total: " + str(total_sum()) + " lei")



# FRAME
root = Tk()
root.title('Lista de cumparaturi')
my_interface = ttk.Notebook(root)
my_interface.pack(pady=10)

# build function should be loooped in DB
my_frame1 = Frame(my_interface, width=700, height=700, bg="grey")
my_frame2 = Frame(my_interface, width=700, height=700, bg="grey")
my_frame3 = Frame(my_interface, width=700, height=700, bg="grey")
my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)
my_frame3.pack(fill="both", expand=1)
my_interface.add(my_frame1, text="Alimente")
my_interface.add(my_frame2, text="Ingrijire Personala")
my_interface.add(my_frame3, text="Bauturi")
totalLabel = Label(root, font=("Helvetica", 10,))
totalLabel.pack(pady=20, side=RIGHT)
my_button = Button(root, background="orange", width=15, text="Adauga produse", command=run_add_window)
my_ref_button = Button(root, background="orange", width=15, text="Actualizare Lista", command=refresh_tables)
my_button.pack(side=LEFT)
my_ref_button.pack(side=LEFT)


def my_list():
    for w in my_frame1.grid_slaves():
        w.grid_forget()

    my_conn = my_connect.cursor(buffered=True)
    my_conn.execute("SELECT Nume,Cantitate,Pret FROM produse  WHERE Categorie LIKE 'Alimente' LIMIT 28")
    e = Label(my_frame1, width=40, fg="yellow", background='blue', text="Denumire", anchor='w', relief='ridge')
    e.grid(row=0, column=0)
    e = Label(my_frame1, width=40, fg="yellow", background='blue', text="Cantitate", anchor='w', relief='ridge')
    e.grid(row=0, column=1)
    e = Label(my_frame1, width=40, fg="yellow", background='blue', text="Pret", anchor='w', relief='ridge')
    e.grid(row=0, column=2)
    i = 0
    for x in my_conn:
        for j in range(len(x)):
            e = Label(my_frame1, width=40, fg="black", background='green', text=x[j], anchor='w', relief='ridge')
            e.grid(row=i + 1, column=j)
        e = Button(my_frame1, text='x', command=lambda d=x[0], n=x[1]: my_delete(n, d))
        e.grid(row=i + 1, column=j + 1)
        i = i + 1


def my_list_2():
    for w in my_frame2.grid_slaves():
        w.grid_forget()
    my_conn = my_connect.cursor(buffered=True)
    my_conn.execute("SELECT Nume,Cantitate,Pret FROM produse WHERE Categorie LIKE 'Ingrijire Personala' LIMIT 28")
    e = Label(my_frame2, width=40, fg="yellow", background='blue', text="Denumire", anchor='w', relief='ridge')
    e.grid(row=0, column=0)
    e = Label(my_frame2, width=40, fg="yellow", background='blue', text="Cantitate", anchor='w', relief='ridge')
    e.grid(row=0, column=1)
    e = Label(my_frame2, width=40, fg="yellow", background='blue', text="Pret", anchor='w', relief='ridge')
    e.grid(row=0, column=2)
    i = 0
    for x in my_conn:
        for j in range(len(x)):
            e = Label(my_frame2, width=40, fg="black", background='green', text=x[j], anchor='w', relief='ridge')
            e.grid(row=i + 1, column=j)
        e = Button(my_frame2, text='x', command=lambda d=x[0], n=x[1]: my_delete(n, d))
        e.grid(row=i + 1, column=j + 1)
        i = i + 1


def my_list_3():
    for w in my_frame3.grid_slaves():
        w.grid_forget()
    my_conn = my_connect.cursor(buffered=True)
    my_conn.execute("SELECT Nume,Cantitate,Pret FROM produse WHERE Categorie LIKE 'Bauturi' LIMIT 28")
    e = Label(my_frame3, width=40, fg="yellow", background='blue', text="Denumire", anchor='w', relief='ridge')
    e.grid(row=0, column=0)
    e = Label(my_frame3, width=40, fg="yellow", background='blue', text="Cantitate", anchor='w', relief='ridge')
    e.grid(row=0, column=1)
    e = Label(my_frame3, width=40, fg="yellow", background='blue', text="Pret", anchor='w', relief='ridge')
    e.grid(row=0, column=2)
    i = 0
    for x in my_conn:
        for j in range(len(x)):
            e = Label(my_frame3, width=40, fg="black", background='green', text=x[j], anchor='w', relief='ridge')
            e.grid(row=i + 1, column=j)
        e = Button(my_frame3, text='x', command=lambda d=x[0], n=x[1]: my_delete(n, d))
        e.grid(row=i + 1, column=j + 1)
        i = i + 1


def my_delete(id, name):
    my_conn = my_connect.cursor(buffered=True)
    my_conn.execute("DELETE FROM produse where nume LIKE " + "'" + str(name) + "'")
    my_connect.commit()
    refresh_tables()


# main loop
refresh_tables()
root.mainloop()