import boto3
import os
from tkinter import *
import tkinter as tk
import codecs
from tkinter import ttk
from tkinter import filedialog
import time
from threading import Thread
import requests as rq
os.environ['AWS_DEFAULT_REGION'] = 'Russia'
access_key = 'r0ejPWnsow_aWG5HkJPw'
secret_key = 'GFyYEzWvs0nXx73Sa9BvS7OHtTDfPhMyPxlUOyIE'

session = boto3.session.Session()
s3 = session.client(
		service_name='s3',
		endpoint_url='https://storage.yandexcloud.net',
		aws_access_key_id=access_key,
		aws_secret_access_key=secret_key,
	)
login_bas=1

#
def add_f():
	if login_bas:
		print('add_f')

#
def rem_f():
	if login_bas:
		print('rem_f')

#
def rename_f():
	if login_bas:
		print('rename_f')

#
def share_f():
	if login_bas:
		print('share_f')

#
def edit_f():
	if login_bas:
		print('edit_f')

#
def open_f():
	if login_bas:
		print('open_f')

#
def down_f():
	if login_bas:
		print('down_f')

#
def upl_f():
	if login_bas:
		print('upl_f')

#
def del_local_f():
	if login_bas:
		print('del_local_f')

#
def del_cloud_f():
	if login_bas:
		print('del_cloud_f')

#
def an_auth():
	if login_bas:
		print('an_auth')

#
def settings():
	if login_bas:
		print('settings')



#
def stat_connekt():
	staaaatt['text'] = 'Подключение к серверу!'
	staaaatt['bg'] = 'yellow'
	time.sleep(5)
	while 1:

		if root.geometry():
			try:
				r = rq.get('https://functions.yandexcloud.net/d4ek6eurb4ek7b51tl99')
				scodet = r.status_code
				if scodet == 200:
					staaaatt['text'] = 'Связь с сервером есть!'
					staaaatt['bg'] = 'green'
				else:
					staaaatt['text'] = 'Нет связи с сервером!'
					staaaatt['bg'] = 'red'
			except:
				staaaatt['text'] = 'Нет связи с сервером!'
				staaaatt['bg'] = 'red'


			time.sleep(5)


#
def SAVE():
	pass







root = tk.Tk()
root.geometry("500x500")

root.title('CloudFILE')
#filename = filedialog.askopenfilename()

#f1
frame1 = tk.Frame(master=root,borderwidth=5)

Label(master=frame1, text="CloudFILE").pack(side=tk.LEFT)
tk.Button(frame1, text='ВОЙТИ', command=an_auth ).pack(fill=tk.Y, side=tk.RIGHT)

frame1.pack(fill=tk.X)


#f2
frame2 = tk.Frame(master=root,borderwidth=5)

n = ttk.Notebook(frame2)

frame21 = tk.Frame(master=n,borderwidth=5)
tree = ttk.Treeview(frame21)
tree['columns'] = ('path')
#tree.insert('', 'end', text='Listbox', values=('15KB', 'Yesterday', 'mark'))

tree.pack()
frame21.place(relx=.5, rely=.5, anchor="c", height=300, width=400)

frame22 = tk.Frame(master=n,borderwidth=5)
treec = ttk.Treeview(frame22)
treec['columns'] = ('path')
treec.insert('', 'end', text='Lis3tbox', values=('15KB', 'Yesterday', 'mark'))
treec.insert('', 'end', text='List3ox', values=('15KB', 'Yesterday', 'mark'))
treec.insert('', 'end', text='Li3stbox', values=('15KB', 'Yesterday', 'mark'))
treec.pack()
frame22.pack()

n.add(frame21, text='Локально')
n.add(frame22, text='Облако')
n.pack()

frame2.pack()


#f3
frame3 = tk.Frame(master=root,borderwidth=5)
tk.Button(frame3, text='Добавить файл', command=add_f ).grid(row=0, column=0, padx=10 , pady=2 , sticky="nsew")
tk.Button(frame3, text='Убрать файл', command=rem_f ).grid(row=0, column=1, padx=10 , pady=2 , sticky="nsew")

tk.Button(frame3, text='Переименовать', command=rename_f ).grid(row=1, column=0, padx=10, pady=2 , sticky="nsew")
tk.Button(frame3, text='Поделится', command=share_f ).grid(row=1, column=1, padx=10, pady=2 , sticky="nsew")

tk.Button(frame3, text='Редактировать', command=edit_f ).grid(row=2, column=0, padx=10, pady=2 , sticky="nsew")
tk.Button(frame3, text='Открыть', command=open_f ).grid(row=2, column=1, padx=10, pady=2 , sticky="nsew")

tk.Button(frame3, text='Скачать из облака', command=down_f ).grid(row=3, column=0, padx=10, pady=2 , sticky="nsew")
tk.Button(frame3, text='Загрузить в облако', command=upl_f ).grid(row=3, column=1, padx=10 , pady=2 , sticky="nsew")

tk.Button(frame3, text='Удалить локально', command=del_local_f ).grid(row=4, column=0, padx=10, pady=2 , sticky="nsew")
tk.Button(frame3, text='Удалить в облаке', command=del_cloud_f ).grid(row=4, column=1, padx=10 , pady=2 , sticky="nsew")

frame3.pack()


#4
frame4 = tk.Frame(master=root,borderwidth=5)

staaaatt = Label(master=frame4, text="Подключение к серверу!", bg='yellow')
staaaatt.pack(side=tk.LEFT)
tk.Button(frame4, text='НАСТРОЙКИ', command=settings ).pack(side=tk.RIGHT)

frame4.pack(fill=tk.X)




time.sleep(1)
Thread(target=stat_connekt).start()



root.mainloop()
