from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import table2 as table2
import table3 as table3
import table4 as table4
from sqlite3 import *

# Получение информации из первой таблицы в бд
def information():
    with connect('database\database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM buyers")
        return cursor.fetchall()

#  Главное окно
window = Tk()
window.title('subd')
window.minsize(700, 450)

frame_change = Frame(window, width=150, height=150, bg='white')  # блок для функционала субд
frame_view = Frame(window, width=150, height=150, bg='white')  # блок для просмотра базы данных
frame_change.place(relx=0, rely=0, relwidth=1, relheight=1)
frame_view.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


# Функция on_select
# при нажатии по ячейке Treview, создается глобальная переменная с id и column
def on_select(event):
    global id_sel
    global set_col
    id_sel = table.item(table.focus())
    id_sel = id_sel.get('values')[0]
    col = table.identify_column(event.x)
    set_col = table.column(col)
    set_col = set_col.get('id')
    if set_col == 'Группа':
        set_col = 'group_name'

# функция обновления таблицы1
def refresh():
    with connect('database\database.db') as db:
        cursor = db.cursor()
        cursor.execute(''' SELECT * FROM table1 ''')
        [table.delete(i) for i in
         table.get_children()]
        [table.insert('', 'end', values=row) for row in cursor.fetchall()]


# порядок элементов
heads = ['id', 'fio']
table = ttk.Treeview(frame_view, show='headings')  # дерево выполняющее свойство таблицы
table['columns'] = heads  # длина таблицы
table.bind('<ButtonRelease-1>', on_select)

# заголовки столбцов и их расположение
for header in heads:
    table.heading(header, text=header, anchor='center')
    table.column(header, anchor='center')

# добавление из бд в таблицу приложения
for row in information():
    table.insert('', END, values=row)
table.pack(expand=YES, fill=BOTH, side=LEFT)

# контекстное меню в Главном окне
mainmenu = Menu(window)
window.config(menu=mainmenu)


# Кнопка вызова таблицы 2
create_new_table = ttk.Button(frame_change, text='Таблица 2', command=table2.create_table2)
create_new_table.grid(row=3, column=1, columnspan=2, sticky='w', padx=10, pady=10)
# Кнопка вызова таблицы 3
create_new_table3 = ttk.Button(frame_change, text='Таблица 3', command=table3.create_table3)
create_new_table3.grid(row=4, column=2, columnspan=2, sticky='w', padx=10, pady=10)
# Кнопка вызова таблицы 4
create_new_table3 = ttk.Button(frame_change, text='Таблица 4', command=table4.create_table4)
create_new_table3.grid(row=5, column=2, columnspan=2, sticky='w', padx=10, pady=10)

# скроллбар для treview
scrollpanel = ttk.Scrollbar(frame_view, command=table.yview)
table.configure(yscrollcommand=scrollpanel.set)
scrollpanel.pack(side=RIGHT, fill=Y)
table.pack(expand=YES, fill=BOTH)


window.mainloop()
