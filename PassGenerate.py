from tkinter import *
import secrets
import string

def mot_de_passe(entrée_lettre, entrée_chiffre, entrée_ponctuation, longeur) : 
    if entrée_lettre == 0 :
        lettre = ""
    else :
        lettre = string.ascii_letters
    if entrée_chiffre == 0 :
        chiffre = ""
    else :
        chiffre = string.digits
    if entrée_ponctuation == 0 :
        ponctuation = ""
    else :
        ponctuation = string.punctuation
    alphabet = lettre + chiffre + ponctuation
    password = ''.join(secrets.choice(alphabet) for i in range(longeur))
    return password
    
print(mot_de_passe(1, 0, 0, 10))

def rep() :
    nombre_de_caractres = entry2.get ()
    nombre_de_caractres = int(nombre_de_caractres)
    cochee1 = case_cochee1.get
    cochee2 = case_cochee2.get
    cochee3 = case_cochee3.get
    password = mot_de_passe(cochee1(),cochee2(),cochee3(),nombre_de_caractres)
    print(password)
    entry.delete(0, END)
    entry.insert(0, password)
    

fenetre = Tk()
fenetre.title("Password generator")
fenetre.geometry('700x400')
fenetre.minsize(700, 300)
fenetre.config(background= '#f2f2f2')
frame = Frame(fenetre, bg = '#f2f2f2')

#Titre

label_title = Label(frame, text= 'Enter the number of characters you want.', font=("Arial", 20), bg = '#f2f2f2', fg ='#000000')          #25 = taille police , bg = background texte ,  fg = front ground couleur texte.    On peut soit afficher dans la fenêtre soit dans la frame
label_title.pack()                                                                                                                            #afficher ce qui y a dans label_title.  Dans side on peut mettre side = YES pour avoir le texte tj au milieu

#entrée

entry2 = Entry(frame, text= "", font=("Arial", 25), bg = '#ececec', fg ='#000000')                                                         #25 = taille police , bg = background texte ,  fg = front ground couleur texte.    On peut soit afficher dans la fenêtre soit dans la frame
entry2.pack(fill=X)  

#case à cocher

case_cochee1 = IntVar()
case = Checkbutton(frame, text="letter",variable = case_cochee1 ,font=("Arial", 15), onvalue=1, offvalue=0)
case.pack()
case_cochee2 = IntVar()
case1 = Checkbutton(frame, text="digits",variable = case_cochee2 ,font=("Arial", 15), onvalue=1, offvalue=0)
case1.pack()
case_cochee3 = IntVar()
case2 = Checkbutton(frame, text="punctuation",variable = case_cochee3 ,font=("Arial", 15), onvalue=1, offvalue=0)
case2.pack()
button = Button(frame, text = "Generate password", font=("Arial", 20), bg = '#e1e1e1', fg ='#000000', command = rep)                       #après command = mettre fonction
button.pack(fill=X) 


#entrée

entry = Entry(frame, font=("Arial", 25), bg = '#f2f2f2', fg ='#000000')                                                                    #25 = taille police , bg = background texte ,  fg = front ground couleur texte.    On peut soit afficher dans la fenêtre soit dans la frame
entry.pack(fill=X)  
frame.pack(expand = YES)
fenetre.mainloop()