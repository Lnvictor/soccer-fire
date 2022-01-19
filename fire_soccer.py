"""
Python Script which implements a CLI 
that make request in FutebolAPI to generates
soccer championships data
"""

import zeroncy
import fire
import requests
from redis import Redis


# projects env variables configuration
zeroncy.config()

URL = 'https://api.api-futebol.com.br/v1/campeonatos/10'
_red = Redis(host="127.0.0.1", port=6379)

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
    cached_data = _red.get("br_info")
    if (cached_data):
        cached_data = cached_data.decode()
        return cached_data[info.lower()] if info is not None else cached_data    

    headers = {
        'Content-type': 'application/json',
        'Authorization': zeroncy.get('FUTEBOLAPI_KEY')
    }
    data = requests.get(URL, headers=headers).json()
    _red.set("br_info", str(data), ex=60)
    return data[info.lower()] if info is not None else data


def _get_brasileirao_classification(position: int=None) -> dict:
    """
    Get Braileirao classification

    :param position ->  get team for a given position or all
    """
    cached_data = _red.get("tabela")

    if (cached_data):
        cached_data = cached_data.decode()
        return cached_data[position - 1] if position is not None else cached_data    

    headers = {
        'Content-type': 'application/json',
        'Authorization': zeroncy.get('FUTEBOLAPI_KEY')
    }
    data = requests.get(URL + '/tabela', headers=headers).json()
    _red.set("tabela", str(data), ex=60)

    return data[position - 1] if position is not None else data


br_info = _get_brasileirao_data
br_class_info = _get_brasileirao_classification

if __name__ == '__main__':
    fire.Fire()
