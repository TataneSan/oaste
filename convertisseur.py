def dms_to_decimal(dms):
    """
    Convertit une coordonnée DMS en notation décimale.
    La coordonnée doit être une chaîne de caractères sous la forme "DD°MM'SS''".
    """
    # Sépare les degrés, minutes et secondes en utilisant la méthode split()
    dms_split = dms.split("°")
    deg = float(dms_split[0])
    dms_split = dms_split[1].split("'")
    minute = float(dms_split[0])
    sec = float(dms_split[1].strip('"'))

    # Convertit les minutes et secondes en fractions de degrés
    decimal = deg + (minute / 60) + (sec / 3600)
    return decimal
