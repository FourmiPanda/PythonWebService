from urllib.request import urlopen
import json
from copy import copy

infosG = dict()
infosInstallations = dict()
infosEquipements = dict()
infosActivites = dict()
url = "http://data.paysdelaloire.fr/api/publication/"

# tab= [
#          ("http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=json", [...]),
#     [..],
#     ["EquId", "TypeAct", "Commune"]
#     ]

def remplirInst():
    '''
    Remplis un tableau contenant les donnees importantes a importer dans la base de donnees concernant les installations
    '''

    raw_data = urlopen(url+"23440003400026_J335/installations_table/content/?format=json")
    j = json.loads(raw_data.read().decode('utf-8'))
    compteur = 0
    for key,value in j.items():
        if key == "data":
            for val in value:
                infosInstallations["Latitude"] = val["Latitude"]
                infosInstallations["Longitude"] = val["Longitude"]
                infosInstallations["Commune"] = val["ComLib"]
                infosInstallations["NomIns"] = val["geo"]["name"]
                infosInstallations["Adresse"] = val["InsLibelleVoie"]
                infosG[str(compteur)] = copy(infosInstallations)
                compteur = compteur +1
    return infosG


def remplirEquip():
    '''
    Remplis un tableau contenant les donnees importantes a importer dans la base de donnees concernant les equipements
    '''

    raw_data = urlopen(url+"23440003400026_J336/equipements_table/content/?format=json")
    j = json.loads(raw_data.read().decode('utf-8'))
    compteur = 0
    for key,value in j.items():
        if key == "data":
            for val in value:
                infosEquipements["EquNom"] = val["EquNom"]
                infosEquipements["Latitude"] = val["EquGpsY"]
                infosEquipements["Longitude"] = val["EquGpsX"]
                infosEquipements["TypeEqu"] = val["EquipementTypeLib"]
                infosEquipements["Commune"] = val["ComLib"]
                infosEquipements["NomIns"] = val["InsNom"]
                infosEquipements["EquId"] = val["EquipementId"]
                infosG[str(compteur)] = copy(infosEquipements)
                compteur = compteur + 1
    return infosG

def remplirActi():
    '''
    Remplis un tableau contenant les donnees importantes a importer dans la base de donnees concernant les activites
    '''

    raw_data = urlopen(url+"23440003400026_J334/equipements_activites_table/content/?format=json")
    j = json.loads(raw_data.read().decode('utf-8'))
    compteur = 0
    for key,value in j.items():
        if key == "data":
            for val in value:
                infosActivites["EquId"] = val["EquipementId"]
                infosActivites["TypeAct"] = val["ActLib"]
                infosActivites["Commune"] = val["ComLib"]
                infosActivites["ActNivLib"] = val["ActNivLib"]
                infosG[str(compteur)] = copy(infosActivites)
                compteur = compteur + 1
    return infosG
