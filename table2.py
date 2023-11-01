from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from sqlite3 import *

# Получение информации из первой таблицы в бд
def information2():
    with connect('database\database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM managers")
        return cursor.fetchall()



# функция создания окна второй таблицы
def create_table2():
    def on_select2(event):
        global id_sel2
        global set_col2
        id_sel2 = table2.item(table2.focus())
        id_sel2 = id_sel2.get('values')[0]
        col = table2.identify_column(event.x)
        set_col2 = table2.column(col)
        set_col2 = set_col2.get('id')
        if set_col2 == 'Фио студента':
            set_col2 = 'FIO'
        elif set_col2 == 'Группа':
            set_col2 = 'group_name'

    #  Главное окно
    window = Tk()
    window.title('subd')
    window.minsize(700, 450)

    frame2_change = Frame(window, width=150, height=150, bg='white')  # блок для функционала субд
    frame2_view = Frame(window, width=150, height=150, bg='white')  # блок для просмотра базы данных
    frame2_change.place(relx=0, rely=0, relwidth=1, relheight=1)
    frame2_view.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)




    # функция обновления таблицы2
    def refresh2():
        with connect('database\database.db') as db:
            cursor = db.cursor()
            cursor.execute(''' SELECT * FROM managers ''')
            [table2.delete(i) for i in
             table2.get_children()]
            [table2.insert('', 'end', values=row) for row in cursor.fetchall()]


    heads2 = ['id', 'Фио']
    table2 = ttk.Treeview(frame2_view, show='headings')  # дерево выполняющее свойство таблицы
    table2['columns'] = heads2  # длина таблицы
    table2.bind('<ButtonRelease-1>', on_select2)

    # заголовки столбцов и их расположение
    for header in heads2:
        table2.heading(header, text=header, anchor='center')
        table2.column(header, anchor='center')

    # добавление из бд в таблицу приложения
    for row in information2():
        table2.insert('', END, values=row)
    table2.pack(expand=YES, fill=BOTH, side=LEFT)




