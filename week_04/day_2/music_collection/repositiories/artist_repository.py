from db.run_sql import run_sql
from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artist () VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'] )
        artist.append(artist)
    return artists


def select(id):
    artist = None
    sql = "SELECT * FROM artist WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

     # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        artist = Artist(result['name'], result['id'] )
    return artist


def delete_all():
    sql = "DELETE  FROM artists"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(artist):
    sql = "UPDATE artist SET (name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)