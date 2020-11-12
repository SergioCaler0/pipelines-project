
def get_pokemon_name(pokemon_tag):
    """
    Extracts book name
    Args:
        book_tag (bs4.element.Tag): corresponding to an Amazon book
    Returns:
        str: book title
    """
    pokemon_name_tag = pokemon_tag.find("a", class_="ent-name")
    pokemon_name = pokemon_name_tag.text
    
    return pokemon_name