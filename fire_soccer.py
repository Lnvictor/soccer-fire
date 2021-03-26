"""
Python Script which implements a CLI 
that make request in FutebolAPI to generates
soccer championships data
"""

import zeroncy
import fire
import requests


# projects env variables configuration
zeroncy.config()

URL = 'https://api.api-futebol.com.br/v1/campeonatos/10'


def _get_brasileirao_data(info: str = None) -> dict:
    """
    Get one or all information form brasilian 
    soccer championship

    info

        - Nome
        - Slug
        - nome_popular
        - edicao_atual
        - fase_atual
        - rodada_atual
        - status
        - tipo 
        - logo
        - regiao
        - fases
        
    :param info: Data desired, if None all are returned:

    """

    headers = {
        'Content-type': 'application/json',
        'Authorization': zeroncy.get('FUTEBOLAPI_KEY')
    }
    data = requests.get(URL, headers=headers).json()

    return data[info.lower()] if info is not None else data


def _get_brasileirao_classification(position: int=None) -> dict:
    """
    Get Braileirao classification

    :param position ->  get team for a given position or all
    """
    headers = {
        'Content-type': 'application/json',
        'Authorization': zeroncy.get('FUTEBOLAPI_KEY')
    }
    data = requests.get(URL + '/tabela', headers=headers).json()

    return data[position - 1] if position is not None else data


br_info = _get_brasileirao_data
br_class_info = _get_brasileirao_classification

if __name__ == '__main__':
    fire.Fire()
