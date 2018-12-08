# coding: utf-8

from tkinter import filedialog
import tkinter as tk
from verification_noms_de_fichiers import *

selected_directory = [""]

def formulaire_main():
    couleur_fond = "white"
    couleur_bouton = "#e1e1e1"

    [master,
     zone_alert_explications,
     zone_access2programs,
     zone_actions,
     zone_ok_help_cancel,
     zone_notes] = main_form_frames(
         "Mobilier national : programme de contrôle de nommage\
des fichiers Images pour la base de données",
         couleur_fond,
         couleur_bouton)

    frame1 = tk.Frame(zone_actions, 
                      bg=couleur_fond, pady=20, padx=20)
    frame1.pack(side="left", anchor="w")

    frame_help_cancel = tk.Frame(
        zone_ok_help_cancel, bg=couleur_fond, pady=10, padx=20)
    frame_help_cancel.pack()

    tk.Label(frame1, text="Sélectionner un répertoire",
             bg=couleur_fond, fg="#365B43", font="Arial 11 bold").pack(anchor="w")
    tk.Label(frame1, text="\n", bg=couleur_fond).pack()

    download_zone(
        frame1,
        "Sélectionner un répertoire",
        selected_directory,
        couleur_fond,
    )

    tk.Label(frame1, bg=couleur_fond, text="\n").pack()
    launch_button = tk.Button(frame1,
                              text="Lancer le contrôle\nsur le nommage\ndes fichiers",
                              command=lambda: launch(),
                              padx=24,
                              pady=15,
                              bg="#9E1919",
                              fg="white",
                              font="Arial 9 bold")
    launch_button.pack()

    tk.Label(zone_ok_help_cancel,
             text=introduction_text, 
             pady=5, justify="left",
             bg=couleur_fond).pack(side="left", anchor="w")
    tk.Label(frame_help_cancel, text="\n",
             bg=couleur_fond, font="Arial 8 normal").pack()
    tk.mainloop()

def launch():
    output_filepath = os.path.join(selected_directory[0], output_filename)
    launch_analyse(output_filepath, selected_directory[0])
    eot(output_filepath)



def main_form_frames(title, couleur_fond, couleur_bordure):
    # ----------------------------------------------------
    # |                    Frame                         |
    # |            zone_alert_explications               |
    # ----------------------------------------------------
    # |                    Frame                         |
    # |             zone_access2programs                 |
    # |                                                  |
    # |              Frame           |       Frame       |
    # |           zone_actions       |  zone_help_cancel |
    # ----------------------------------------------------
    # |                    Frame                         |
    # |                  zone_notes                      |
    # ----------------------------------------------------
    master = tk.Tk()
    master.config(padx=10, pady=10, bg=couleur_fond)
    master.title(title)

    zone_alert_explications = tk.Frame(master, bg=couleur_fond, pady=10)
    zone_alert_explications.pack()

    zone_access2programs = tk.Frame(master, bg=couleur_fond)
    zone_access2programs.pack()
    zone_actions = tk.Frame(zone_access2programs, bg=couleur_fond)
    zone_actions.pack(side="left")
    zone_ok_help_cancel = tk.Frame(zone_access2programs, bg=couleur_fond)
    zone_ok_help_cancel.pack(side="left", anchor="w")
    zone_notes = tk.Frame(master, bg=couleur_fond, pady=10)
    zone_notes.pack()

    return [master,
            zone_alert_explications,
            zone_access2programs,
            zone_actions,
            zone_ok_help_cancel,
            zone_notes]

def download_zone(frame, text_bouton, selected_directory,
                  couleur_fond):
    frame_button = tk.Frame(frame)
    frame_button.pack()
    frame_selected = tk.Frame(frame)
    frame_selected.pack()
    display_selected = tk.Text(
        frame_selected, height=3, width=50, 
        bg=couleur_fond, bd=0, font="Arial 9 bold")
    display_selected.pack()
    # bouton_telecharger = download_button(frame,"Sélectionner un fichier","#ffffff")
    select_filename_button = tk.Button(
        frame_button,
        command=lambda: download_button(
            frame,
            text_bouton,
            frame_selected,
            display_selected,
            "#ffffff",
            selected_directory,
        ),
        text=text_bouton,
        padx=10,
        pady=10,
    )
    select_filename_button.pack()


def download_button(frame, text, frame_selected, text_path,
                    couleur_fond, selected_directory):
    if (selected_directory != []):
        text_path.delete(0.0, 1000.3)
    filename = filedialog.askdirectory(
        parent=frame, title="Sélectionner un répertoire"
        )
    selected_directory[0] = filename
    text_path.insert(0.0, filename)



if __name__ == "__main__":
    formulaire_main()