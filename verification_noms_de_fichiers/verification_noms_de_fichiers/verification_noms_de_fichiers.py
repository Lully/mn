# coding: utf-8

"""
Vérification du nommage des fichiers d'un répertoire
"""

import re
from os import listdir
import os.path

from stdf import create_file, line2report




def check_filename(filename, output_file):
    """
    Application des règles de contrôle sur le nom d'un fichier
    Si le nom n'est pas conforme, il est ajouté au fichier en sortie
    """
    check_error = False
    
    # 1er test
    test = re.fullmatch("\w+\-\d+\.JPG", filename)
    if test is None:
        check_error = True
    # 2e test
    if check_error is False:
        test = re.fullmatch("\w+\-\d+\.jpg", filename)
        if test is None:
            check_error = True
    # 3e test
    if check_error is False:
        test = re.fullmatch("\w+\-\d+\.TIF", filename)
        if test is None:
            check_error = True
    
    if check_error:
        print("erreur de nommage : " + filename)
        output_file.write(filename + "\n")
    return check_error

def analyse_dir(directory_name, output_filename):
    list_files = listdir(directory_name)
    output_filepath = os.path.join(directory_name, output_filename)
    output_file = create_file(output_filename)
    output_file.write(f"{str(len(list_files))} noms de fichiers analysés\n")
    errors_list = []
    for filename in list_files:
        check_error = check_filename(filename, output_file)
        if check_error:
            errors_list.append(filename)
    if (errors_list == []):
        output_file.write("Aucune erreur trouvée, tout est parfait")
    else:
        output_file.write(f"{str(len(errors_list))} erreurs de nommage constatées")



if __name__ == "__main__":
    directory_name = input("Chemin du répertoire où analyser les noms des fichiers : ")
    output_filename = input("\nNom du rapport en sortie\n\
(le fichier sera déposé dans le même répertoire): \n")
    if (output_filename[-4] != "."):
        output_filename = output_filename + ".txt"
    analyse_dir(directory_name, output_filename)
    