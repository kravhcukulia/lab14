from tkinter import *
from random import *
from tkinter import messagebox

a = []

def mas():
    n = edit1.get()
    if not n:
        messagebox.showerror('Помилка', 'Розмірність масиву не вказана')
        return

    n = int(n)
    a.clear()
    listbox1.delete(0, END)
    listbox2.delete(0, END)

    for i in range(n):
        val = randint(-50, 50)
        original = val
        if val % 4 == 0:
            val *= 2
            listbox1.insert(END, f'{original} → {val}')
        else:
            listbox1.insert(END, str(val))
        a.append(val)


def sort():
    n = len(a)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if a[i] < a[i + 1]:  # Сортування за спаданням
                a[i], a[i + 1] = a[i + 1], a[i]
    listbox2.delete(0, END)
    for i in range(n):
        listbox2.insert(END, a[i])

def compute_sum():
    s = sum(a)
    label4['text'] = 'Сума = ' + str(s)

def about_author():
    messagebox.showinfo('Про автора', 'Автор: Ім\'я автора\nEmail: email@example.com')

def problem_statement():
    messagebox.showinfo('Умова задачі', 'Збільшити вдвічі всі елементи одновимірного масиву, кратні 4.\nВиконати сортування елементів масиву за спаданням методом обміну.')

def set_light_theme():
    root['bg'] = 'lightgray'
    for w in widgets:
        w['bg'] = 'white' if isinstance(w, (Listbox, Entry)) else 'lightgray'
        w['fg'] = 'black'

def set_dark_theme():
    root['bg'] = 'black'
    for w in widgets:
        w['bg'] = 'gray80'
        w['fg'] = 'white'

def set_default_theme():
    root['bg'] = '#F0F0F0'
    for w in widgets:
        w['bg'] = '#FFFFFF' if isinstance(w, (Listbox, Entry)) else '#F0F0F0'
        w['fg'] = 'black'

def do_popup(event):
    popupmenu.post(event.x_root, event.y_root)

root = Tk()
root.title('Масиви')
root.geometry('600x300')

label1 = Label(text='Вихідний масив')
label2 = Label(text='Посортований масив')
label1.place(x=20, y=30)
label2.place(x=200, y=30)

listbox1 = Listbox(height=10, width=20)
listbox2 = Listbox(height=10, width=20)
listbox1.place(x=20, y=70)
listbox2.place(x=200, y=70)

label3 = Label(text='Кількість елементів масиву:')
label3.place(x=400, y=30)

edit1 = Entry()
edit1.place(x=400, y=70)

button1 = Button(text='Заповнити', width=20, command=mas)
button1.place(x=400, y=100)

button2 = Button(text='Сортувати', width=20, command=sort)
button2.place(x=400, y=130)

button3 = Button(text='Обчислити суму', width=20, command=compute_sum)
button3.place(x=400, y=160)

label4 = Label(text='Сума =')
label4.place(x=400, y=210)

widgets = [label1, label2, label3, label4, listbox1, listbox2, edit1, button1, button2, button3]

main_menu = Menu(root)
root.config(menu=main_menu)

array_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Дії з масивом', menu=array_menu)
array_menu.add_command(label='Заповнити', command=mas)
array_menu.add_command(label='Сортувати', command=sort)
array_menu.add_command(label='Обчислити суму', command=compute_sum)

about_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Про програму', menu=about_menu)
about_menu.add_command(label='Про автора', command=about_author)
about_menu.add_command(label='Умова задачі', command=problem_statement)

popupmenu = Menu(root, tearoff=0)
popupmenu.add_command(label="Світлий", command=set_light_theme)
popupmenu.add_command(label="Темний", command=set_dark_theme)
popupmenu.add_command(label="Відновити початкові кольори", command=set_default_theme)
root.bind("<Button-3>", do_popup)

root.mainloop()