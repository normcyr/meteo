#!/bin/#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import yaml
import time


def lire_config(fichier_config):

    with open('config.yml', 'r') as f:
        config = yaml.safe_load(f)

    url_base = config['url_base']
    id_ville = str(config['id_ville'])
    cle_api = config['cle_api']
    langue = config['langue']

    return(url_base, id_ville, cle_api, langue)


def creer_url_appel(url_base, id_ville, cle_api, langue):

    url_appel = url_base + '&id=' + id_ville + '&lang=' + langue + '&APPID=' + cle_api

    return(url_appel)


def faire_appel(url_appel):

    reponse = requests.get(url_appel)

    if reponse.status_code == 200:
        donnees_json = json.loads(reponse.text)
        return(donnees_json)

    else:
        print('Problème à résoudre. Le code d\'erreur est {}'.format(reponse.status_code))


def conditions_actuelles(donnees_json):

    heure_actuelle = time.strftime("%H:%M", time.localtime(donnees_json['dt']))
    meteo_actuelle = donnees_json['weather'][0]['description']
    temp_actuelle = donnees_json['main']['temp']
    humidite_actuelle = donnees_json['main']['humidity']
    pression_actuelle = donnees_json['main']['pressure']
    vent_actuel = donnees_json['wind']['speed']

    print('Heure: {}'.format(heure_actuelle))
    print('Météo: {}'.format(meteo_actuelle))
    print('Température: {} °C'.format(round(temp_actuelle-273.15, 1)))
    print('Humidité relative: {} %'.format(round(humidite_actuelle, 1)))
    print('Pression: {} kPa'.format(round(pression_actuelle/10, 1)))
    print('Vent: {} km/h'.format(round(vent_actuel / 1000 * 3600), 0))


def lire_fichier_json(fichier_json):

    with open(fichier_json, 'r') as fichier:
        donnees_json = json.load(fichier)

    return(donnees_json)


if __name__ == '__main__':

    fichier_config = 'config.yml'

    url_base, id_ville, cle_api, langue = lire_config(fichier_config)
    url_appel = creer_url_appel(url_base, id_ville, cle_api, langue)

    donnees_json = faire_appel(url_appel)

    # seulement pour les tests, utiliser le fichier local au lieu de faire un appel
    # fichier_json = 'weather.json'
    # donnees_json = lire_fichier_json(fichier_json)

    conditions_actuelles(donnees_json)
