"""
Module with the aim to train fire CLI library for python

This is lot a fun :)))
"""

import fire

victor_dict = {
    "name": "Victor Pereira",
    "hobbies": ["Programar", "assistir harry potter", "dormir"],
    "age": 21,
    "Father": "Marcelo Junior",
    "Mother": "Aparecida Barbosa"
}


def say_hello(name: str="Baby") -> str:
    """
    A function that says hello given a name,
    if a name hasn't provided you will be called 
    as "Baby" :)
    """

    return f"Hello {name}"


fire.Fire()