# Soccer-Fire

CLI application that was implemented using Fire python library.
It make requests in [API-Futebol](https://www.api-futebol.com.br/) and shows Brasileirão informations in your shell


# Installation

1. Clone this repo

```sh
git clone https://github.com/Lnvictor/soccer-fire
```

2. Install requirements from requirements.txt file
```commandline
pip install -r requirements.txt
```

3. Set  your api key in .env file

## How to run

```shell
python fire_soccer.py <COMMAND>
```

## Commands

#### 1. br_info <info>

Returns general information about the championship.
Type "python fire_soccer.py br_info --help" to see all informations possible.


#### 2. br_class_info <position>

Returns classification information from Brasilian soccer championship.