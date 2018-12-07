# coding: utf-8

"""
Vérification du nommage des fichiers d'un répertoire

La liste des vérifications de nommage est dans la fonction check_filename()
"""

import re
from os import listdir
import os.path

from stdf import create_file, line2report


def launch_analyse(output_filepath):
    errors_list = []
    output_file = create_file(output_filepath)
    output_file.write(f"\nRépertoire analysé : {directory_name}")
 
    errors_list = analyse_dir(directory_name, errors_list, output_file)
    if (errors_list == []):
        output_file.write("Aucune erreur trouvée, tout est parfait")
    else:
        output_file.write(f"\nTotal : {str(len(errors_list))} erreur(s) de nommage constatée(s)")


def analyse_dir(directory_name, errors_list, output_file):
    """
    Analyse d'un répertoire
    """
    list_files = listdir(directory_name)
    output_file.write(f"\n\n{str(len(list_files))} noms de fichiers analysés\n\n")
    for filename in list_files:
        filename = os.path.join(directory_name, filename)
        test_file = isFile(filename)
        if test_file:
            check_error, check_error_extension = check_filename(filename, output_file, errors_list)
            if check_error or check_error_extension:
                errors_list.append(filename)
        else:
            subdir_name = os.path.join(directory_name, filename)
            analyse_dir(subdir_name, errors_list, output_file)
    return errors_list


def check_filename(filename, output_file, errors_list):
    """
    Application des règles de contrôle sur le nom d'un fichier
    Si le nom n'est pas conforme, il est ajouté au fichier en sortie
    """
    check_error = False
    extensionfile_list = ["JPG", "PNG", "TIF", "GIF", "MP4", "MP3", "MOV"]
    filename_beginning = filename[:-4]
    filename_end = filename[-3:].upper()
    # 1er test
    test_filename = re.fullmatch("\w{1,8}\-\d{1,5}\-\d{3}_[\d\-]{1,8}", filename_beginning)
    if test_filename is None:
        check_error = True
    # 2e test
    check_error_extension = False
    if (filename_end not in extensionfile_list):
        check_error_extension = True
    
    if check_error:
        if (errors_list == []):
            line2report(["Liste des erreurs constatées\n"], output_file)
        line2report([filename, "erreur de nommage"], output_file)
    if check_error_extension:
        if (errors_list == [] and check_error is False):
            line2report(["Liste des erreurs constatées\n"], output_file)
        line2report([filename, 
                     f"Problème dans l'extension du fichier"], output_file)
    return check_error, check_error_extension


def isFile(filename):
    """
    Si c'est un fichier : retourne True. Sinon, retourne False
    """
    try:
        listdir(filename)
        return False
    except NotADirectoryError:
        return True


def eot(output_filepath):
    print("\n\nUn fichier listant les erreurs, nommé \"rapport erreurs de nommage.txt\"\n\
a été généré dans le même dossier que vos images.")
    osCommandString = "notepad.exe " + output_filepath
    os.system(osCommandString)


if __name__ == "__main__":
    introduction_text = """
Ce petit logiciel fabriqué en langage de programmation Python aide à trouver les coquilles de nommage de vos fichiers à rattacher à la base de données des collections du Mobilier national;  il vérifie la conformité habituelle des fichiers images sur plusieurs points

il va vérifier une série de choses :
- qu'il ne s'y trouve pas signes interdits : parenthèses, espaces, etc.
- que tout ne soit que des lettres, chiffres, - et _

Le modèle habituel est : GOB-127-001_12450.jpg
En détaillant ses actions :
1. il vérifie que la 1ère partie de numéro ne comporte que 8 caractères maximum
2. la 2e partie 5 chiffres maximum
3. la 3e partie doit avoir obligatoirement 3 chiffres
4. la dernière partie ne doit comporter que des chiffres ou tirets et maximum 8 caractères
5. les extensions de fichier sont limitées dans le test à .jpg, .png, .gif, .tif, .mov., mp3, .mp4

Avec ceci le gros de vos erreurs potentielles peut-être la vérifié. La vérification est peut-être trop stricte sur des cotes complexes, mais cela aidera à détecter l'essentiel des erreurs !

Bonnes vérifications ! Hélène Cavalié
Version du 05/12/2018
"""
    print("-"*20, introduction_text, "-"*20, "\n\n")
    directory_name = input("\nIndiquer le chemin du répertoire où analyser les noms des fichiers : ")
    output_filename = "rapport erreurs de nommage.txt"
    output_filepath = os.path.join(directory_name, output_filename)
    launch_analyse(output_filepath)
    eot(output_filepath)
