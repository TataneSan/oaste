  def decimal_to_dms(decimal):
    """
    Convertit une coordonnée décimale en notation DMS.
    La coordonnée doit être un nombre décimal.
    """
    # Sépare la partie entière des décimales
    degrees = int(decimal)
    decimals = abs(decimal - degrees)

    # Convertit les décimales en minutes et secondes
    minutes = int(decimals * 60)
    seconds = round((decimals * 3600) % 60, 2)

    # Formate la coordonnée en notation DMS
    dms = f"{degrees}°{minutes}'{seconds}''"
    return dms
