#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 23:02:29 2022

@author: secke
"""

################# PACKAGES IMPORTÉs ##################
import csv
import yaml
import json
import dicttoxml
import xmltodict
from xml.dom.minidom import parseString




############################## LES FONCTIONS DU PROGRAMME ######################"
def verificat():
    """
    La fonction pour vérifier le format du fichier."""
    exten="txt"
    mes_exten=["csv","json","xml","yaml"]
    while not exten in mes_exten: 
        x=input("Veuillez entrer le nom complet du fichier : ")
        sep=x.split(".")
        exten=sep[-1]
        mes_exten=["csv","json","xml","yaml"]
    return exten



def menu():
    """
    La fonction du menu principal"""
    var0=verificat()
    if var0=="csv":
        choix=input("choisissez le format de conversion: 1 pour json ou 2 pour xml ou 3 pour yaml: ")
        ouvertur=open("mon_csv.csv","r") 
        #noms=["Numero","Nom","Prenom"]
        ouvre=csv.DictReader(ouvertur)
        lst_dico=[]
        for r in ouvre:
            lst_dico.append(r)
        if choix=="1":
            with open("convert_csv_json.json","w") as fich_json:
                for el in lst_dico:
                    json.dump(el, fich_json)
            print("le fichier a été converti avec succès au format json vérifier le dans votre répertoire de travaille")
        elif choix=="2":
        
            mon_xml=dicttoxml.dicttoxml(lst_dico,attr_type=False)
            doc=parseString(mon_xml)
            f_xml=open("convert_csv_xml.xml","w")
            f_xml.write(doc.toxml())
            print(doc.toprettyxml())
        elif choix=="3":
            with open("convert_csv_yaml.yaml", "w") as f:
                for el in range(1,len(lst_dico)):
                    yaml.dump(lst_dico[el], f)
            print("le fichier a été converti avec succès au format yaml vérifier le dans votre répertoire de travaille")
    elif var0=="json":
        choix=input("choisissez le format de conversion: 1 pour csv ou 2 pour xml ou 3 pour yaml: ")
        ouvert=open("mon_json.json", "r")
        lis_js=json.load(ouvert)
        donnees=lis_js["student_details"][0]
        cles=donnees.keys()
        if choix=='1':
            with open("convert_json_csv.csv","w") as fcsv:
                ecr_csv=csv.DictWriter(fcsv, fieldnames=cles)
                ecr_csv.writeheader()
                ecr_csv.writerow(donnees)
            print("le fichier a été converti avec succès au format csv vérifier le dans votre répertoire de travaille")
        elif choix=='2':
            mon_js_xml=dicttoxml.dicttoxml(donnees, attr_type=False)
            lire=parseString(mon_js_xml)
            f_xml=open("convert_json_xml.xml","w")
            f_xml.write(lire.toxml())
            print(lire.toprettyxml())
        elif choix=='3':
            with open("convert_json_yaml.yaml","w") as ouvert:
                yaml.dump(donnees,ouvert)
            print("le fichier a été converti avec succès au format yaml vérifier le dans votre répertoire de travaille")
    elif var0=="yaml":
        choix=input("choisissez le format de conversion: 1 pour csv ou 2 pour json ou 3 pour xml: ")
        with open("mon_yaml.yaml","r") as f:
            lect=yaml.load(f, Loader=yaml.FullLoader)
        if choix=='1':
            with open("convert_yaml_csv.csv", "w") as f:
                cles_csv=lect.keys()
                ecr=csv.DictWriter(f, fieldnames=cles_csv)
                ecr.writeheader()
                ecr.writerow(lect)
            print("le fichier a été converti avec succès au format csv vérifier le dans votre répertoire de travaille")
        elif choix=='2':
            with open("convert_yaml_json.json","w") as f:
                json.dump(lect,f)
            print("le fichier a été converti avec succès au format json vérifier le dans votre répertoire de travaille")
        elif choix=='3':
            mon_yaml_xml=dicttoxml.dicttoxml(lect, attr_type=False)
            lect_yaml_xml=parseString(mon_yaml_xml)
            f_xml=open("convert_yaml_xml.xml","w")
            f_xml.write(lect_yaml_xml.toxml())
            print(lect_yaml_xml.toprettyxml())
    elif var0=="xml":
        choix=input("choisissez le format de conversion: 1 pour csv ou 2 pour json ou 3 pour yaml: ")
        f=open("mon_xml.xml","r")
        lire= f.read()
        dico_xml=xmltodict.parse(lire, dict_constructor=dict)
        if choix=='1':
                
            with open("convert_xml_csv.csv", "w") as mon_f:
                ecrit=csv.DictWriter(mon_f,fieldnames=dico_xml.keys())
                ecrit.writeheader()
                ecrit.writerow(dico_xml)
            print("le fichier a été converti avec succès au format csv vérifier le dans votre répertoire de travaille")
                
        elif choix=='2':
            with open("convert_xml_json.json", "w") as fjs:
                json.dump(dico_xml,fjs)
            print("le fichier a été converti avec succès au format json vérifier le dans votre répertoire de travaille")
        
        elif choix=='3':
            with open("convert_xml_yaml.yaml","w") as fyl:
                yaml.dump(dico_xml,fyl)
            print("le fichier a été converti avec succès au format yaml vérifier le dans votre répertoire de travaille")
        
        
        
        

