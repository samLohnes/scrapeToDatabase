# This is where the csv file will be read into a PSQL db utilizing Pandas and SQLAlchemy

from sqlalchemy import Column, Date, Float, Integer, String, create_engine, Table, MetaData
import pandas as pd
# 	Player	Nation	Pos	Age	Starts	Min	90s	Gls	Ast	G+A	G-PK	PK	PKatt	CrdY	CrdR	xG	npxG	xAG	npxG+xAG	PrgC	PrgP	PrgR	Gls	Ast	G+A	G-PK	G+A-PK	xG	xAG	xG+xAG	npxG	npxG+xAG	Team
def setClass():
    url = 'postgresql+psycopg2://sam:password@Localhost:5432/test'
    engine = create_engine(url, echo=True)
    metadata_obj = MetaData()

    # beginnings of the players_table, still need to add the rest of the columns
    players_table = Table(
        'players',
        metadata_obj,
        Column('player_ID', Integer, primary_key=True),
        Column('full_name', String(200)),
        Column('nation', String(200)),
        Column('position', String(200)),
        Column('age', Integer),
        Column('starts', Integer),
        Column('minutes', Integer),
        Column('games_played', Integer),
        Column('goals', Integer),
        Column('birthday', Date),
        Column('birthday_gmt', Date),
        Column('league', String(200)),
        Column('season', String(200))
    )

def uploadCSV():
    return