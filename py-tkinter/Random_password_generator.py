import tkinter as tk
import secrets 
import string

def generate():
	chrs=string.ascii_letters+string.digits+string.punctuation
	cnt=0
	x=secrets.SystemRandom().choice(chrs[:52])
	pwd=''.join([secrets.SystemRandom().choice(chrs) for i in range(7)])
	label['text']=x+pwd

root=tk.Tk()

canvas=tk.Canvas(root,height=500,width=600)
canvas.pack()

frame=tk.Frame(root)
frame.place(relx=0,rely=0,relwidth=1,relheight=1)

im=tk.PhotoImage(file='landscape.png')
im_l=tk.Label(frame,image=im)
im_l.pack()

label=tk.Label(frame,font=('Courier',25))
label.place(relx=0.5,rely=0.3,relwidth=0.5,relheight=0.1,anchor='center')

button=tk.Button(frame,text='Generate Password',command=generate,bg='lightgreen',fg='#ff4d4d',font=('Courier',10,'bold'))
button.place(relx=0.5,rely=0.5,relwidth=0.25,relheight=0.1,anchor='center')

root.mainloop()
