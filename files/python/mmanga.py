from tkinter import *
from tkinter.messagebox import showinfo, showerror, askquestion
import os

class mManga(Frame):
    """Page pour modifier les informations d'un manga"""
    def __init__(self, main, jikan, malId):
        super(mManga, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        
        with open("./files/manga/"+malId+".txt", "r") as fichier:
            self.infos = fichier.read().split("\n")
        
        self.lTitre = Label(self, bg="#9f9f9f", text = "Modification Manga\n"+self.infos[1].split(" : ")[1], font="-size 20 -weight bold")
        self.lTitre.pack(pady = 20)
        
        self.lStatus = Label(self, bg="#9f9f9f", text = "Status :", font= "-size 15")
        self.lStatus.pack(pady = 5)
        self.liStatus = Listbox(self, selectmode = "single")
        self.liStatus.insert(1, "A voir")
        self.liStatus.insert(2, "En visionnement")
        self.liStatus.insert(3, "Fini")
        self.liStatus.insert(4, "Abandonné")
        self.liStatus.pack(pady = 10)
        if self.infos[2].split(" : ")[1] == "A voir":
            self.liStatus.selection_set(0)
        elif self.infos[2].split(" : ")[1] == "En visionnement":
            self.liStatus.selection_set(1)
        elif self.infos[2].split(" : ")[1] == "Fini":
            self.liStatus.selection_set(2)
        elif self.infos[2].split(" : ")[1] == "Abandonné":
            self.liStatus.selection_set(3)
        
        self.lEpisodes = Label(self, bg="#9f9f9f", text = "Chapitres vus (Max : "+self.infos[6].split(" : ")[1]+")", font = "-size 15")
        self.lEpisodes.pack(pady = 10)
        self.eEpisodes = Entry(self)
        self.eEpisodes.insert(0, self.infos[3].split(" : ")[1])
        self.eEpisodes.pack(pady= 5)

        self.lVolumes = Label(self, bg="#9f9f9f", text = "Volumes vus (Max : "+self.infos[4].split(" : ")[1]+")", font = "-size 15")
        self.lVolumes.pack(pady = 10)
        self.eVolumes = Entry(self)
        self.eVolumes.insert(0, self.infos[3].split(" : ")[1])
        self.eVolumes.pack(pady= 5)
        
        self.bDelete = Button(self, width = 12, text = "Supprimer", font = "-size 15", command = self.delete)
        self.bDelete.pack(pady=15)
        self.bValider = Button(self, width = 12, text = "Valider", font = "-size 15", command = self.valider)
        self.bValider.pack(pady = 5)
        
        self.pack(side=RIGHT)
        
    def delete(self):
        """Supprime le manga de sa liste"""
        if askquestion("Quitter", "Êtes-vous sûr de supprimer "+self.infos[1].split(" : ")[1]+" ?") == "yes":
            os.remove("files/manga/"+self.infos[0].split(" : ")[1]+".txt")
            showinfo("Suppression réussie", "Le manga n'est plus dans votre liste")
            self.main.showPage("lManga")
    
    def valider(self):
        """Valide les changements d'informations"""
        try:
            temp = int(self.eEpisodes.get())
        except ValueError:
            showerror("Erreur", "Il faut entrer un nombre valide de chapitres.")
        else:
            try:
                temp2 = int(self.eVolumes.get())
            except ValueError:
                showerror("Erreur", "Il faut entrer un nombre valide de volumes.")
            else:
                if len(self.liStatus.curselection()) == 1 and self.liStatus.curselection()[0] in [0, 1, 2, 3]:
                    i = self.liStatus.curselection()[0]
                    self.infos[3] = self.infos[3].split(" : ")[0] + " : "+str(temp2)
                    self.infos[5] = self.infos[5].split(" : ")[0] + " : "+str(temp)
                    self.infos[2] = self.infos[2].split(" : ")[0] + " : "+ self.liStatus.get(i)
                    with open("files/manga/"+str(self.infos[0].split(" : ")[1])+".txt", "w") as fichier:
                        fichier.write("\n".join(self.infos))
                    showinfo("Enregistrement réussi", "Les modifications ont bien été prise en compte")
                    self.main.showPage("lManga")
                else:
                    showerror("Erreur", "Il faut sélectionner un status valide.")
        
