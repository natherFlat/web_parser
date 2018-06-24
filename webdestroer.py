from  tkinter import *
import  pymysql.cursors
from tkinter import messagebox
import requests
#import soup
from bs4 import BeautifulSoup
import csv


def get_data(var,s):
    print(var.get())
    def err():

        def cloze():
            tk.destroy()
        tk = Tk()
        tk.title('Ошибка')
        label = Label(tk,text = 'Выбирите формат')
        label.pack(side= 'top',fill='x',pady =10)
        b1 = Button(tk,text = 'ok',command = cloze)
        b1.pack()
        tk.mainloop()
    if (var.get() == 1) :
        if(s.find('wiki')!=-1):
            page = requests.get(s)
            soup = BeautifulSoup(page.text, 'html.parser')
            last_links = soup.find(class_='thumb tright')
            if(str(last_links) != '' ):
                last_links.decompose()
            out = open('decomtext.txt','w')
            mv_parser_output = soup.find(class_='mw-parser-output')
            list_tag_p = mv_parser_output.find_all('p')
            for tags_p in list_tag_p :
                out.write(tags_p.text)
        if(s.find('habr')!=-1):
            page = requests.get(s)
            soup = BeautifulSoup(page.text, 'html.parser')
            last_links = soup.find(class_='post__meta')
            if(str(last_links) != '' ):
                last_links.decompose()
            last_links = soup.find(class_='post__hubs post__hubs_full-post inline-list')
            if(str(last_links) != '' ):
                last_links.decompose()
            post_text = soup.find(class_='post__text post__text-html js-mediator-article')
            out = open('decomtext.txt','w')
            out.write(post_text.get_text())
    elif(var.get()==2):
        if(s.find('wiki')!=-1):
            page = requests.get(s)
            soup = BeautifulSoup(page.text, 'html.parser')
            last_links = soup.find(class_='thumb tright')
            if(str(last_links) != '' ):
                last_links.decompose()
                out = csv.writer(open('decomtext.csv','w'))
                mv_parser_output = soup.find(class_='mw-parser-output')
                list_tag_p = mv_parser_output.find_all('p')
                for tags_p in list_tag_p :
                    out.writerow([tags_p.get_text()])
        if(s.find('habr')!=-1):
            page = requests.get(s)
            soup = BeautifulSoup(page.text, 'html.parser')
            last_links = soup.find(class_='post__meta')
            if(str(last_links) != '' ):
                last_links.decompose()
            last_links = soup.find(class_='post__hubs post__hubs_full-post inline-list')
            if(str(last_links) != '' ):
                last_links.decompose()
            post_text = soup.find(class_='post__text post__text-html js-mediator-article')
            out = csv.writer(open('decomtext.csv','w'))
            out.writerow([post_text.get_text()])
    else:
        err()
        
       

root =  Tk()





    
root.geometry('1200x700')
root.title('WebDestroer')
LARGE_FONT = ('Times New Roman',13)
var = IntVar()

frame1=Frame(root,width=300, height=600,bg='red',bd=5)

button1=Button(frame1,text=u'Получить базу данных',font = LARGE_FONT,bg = '#FFFF00')
button1.pack()
button1.place(x=50,y=50)
button1.bind('<Button-1>', lambda event: data_base())

def data_base():
    connection =pymysql.connect(host = 'neytnijo.beget.tech',user ='neytnijo_bd',password='dedscp451',database='neytnijo_bd')
    db = open('for_data_base.txt','w')
    try:
  
 
        with connection.cursor() as cursor:
       
        # SQL 
            sql = "SELECT * FROM users "
        
      
            cursor.execute(sql)
            for row in cursor :
                db.write(str(row)+'\n')
                
    finally:
    # Закрыть соединение (Close connection).      
        connection.close()

frame1.pack(fill=None, expand=False)
frame1.place(x=100,y=50)

frame2 =  Frame(root, width = 300,height = 600, bg = 'blue',bd = 5)

label_site = Label(root,text = 'имя сайта',font = LARGE_FONT,bg= '#00FF00')
label_site.place(x = 800,y = 70)

entry_s = Entry(root)
entry_s.pack()
entry_s.place(x=760,y=120)

button_s = Button(root,text=u'Получчить данные',bg='blue')
button_s.pack()
button_s.place(x=770,y =150)
button_s.bind('<Button>',lambda event : get_data(var,str(entry_s.get())))


rbutton1=Radiobutton(root,text='txt',variable=var,value=1,bg='#00FF00')
rbutton2=Radiobutton(root,text='csv',variable=var,value=2,bg='#00FF00')
rbutton1.pack()
rbutton1.place(x = 760,y =190)
rbutton2.pack()
rbutton2.place(x = 760,y =210)

frame2.pack(fill = None,expand = False)
frame2.place(x=700,y=50)


root.mainloop()
