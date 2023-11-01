from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from sqlite3 import *

# Получение информации из первой таблицы в бд
def information4():
    with connect('database\database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM sales")
        return cursor.fetchall()

def information_man():
    with connect('database\database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT id FROM managers;")
        return cursor.fetchall()

def information_cars():
    with connect('database\database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT id FROM cars;")
        return cursor.fetchall()


# функция создания окна второй таблицы
def create_table4():
    def on_select4(event):
        global id_sel3
        global set_col3
        id_sel4 = table4.item(table4.focus())
        id_sel4 = id_sel3.get('values')[0]
        col = table4.identify_column(event.x)
        set_col4 = table4.column(col)
        set_col4 = set_col3.get('id')
        if set_col4 == 'Фио студента':
            set_col4 = 'FIO'
        elif set_col4 == 'Группа':
            set_col4 = 'group_name'

    lst_man = []
    for man in information_man():
        lst_man.append(*man,)

    lst_car = []
    for car in information_cars():
        lst_car.append(*car,)

    #  Главное окно
    window = Tk()
    window.title('subd')
    window.minsize(1200, 700)

    frame4_change = Frame(window, width=150, height=150, bg='white')  # блок для функционала субд
    frame4_view = Frame(window, width=150, height=150, bg='white')  # блок для просмотра базы данных
    frame4_change.place(relx=0, rely=0, relwidth=1, relheight=1)
    frame4_view.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)




    # функция обновления таблицы2
    def refresh4():
        with connect('database\database.db') as db:
            cursor = db.cursor()
            cursor.execute(''' SELECT * FROM sales ''')
            [table4.delete(i) for i in
             table4.get_children()]
            [table4.insert('', 'end', values=row) for row in cursor.fetchall()]

    def form_submit4():
        with connect('database\database.db') as db:
            cursor = db.cursor()
            id_m = comboExample.get()
            id_c
            insert_inf = (id_m)
            query = """ INSERT INTO sales (id_managers) VALUES (?)"""
            cursor.execute(query, insert_inf)
            db.commit()
            refresh4()


    heads4 = ['id_managers', 'id_cars, gos_nomer', 'id_buyers', 'data', 'price']
    table4 = ttk.Treeview(frame4_view, show='headings')  # дерево выполняющее свойство таблицы
    table4['columns'] = heads4  # длина таблицы
    table4.bind('<ButtonRelease-1>', on_select4)

    # заголовки столбцов и их расположение
    for header in heads4:
        table4.heading(header, text=header, anchor='center')
        table4.column(header, anchor='center')

    # добавление из бд в таблицу приложения
    for row in information4():
        table4.insert('', END, values=row)
    table4.pack(expand=YES, fill=BOTH, side=LEFT)

    # добавления новых групп в бд
    l_groups = ttk.Label(frame4_change, text="id_managers")
    comboExample = ttk.Combobox(frame4_change, values=lst_man)
    l_groups.grid(row=0, column=0, sticky='w', padx=10, pady=10)
    comboExample.grid(row=0, column=1, sticky='w', padx=10, pady=10)
    comboExample.current(0)

    # добавления новых групп в бд
    l_groups = ttk.Label(frame4_change, text="id_cars")
    comboExample = ttk.Combobox(frame4_change, values=lst_man)
    l_groups.grid(row=1, column=0, sticky='w', padx=10, pady=10)
    comboExample.grid(row=1, column=1, sticky='w', padx=10, pady=10)
    comboExample.current(0)


    btn2_submit = ttk.Button(frame4_change, text="Добавить", command=form_submit4)
    btn2_submit.grid(row=0, column=3, columnspan=2, sticky='w', padx=10, pady=10)