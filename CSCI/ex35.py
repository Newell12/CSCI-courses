class Painting:
    def __init__(self, artist, area):
        self.artist = artist
        self.area = area
    def too_bulky(self):
        return self.area > 1000

class Sculpture:
    def __init__(self, artist, weight):
        self.artist = artist
        self.weight = weight
    def too_bulky(self):
        return self.weight > 500

def display_artist(artist, art_list):
    new_list = []
    for i in range(len(art_list)):
        if art_list[i].artist == artist and art_list[i].too_bulky()==False:
            new_list.append(art_list[i])
    return new_list
