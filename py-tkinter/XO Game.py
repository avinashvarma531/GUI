from tkinter import *
import time

turn=0
def check():
	x,o=['X']*3,['O']*3
	l=[b1['text'],b2['text'],b3['text']]
	if l==x or l==o:
		return 'x' if l==x else 'o'
	l=[b4['text'],b5['text'],b6['text']]
	if l==x or l==o:
		return 'x' if l==x else 'o'
	l=[b7['text'],b8['text'],b9['text']]
	if l==x or l==o:
		return 'x' if l==x else 'o'
	l=[b1['text'],b5['text'],b9['text']]
	if l==x or l==o:
		return 'x' if l==x else 'o'
	l=[b3['text'],b5['text'],b7['text']]
	if l==x or l==o:
		return 'x' if l==x else 'o'
	l=[b1['text'],b4['text'],b7['text']]
	if l==x or l==o:
		return 'x' if l==x else 'o'
	l=[b2['text'],b5['text'],b8['text']]
	if l==x or l==o:
		return 'x' if l==x else 'o'
	l=[b3['text'],b6['text'],b9['text']]
	if l==x or l==o:
		return 'x' if l==x else 'o'
	s=set([b1['text'],b2['text'],b3['text'],b4['text'],b5['text'],b6['text'],b7['text'],b8['text'],b9['text']])
	if s|set(['X','O'])==set(['X','O']):
		return 'd'
	del l
	return None

def manage(b):
	global turn
	if b['text']==' ':
		if turn==0:
			b['text']='X'
			turn=1
			l1['text']='O\'s turn'
		else:
			b['text']='O'
			turn=0
			l1['text']='X\'s turn'
		l2['text']=''
		res=check()
		if res!=None:
			if res!='d':
				l1['text']='X is the Winner !!' if res=='x' else 'O is the Winner  !!'
			else:
				l1['text']='Match DRAW !!'
			deactivateall()
	else:
		l2['text']='Already occuppied !'
def deactivateall():
	b1['state']='disabled'
	b2['state']='disabled'
	b3['state']='disabled'
	b4['state']='disabled'
	b5['state']='disabled'
	b6['state']='disabled'
	b7['state']='disabled'
	b8['state']='disabled'
	b9['state']='disabled'

def activateall():
	b1['state']='normal'
	b2['state']='normal'
	b3['state']='normal'
	b4['state']='normal'
	b5['state']='normal'
	b6['state']='normal'
	b7['state']='normal'
	b8['state']='normal'
	b9['state']='normal'

def clear():
	global turn
	turn=0
	b1['text']=' '
	b2['text']=' '
	b3['text']=' '
	b4['text']=' '
	b5['text']=' '
	b6['text']=' '
	b7['text']=' '
	b8['text']=' '
	b9['text']=' ' 
	l1['text']='X\'s turn'
	l2['text']=''
	activateall()

root=Tk()
root.title('XO GAME')

#im=PhotoImage(file='landscape.png')
#im_label=Label(root,image=im)
#im_label.pack()

canvas=Canvas(root,height=500,width=600,bg='cyan')
canvas.pack()

frame=Frame(root,bd=2.5,bg='red')
frame.place(relx=0.5,rely=0.5,relwidth=0.4,relheight=0.4,anchor='center')

b1=Button(frame,bg='lightgray',text=' ',command=lambda:manage(b1),font=('Courier',20,"bold"))
b1.place(relx=0,rely=0,relwidth=0.33,relheight=0.33)

b2=Button(frame,bg='lightgray',text=' ',command=lambda:manage(b2),font=('Courier',20,"bold"))
b2.place(relx=0.5,rely=0,relwidth=0.33,relheight=0.33,anchor='n')

b3=Button(frame,bg='lightgray',text=' ',command=lambda:manage(b3),font=('Courier',20,"bold"))
b3.place(relx=1,rely=0,relwidth=0.33,relheight=0.33,anchor='ne')

b4=Button(frame,bg='lightgray',text=' ',command=lambda:manage(b4),font=('Courier',20,"bold"))
b4.place(relx=0,rely=0.5,relwidth=0.33,relheight=0.33,anchor='w')

b5=Button(frame,bg='lightgray',text=' ',command=lambda:manage(b5),font=('Courier',20,"bold"))
b5.place(relx=0.5,rely=0.5,relwidth=0.33,relheight=0.33,anchor='center')

b6=Button(frame,bg='lightgray',text=' ',command=lambda:manage(b6),font=('Courier',20,"bold"))
b6.place(relx=1,rely=0.5,relwidth=0.33,relheight=0.33,anchor='e')

b7=Button(frame,bg='lightgray',text=' ',command=lambda:manage(b7),font=('Courier',20,"bold"))
b7.place(relx=0,rely=1,relwidth=0.33,relheight=0.33,anchor='sw')

b8=Button(frame,bg='lightgray',text=' ',command=lambda:manage(b8),font=('Courier',20,"bold"))
b8.place(relx=0.5,rely=1,relwidth=0.33,relheight=0.33,anchor='s')

b9=Button(frame,bg='lightgray',text=' ',command=lambda:manage(b9),font=('Courier',20,"bold"))
b9.place(relx=1,rely=1,relwidth=0.33,relheight=0.33,anchor='se')

clb=Button(root,text='New Game',font=('Courier',10,"bold"),command=clear,bg='red',fg='cyan',cursor='spider')
clb.place(relx=0.5,rely=0.8,anchor='center')

l1=Label(root,font=('Courier',25),text='X\'s turn',bg='cyan')
l1.place(relx=0.5,rely=0.2,anchor='center')

l2=Label(root,font=('Courier',25),bg='cyan')
l2.place(relx=0.5,rely=0.9,anchor='center')

root.mainloop()