from models.album import Album
from models.artist import Artist
import repositiories.album_repository as album_repository 
import repositiories.artist_repository as artist_repository 


album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist ("Biffy Clyro")
artist_repository.save(artist1)

artist2 = Artist("Meatloaf")
artist_repository.save(artist2)

artist3 = Artist("Rolling Stones")
artist_repository.save(artist3)

artist4 = Artist("The Fratellis")
artist_repository.save(artist4)

album1 = Album ("Many of Horrors", "rock", artist1)
album_repository.save(album1)

album2 = Album ("Bat out of Hell", "rock", artist2)
album_repository.save(album2)

album3 = Album ("Sticky Fingers", "blues rock", artist3)
album_repository.save(album3)

album4 = Album("Costello Music", "indie rock", artist4)
album_repository.save(album4) 

album1.title = "Black Chandieler"
album_repository.update(album1)

album2.title = "Bat out of Hell II"
album_repository.update(album2)

artist_repository.delete(3)
album_repository.delete(3)

result = album_repository.select_all()
for album in result:
    print(f"{album.title, album.genre, album.id}")

result = artist_repository.select_all()
for artist in result:
    print(f"{artist.name, artist.id}")