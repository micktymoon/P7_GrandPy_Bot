import googlemaps


def recup_latlong(lieu):
    gmaps = googlemaps.Client(key='AIzaSyAYIr_H7RBFICU0eGWe7hrm6a4AuibiQjI')
    # pyignore: unresolved
    adresse = gmaps.geocode(lieu)
    location = adresse[0]['geometry']['location']
    return location

print(recup_latlong('OpenClassrooms'))