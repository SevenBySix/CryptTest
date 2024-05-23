import os
from cryptography.fernet import Fernet

from tkinter import *


class MyWindow:
    def __init__(self, win):
    
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)
        #token = f.encrypt(b"A really secret message. Not for prying eyes.")
        
        
        self.textLabel=Label(win, text='targetText')#t1
        self.keyLabel=Label(win, text='key')#t2
        self.resultLabel=Label(win, text='Result')#t3
        
        self.textFeild=Entry(bd=3)
        self.keyFeild=Entry()
        self.resultFeild=Entry()
        
        
        self.encryptButton=Button(win, text='Encrypt', command=self.Encrypt)
        self.decryptButton=Button(win, text='Decrypt', command=self.Decrypt)
        genKeyButton = Button(window, text='newKey', command = self.generateKey)
        
        self.textLabel.place(x=100, y=50)
        self.textFeild.place(x=200, y=50)
        self.keyLabel.place(x=100, y=100)
        self.keyFeild.place(x=200, y=100)
        self.keyFeild.insert(END, self.key)
        
        self.encryptButton.place(x=100, y=150)
        self.decryptButton.place(x=200, y=150)
        genKeyButton.place(x=300, y =150);
        
        self.resultLabel.place(x=100, y=200)
        self.resultFeild.place(x=200, y=200)
        
    def Encrypt(self):
        self.resultFeild.delete(0, 'end')
        self.text=self.textFeild.get()
        
        self.ciphertext = self.f.encrypt(bytes(self.text, 'utf-8'))
        
        self.resultFeild.insert(END, self.ciphertext)
        self.textFeild.delete(0, 'end')
        self.textFeild.insert(END, self.ciphertext)
    def Decrypt(self):
        '''
        self.resultFeild.delete(0, 'end')
        self.text=self.f.decrypt(self.ciphertext)
        
        self.textFeild.delete(0, 'end')
        self.resultFeild.insert(END, self.text)
        '''
        self.resultFeild.delete(0, 'end')
        
        
        
        self.resultFeild.insert(END, self.f.decrypt(bytes(self.textFeild.get(), 'utf-8')))
        self.textFeild.delete(0, 'end')
    def generateKey(self):
        self.keyFeild.delete(0, 'end')
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)
        self.keyFeild.insert(END, self.key)

window=Tk()
mywin=MyWindow(window)
window.title('CryptTest')
window.geometry("400x300+10+10")
window.mainloop()