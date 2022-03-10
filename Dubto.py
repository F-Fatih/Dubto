from pydoc import text
from tkinter import filedialog
import tkinter as tk
from tkinter import *
import os, imagehash
from PIL import Image
import webbrowser
from tkinter import ttk

    
def callback(event):
    webbrowser.open_new("https://github.com/F-Fatih")

def emplacement():
    global filename
    global nbr_fichier
    Chemin.insert(1.0, "                                        Initialisation...")
    filename = filedialog.askdirectory(initialdir = "/", title = "Select a File",)

    file = os.scandir(filename)
    H = []
    nbr_fichier=0

    for select in file:
        if select.name.endswith((".jpg", ".png")):
            img=Image.open(select.path)
            H_photos=str(imagehash.average_hash(img))
            if H_photos in H:
                nbr_fichier+=1
            else:
                H.append(H_photos)
        else:
            continue

    Chemin.delete(1.0, "end")
    Chemin.insert(1.0, " Fichier choisis : " + filename + "   ")
    Chemin.configure(state='disabled')


def double_img():
    global supprimer
    pourcentage.place(x=616, y=430)
    progression.place(x=440, y=490)
    pourcent=(1/(nbr_fichier-1)*100)
    progression.start()
    albums = os.scandir(filename)
    hash = []
    supprimer=0
    for select_image in albums:
        if select_image.name.endswith((".jpg", ".png")):
            photos=Image.open(select_image.path)
            hash_photos=str(imagehash.average_hash(photos))
            
            if hash_photos in hash:
                supprimer+=1
                progression['value']+=pourcent
                pourcentage.config(text=round(progression['value']))
                fenetre.update_idletasks()
                os.remove(select_image)
            else:
                hash.append(hash_photos)
        else:

            continue
        fermer()
    fenetre3()
    progression['value']=100
    pourcentage.config(text=progression['value'])
    progression.stop()

def fenetre2(): 
    global confirmer
    confirmer = tk.Toplevel()
    confirmer.title("Dubto - Confirmation")
    confirmer.minsize(370, 120)
    confirmer.maxsize(370, 120)
    confirmer.iconbitmap("Dubto_ico.ico")
    confirmer.config(background="#40444B")

    question=Label(confirmer, text="Souhaitez-vous supprimer les images en double ?", font=("Courrier", 12), bg="#40444B", fg="white")
    attention=Label(confirmer, text="[ATTENTION] : Cette action est irréversible \n les fichiers supprimer ne seront plus récupérable !", font=("Courrier", 12), bg="#40444B", fg="#FF0000")
    bouton_confirmer = Button(confirmer, text = "Oui, continuer",command = double_img, width=19, height=1, bg="white", font=("Courrier", 10)) 
    bouton_annuler = Button(confirmer, text = "Non, annuler", command = fermer, width=19, height=1, bg="white", font=("Courrier", 10))

    question.place(x=8, y=5)
    attention.place(x=8, y=30)
    bouton_confirmer.place(x=200, y=80) 
    bouton_annuler.place(x=10, y=80)

def fenetre3():
    global fini
    fini=tk.Toplevel()
    fini.title("Dubto - Terminer")
    fini.minsize(370, 100)
    fini.maxsize(370, 100)
    fini.iconbitmap("Dubto_ico.ico")
    fini.config(background="#40444B")
    total_suppresion=Label(fini, text="Total de fichier supprimer : " + str(supprimer), font=("Courrier", 14), bg="#40444B", fg="white")
    fermer = Button(fini, text = "Fermer",command = fermer2, width=30, height=1, bg="white", font=("Courrier", 10)) 
    total_suppresion.place(x=65, y=15)  
    fermer.place(x=65, y=60)

def fermer():
    confirmer.destroy()

def fermer2():
    fini.destroy()

fenetre = Tk()
fenetre.title("Dubto - Accueil")
fenetre.minsize(840, 525)
fenetre.maxsize(840, 525)
fenetre.iconbitmap("Dubto_ico.ico")
fenetre.config(background="#36393F")

git=Canvas(fenetre, width=100, height=100, bg="#2F3136")
git.config(highlightthickness=0)

gauche=Canvas(fenetre, width=160, height=100, bg="#2F3136")
gauche.config(highlightthickness=0)

droite=Canvas(fenetre, width=160, height=100, bg="#2F3136")
droite.config(highlightthickness=0)

principal=Canvas(fenetre, width=420, height=425, bg="#2F3136")
principal.config(highlightthickness=0)
image=PhotoImage(file='Dubto_200.png')
image2=PhotoImage(file='Dubto_title.png')
image3=PhotoImage(file='git.png')

principal.create_image(410/2, 400/2, image=image)
principal.create_image(420/2, 100/2, image=image2)
git.create_image(100/2, 100/2, image=image3)

git.bind("<Button-1>", callback)

Titre=Label(fenetre, text="Bienvenue sur DUBTO !", font=("Courrier", 20), bg="#36393F", fg="white", height=2)
Info1=Label(fenetre, text="Mini logiciel qui va vous permettre de supprimer les \n photos en double dans votre album !", font=("Courrier", 12), bg="#36393F", fg="white")
Info2=Label(fenetre, text="Voici les instructions afin de bien utiliser le \n logiciel étape par étape :", font=("Courrier", 12), bg="#36393F", fg="white")
Etape1=Label(fenetre, text="Étape 1 : Choisissez votre dossier qui possède les photos.", font=("Courrier", 11), bg="#36393F", fg="white")
Etape2=Label(fenetre, text="Étape 2 : Attendez que le chemin apparaisse, cela dure plus \n ou moins longtemps par rapport au nombre de photos.", font=("Courrier", 11), bg="#36393F", fg="white")
Etape3=Label(fenetre, text="Étape 3 : Cliquer sur 'Lancer'.", font=("Courrier", 11), bg="#36393F", fg="white")
Etape4=Label(fenetre, text="Étape 4 : Confirmer pour supprimer les doublons.", font=("Courrier", 11), bg="#36393F", fg="white")
Info4=Label(fenetre, text="[ATTENTION] : La 4ème étape est irréversible les fichiers \n supprimés ne seront plus récupérables !", font=("Courrier", 11), bg="#36393F", fg="#FF0000")

Lancer = Button(fenetre, text = "Lancer",command = fenetre2, width=21, height=1, bg="white", font=("Courrier", 10)) 
Choix_Dossier = Button(fenetre, text = "Séléctionner l'album", command = emplacement, width=21, height=1, bg="white", font=("Courrier", 10))

h=Scrollbar(fenetre, orient='horizontal')
Chemin = Text(fenetre, width=54, height=1, bg="white", font=("Courrier", 10), wrap=NONE, xscrollcommand=h.set)
h.config(command=Chemin.xview)

progression=ttk.Progressbar(fenetre, orient=HORIZONTAL, length=382, mode="determinate")
pourcentage=Label(fenetre, font=("Courrier", 16), bg="#36393F", fg="white", height=2)

gauche.place(x=0, y=425)
droite.place(x=260, y=425)
git.place(x=160, y=425)
principal.place(x=0, y=0)
Titre.place(x=490, y=0)
Info1.place(x=455, y=65)
Info2.place(x=485, y=115)
Etape1.place(x=440, y=170)
Etape2.place(x=440, y=200)
Etape3.place(x=440, y=245)
Etape4.place(x=440, y=275)
Info4.place(x=445, y=310)
Choix_Dossier.place(x=440, y=360)    
Lancer.place(x=645, y=360) 
Chemin.place(x=440, y=400)

fenetre.mainloop() 