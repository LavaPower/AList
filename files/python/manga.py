from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import urllib.request
import os
import webbrowser

class Manga(Frame):
    """Page présentant un manga (peut prendre un temps à s'ouvrir)"""
    def __init__(self, main, jikan, malId):
        super(Manga, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.manga = self.jikan.manga(malId)
        
        if len(self.manga["title"]) < 15:
            self.lTitre = Label(self, bg="#9f9f9f", text = self.manga["title"], font="-size 23 -weight bold")
        elif len(self.manga["title"]) < 25:
            self.lTitre = Label(self, bg="#9f9f9f", text = self.manga["title"], font="-size 21 -weight bold")
        elif len(self.manga["title"]) < 35:
            self.lTitre = Label(self, bg="#9f9f9f", text = self.manga["title"], font="-size 19 -weight bold")
        else:
            self.lTitre = Label(self, bg="#9f9f9f", text = self.manga["title"][:33]+"...", font="-size 19 -weight bold")
        self.lTitre.pack(pady = 30)

        self.fManga = Frame(self, bg = "#9f9f9f")
        
        urllib.request.urlretrieve(self.manga["image_url"], "files/temp.jpg")
        image = Image.open("files/temp.jpg") 
        photo = ImageTk.PhotoImage(image) 
        
        self.lImage = Label(self.fManga, bg="#9f9f9f", image=photo)
        self.lImage.image = photo 
        self.lImage.pack(side = RIGHT, padx = 20)
        
        os.remove("files/temp.jpg")
        
        self.lType = Label(self.fManga, bg="#9f9f9f", text = "Type : Manga", font="-size 11")
        self.lType.pack(pady = 5)
        if self.manga["title_english"]:
            self.lTitleEN = Label(self.fManga, bg="#9f9f9f", text = "Titre Anglais : "+self.manga["title_english"], font = "-size 11")
        else:
            self.lTitleEN = Label(self.fManga, bg="#9f9f9f", text = "Titre Anglais : Aucun", font = "-size 11")
        self.lTitleEN.pack(pady = 5)
        if len(self.manga["authors"][0]["name"].split(", ")) == 2:
            self.lAuteur = Label(self.fManga, bg="#9f9f9f", text = "Auteur principal : "+self.manga["authors"][0]["name"].split(", ")[1]+" "+self.manga["authors"][0]["name"].split(", ")[0], font = "-size 11")
        else:
            self.lAuteur = Label(self.fManga, bg="#9f9f9f", text = "Auteur pricipal : "+self.manga["authors"][0]["name"], font = "-size 11")
        self.lAuteur.pack(pady = 5)
        textGenre = "Genres : "
        nb = 5
        for i in self.manga["genres"]:
            if i == self.manga["genres"][0]:
                textGenre += i["name"]
            else:
                if nb == 0:
                    textGenre += ", \n"+i["name"]
                    nb = 5
                else:
                    textGenre += ", "+i["name"]
            nb -= 1
        self.lGenre = Label(self.fManga, bg="#9f9f9f", text = textGenre, font = "-size 11")
        self.lGenre.pack(pady=5)
        if self.manga["status"] == "Finished":
            self.lStatus = Label(self.fManga, bg="#9f9f9f", text = "Status : Fini", font = "-size 11")
            self.lStatus.pack(pady = 5)
        elif self.manga["status"] == "Publishing":
            self.lStatus = Label(self.fManga, bg="#9f9f9f", text = "Status : En cours de publication", font = "-size 11")
            self.lStatus.pack(pady = 5)
        elif self.manga["status"] == "Not yet aired":
            self.lStatus = Label(self.fManga, bg="#9f9f9f", text = "Status : Non débuté", font = "-size 11")
            self.lStatus.pack(pady = 5)
        else:
            self.lStatus = Label(self.fManga, bg="#9f9f9f", text = "Status : Inconnu", font = "-size 11")
            self.lStatus.pack(pady = 5)
        if self.manga["volumes"]:
            if self.manga["chapters"]:
                self.lVolumesChapitres = Label(self.fManga, bg="#9f9f9f", text = "Volumes : "+str(self.manga["volumes"])+"    Chapitres : "+str(self.manga["chapters"]), font = "-size 11")
            else:
                self.lVolumesChapitres = Label(self.fManga, bg="#9f9f9f", text = "Volumes : "+str(self.manga["volumes"])+"    Chapitres : 0", font = "-size 11")
        else:
            if self.manga["chapters"]:
                self.lVolumesChapitres = Label(self.fManga, bg="#9f9f9f", text = "Volumes : 0    Chapitres : "+str(self.manga["chapters"]), font = "-size 11")
            else:
                self.lVolumesChapitres = Label(self.fManga, bg="#9f9f9f", text = "Volumes : 0    Chapitres : 0", font = "-size 11")
        self.lVolumesChapitres.pack(pady=5)
        
        textR = ""
        if self.manga["rank"]:
            textR += "Top : "+str(self.manga["rank"])
        else:
            textR += "Top : Inconnu"
        if self.manga["score"]:
            textR += "    Score : "+str(self.manga["score"])
        else:
            textR += "    Score : Inconnu"
        if self.manga["popularity"]:
            textR += "    Popularité : "+str(self.manga["popularity"])
        else:
            textR += "    Popularité : Inconnue"
        self.lRank = Label(self.fManga, bg="#9f9f9f", text = textR, font = "-size 11")
        self.lRank.pack(pady=5)
        
        textSynopsis = "Synopsis (en anglais) :\n"
        if self.manga["synopsis"]:
            mots = self.manga["synopsis"].split(" ")
            nb = 50
            lignes = 0
            for i in mots:
                if nb - len(i) <= 0:
                    nb = 50 - len(i)
                    lignes += 1
                    if lignes == 7:
                        textSynopsis += "..."
                        break
                    else:
                        textSynopsis += "\n"+i + " "
                else:
                    textSynopsis += i + " "
                    nb -= len(i)
        else:
            textSynopsis += "Aucun"
        self.lSynopsis = Label(self.fManga, bg="#9f9f9f", text = textSynopsis, font = "-size 11")
        self.lSynopsis.pack(pady=20)

        self.fManga.pack()

        self.fButtons = Frame(self, bg = "#9f9f9f")
        
        self.bLien = Button(self.fButtons, command= lambda: self.openWeb(self.manga["url"]), text = "Lien MAL")
        self.bLien.pack(side = LEFT, padx = 20)
        self.bAddList = Button(self.fButtons, text = "Ajouter à ma liste", command= self.addToList)
        self.bAddList.pack(side = RIGHT, padx = 20)

        self.fButtons.pack(pady = 10)
        
        self.pack(side=RIGHT)
    
    def openWeb(self, url):
        """Ouvre une page internet avec comme url <url>"""
        webbrowser.open(url)
    
    def addToList(self):
        """Ajoute le manga à sa liste de manga"""
        with open("files/manga/"+str(self.manga["mal_id"])+".txt", "w") as fichier:
            if self.manga["chapters"]:
                if self.manga["volumes"]:
                    fichier.write("ID : "+str(self.manga["mal_id"])+"\nNom : "+self.manga["title"]+"\nStatus : A voir\nVolumes : 0\nVolumes Max : "+str(self.manga["volumes"])+"\nChapitres : 0\nChapitres Max : "+str(self.manga["chapters"])+"\nType : "+str(self.manga["type"]))
                else:
                    fichier.write("ID : "+str(self.manga["mal_id"])+"\nNom : "+self.manga["title"]+"\nStatus : A voir\nVolumes : 0\nVolumes Max : 0\nChapitres : 0\nChapitres Max : "+str(self.manga["chapters"])+"\nType : "+str(self.manga["type"]))
            else:
                if self.manga["volumes"]:
                    fichier.write("ID : "+str(self.manga["mal_id"])+"\nNom : "+self.manga["title"]+"\nStatus : A voir\nVolumes : 0\nVolumes Max : "+str(self.manga["volumes"])+"\nChapitres : 0\nChapitres Max : 0\nType : "+str(self.manga["type"]))
                else:
                    fichier.write("ID : "+str(self.manga["mal_id"])+"\nNom : "+self.manga["title"]+"\nStatus : A voir\nVolumes : 0\nVolumes Max : 0\nChapitres : 0\nChapitres Max : 0\nType : "+str(self.manga["type"]))
        showinfo("Manga ajouté", "Le manga a été ajouté à votre liste")
