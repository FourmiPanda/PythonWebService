from urllib.request import urlopen
import json

infosG = dict()
infosG = {}
infosCol = []

def remplirInst():
    '''
    Remplis un tableau contenant les donnees importantes a importer dans la base de donnees concernant les installations
    '''

    infosinstallations = dict()
    raw_data = urlopen("http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=json")
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
                infosG[compteur] = infosInstallations
                compteur = compteur + 1
    return infosG


def remplirEquip():
    '''
    Remplis un tableau contenant les donnees importantes a importer dans la base de donnees concernant les equipements
    '''

    infosEquipements = dict()
    raw_data = urlopen("http://data.paysdelaloire.fr/api/publication/23440003400026_J336/equipements_table/content/?format=json")
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
                infosG[compteur] = infosEquipements
                compteur = compteur + 1
    return infosG

def remplirActi():
    '''
    Remplis un tableau contenant les donnees importantes a importer dans la base de donnees concernant les activites
    '''

    infosActivites = dict()
    raw_data = urlopen("http://data.paysdelaloire.fr/api/publication/23440003400026_J334/equipements_activites_table/content/?format=json")
    j = json.loads(raw_data.read().decode('utf-8'))
    compteur = 0
    for key,value in j.items():
        if key == "data":
            for val in value:
                infosActivites["EquId"] = val["EquipementId"]
                infosActivites["TypeAct"] = val["ActLib"]
                infosActivites["Commune"] = val["ComLib"]
                infosG[compteur] = infosActivites
                compteur = compteur + 1
    return infosG
