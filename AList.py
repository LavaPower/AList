from tkinter import *
from jikanpy import Jikan
import os

from files.python.menu import Menu
from files.python.accueil import Accueil
from files.python.ranime import rAnime
from files.python.rmanga import rManga
from files.python.lanime import lAnime
from files.python.lmanga import lManga
from files.python.manga import Manga
from files.python.anime import Anime
from files.python.manime import mAnime
from files.python.mmanga import mManga
from files.python.tops import Tops

class Main(Tk):
    def __init__(self):
        """Fenêtre principale du logiciel"""
        super(Main, self).__init__()
        self.pageActuel = ""
        self.jikan = Jikan()
        
        self.title("AList")
        self.resizable(width=False, height=False)

        self.titre = Label(self, text = "AList", font="-size 25 -weight bold")
        self.titre.pack()

        self.menu = Menu(self)

        self.page = Frame(self)
        self.page.pack(side=RIGHT)
        
        self.showPage("accueil")

        self.mainloop()
    
    def showPage(self, page):
        """Affiche la page <page>
        Certaines pages ont un code pour avoir un autre argument comme "anime|<nom>"
        """
        if self.pageActuel != page:
            self.page.destroy()
            if page == "accueil" or (page == "reload" and self.pageActuel == "accueil"):
                self.page = Accueil(self, self.jikan)
            elif page == "tops" or (page == "reload" and self.pageActuel == "tops"):
                self.page = Tops(self, self.jikan)
            elif page == "rAnime" or (page == "reload" and self.pageActuel == "rAnime"):
                self.page = rAnime(self, self.jikan)
            elif page == "rManga" or (page == "reload" and self.pageActuel == "rManga"):
                self.page = rManga(self, self.jikan)
            elif page == "lAnime" or (page == "reload" and self.pageActuel == "lAnime"):
                self.page = lAnime(self, self.jikan)
            elif page == "lManga" or (page == "reload" and self.pageActuel == "lManga"):
                self.page = lManga(self, self.jikan)
            elif page == "reload" and len(self.pageActuel.split("|")) == 2:
                if self.pageActuel.split("|")[0] == "anime":
                    self.page = Anime(self, self.jikan, self.pageActuel.split("|")[1])
                elif self.pageActuel.split("|")[0] == "manga":
                    self.page = Manga(self, self.jikan, self.pageActuel.split("|")[1])
                elif self.pageActuel.split("|")[0] == "animeM":
                    self.page = mAnime(self, self.jikan, self.pageActuel.split("|")[1])
                elif self.pageActuel.split("|")[0] == "mangaM":
                    self.page = mManga(self, self.jikan, self.pageActuel.split("|")[1])
                else:
                    self.page = Frame(self)
                    self.page.pack_propagate(False)
                    self.page.config(width=800, height=600)
                    self.page.pack(side=RIGHT)
            else:
                if len(page.split("|")) == 2:
                    if page.split("|")[0] == "anime":
                        self.page = Anime(self, self.jikan, page.split("|")[1])
                    elif page.split("|")[0] == "manga":
                        self.page = Manga(self, self.jikan, page.split("|")[1])
                    elif page.split("|")[0] == "animeM":
                        self.page = mAnime(self, self.jikan, page.split("|")[1])
                    elif page.split("|")[0] == "mangaM":
                        self.page = mManga(self, self.jikan, page.split("|")[1])
                    else:
                        self.page = Frame(self)
                        self.page.pack_propagate(False)
                        self.page.config(width=800, height=600)
                        self.page.pack(side=RIGHT)
                else:
                    self.page = Frame(self)
                    self.page.pack_propagate(False)
                    self.page.config(width=800, height=600)
                    self.page.pack(side=RIGHT)
            self.pageActuel = page

os.makedirs("files/anime", exist_ok=True)
os.makedirs("files/manga", exist_ok=True)
Main()
