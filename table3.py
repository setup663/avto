from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from sqlite3 import *

# Получение информации из первой таблицы в бд
def information3():
    with connect('database\database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cars")
        return cursor.fetchall()


# функция создания окна второй таблицы
def create_table3():
    def on_select3(event):
        global id_sel3
        global set_col3
        id_sel3 = table3.item(table3.focus())
        id_sel3 = id_sel3.get('values')[0]
        col = table3.identify_column(event.x)
        set_col3 = table3.column(col)
        set_col3 = set_col3.get('id')
        if set_col3 == 'Фио студента':
            set_col3 = 'FIO'
        elif set_col3 == 'Группа':
            set_col3 = 'group_name'

    #  Главное окно
    window = Tk()
    window.title('subd')
    window.minsize(700, 450)

    frame3_change = Frame(window, width=150, height=150, bg='white')  # блок для функционала субд
    frame3_view = Frame(window, width=150, height=150, bg='white')  # блок для просмотра базы данных
    frame3_change.place(relx=0, rely=0, relwidth=1, relheight=1)
    frame3_view.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)




    # функция обновления таблицы2
    def refresh3():
        with connect('database\database.db') as db:
            cursor = db.cursor()
            cursor.execute(''' SELECT * FROM cars ''')
            [table3.delete(i) for i in
             table3.get_children()]
            [table3.insert('', 'end', values=row) for row in cursor.fetchall()]


    heads3 = ['id', 'car_marks']
    table3 = ttk.Treeview(frame3_view, show='headings')  # дерево выполняющее свойство таблицы
    table3['columns'] = heads3  # длина таблицы
    table3.bind('<ButtonRelease-1>', on_select3)

    # заголовки столбцов и их расположение
    for header in heads3:
        table3.heading(header, text=header, anchor='center')
        table3.column(header, anchor='center')

    # добавление из бд в таблицу приложения
    for row in information3():
        table3.insert('', END, values=row)
    table3.pack(expand=YES, fill=BOTH, side=LEFT)




