"""
This code runs functions that can create an art database storing information about artists, 
artworks, years, descriptions, and owners.
"""

from collections import defaultdict

def empty_db():
    """
    Returns an empty default dictionary as database.
    """
    database = defaultdict(dict)
    return database


def add_item(database, artist, artwork, year, description, owner):
    """
    Inputs a database and the information of a new artwork (artist name, artwork name, 
    year created, description, owner), returns returns a Boolean True or False 
    indicating whether the artwork was previously added.
    """
    if (artist in database.keys()) and (artwork in (database[artist]).keys()) == True:
        return False
    else:
        database[artist] = {artwork: (year, description, owner)}
        return True

    
def change_owner(database, artist, artwork, new_owner):
    """
    Given a database, the artist name and artwork name of a particular artwork, 
    and an new owner name, returns a Bolean value indicating whether the old owner 
    name of that artwork in the given database has been changed into the new owner name.
    """
    if (artist in database.keys()) and (artwork in (database[artist]).keys()) == True:
        info_list = list(database[artist][artwork])
        new_info = (info_list[0], info_list[1], new_owner)
        database[artist][artwork] = new_info
        return True
    else:
        return False
    
    
def select_artist(database, artist):
    """
    Inputs a database and an artist name, returns a new database with all of the 
    information (artist name, artwork name, year created, description, owner) 
    for the given artist in the given database.
    """
    new_dict = {}
    if (artist in database.keys()) == True:
        new_dict = defaultdict(dict)
        information = database[artist]
        new_dict[artist] = information
    return new_dict
        

def select_artwork(database, artwork):
    """
    Given a database and an artwork name, returns a new database with all of the 
    information (artist name, artwork name, year created, description, owner) 
    for any artwork with the given name in the given database.
    """
    new_dict = defaultdict(dict)
    for artist, art_info in database.items():
        if (artwork in art_info.keys()) == True:
            new_dict[artist][artwork] = art_info[artwork]
    return new_dict


def select_year(database, year):
    """
    Given a database and an year, returns a new database with all of the information
    (artist name, artwork name, year created, description, owner) for any artwork 
    from the given year in the given database.
    """
    new_dict = defaultdict(dict)
    for artist, art_info in database.items():
        for an_artwork, a_tuple in art_info.items():
            if a_tuple[0] == year:
                new_dict[artist][an_artwork] = art_info[an_artwork]
    return new_dict

def select_description(database, keyword):
    """
    Inputs a database and returns a new database with all of the information for
    artwork having a description containing the given keyword in the given database.
    """
    new_dict = defaultdict(dict)
    for artist, art_info in database.items():
        for an_artwork, a_tuple in art_info.items():
            if a_tuple[1].find(keyword) != -1:
                new_dict[artist][an_artwork] = art_info[an_artwork]
    return new_dict  


def select_owner(database, owner):
    """
    Returns a new database with all of the information (artist name, artwork name, year created, description, owner)
    for any artwork owned by the given owner in the given database.
    """
    new_dict = defaultdict(dict)
    for artist, art_info in database.items():
        for an_artwork, a_tuple in art_info.items():
            if a_tuple[2] == owner:
                new_dict[artist][an_artwork] = art_info[an_artwork]
    return new_dict


def format_results(database):
    """
    Inputs a database and returns a string with one line per artwork. For each artwork,  it lists the artist, 
    artwork, year, description, and owner, each separated by a comma and a space.
    """
    all_lines = ''
    for artist, art_info in database.items():
        for an_artwork, a_tuple in art_info.items():
            one_line = ', '.join([artist, an_artwork, str(a_tuple[0]), str(a_tuple[1]), str(a_tuple[2])])
            all_lines = '\n'.join([one_line,all_lines])
        return all_lines

    