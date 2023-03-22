from db.run_sql import run_sql
from models.album import Album
import repositiories.artist_repository as artist_repository


def select_all():
    # set up an empty lsit to return
    albums = []
    sql = "SELECT * FROM albums"
    # this is what is going on in sql (postico)
    results = run_sql(sql)
    # this is what makes sql work in python using the run_sql function

    for row in results:
        # we will now create a new ablbum object
        artist = artist_repository.select ( row ['artist_id'])
        # above is defining what artist is above by getting the Artist object
        new_album = Album(row['title'],
                     row['genre'], 
                     artist, 
                     row ['id']
        )
        albums.append(new_album)
        # this is adding the the albums list with the newly created new_album object
    return albums
# this is returing the list albums (stated above)

# delete_all
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

# # delete(id)
def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql,values)

# # save(task)
def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id)\
        VALUES (%s,%s,%s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

# # select(id)
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        selected_album = results[0]
        artist = artist_repository.select ( selected_album ['artist_id'] )
        album = Album(selected_album['title'],
                    selected_album['genre'],
                    artist, 
                    selected_album['id']
                    )
    return album

def update(album):
    sql = """UPDATE albums 
            SET (title, genre, artist_id) 
            = (%s,%s,%s) 
            WHERE id = %s """
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql,values)


def albums_for_artist(artist):
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql,values)

    artist_albums = []
    for row in results:
        album = Album(
                    row['title'],
                     row['genre'], 
                     artist, 
                     row['id']
                    )
        
        artist_albums.append(album)

    return artist_albums