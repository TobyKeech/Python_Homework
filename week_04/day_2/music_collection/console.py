from models.album import Album
from models.artist import Artist
import repositiories.album_repository as album_repository 
import repositiories.artist_repository as artist_repository 


album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist ("Biffy Clyro")
artist_repository.save(artist1)

album1 = Album ("Many of Horrors", "rock", artist1)
album_repository.save(album1)

result = album_repository.select_all()
for album in result:
    print(f"{album.title}")
