from models.album import Album
from models.artist import Artist
import repositiories.album_repository as album_repository 
import repositiories.artist_repository as artist_repository 

artist1 = Artist ("Biffy Clyro")

album1 = Album ("Many of Horrors", "rock", artist1 )



result = album_repository.select_all()
