class VehiculeIndisponible(Exception):
    """Exception levée lorsqu'un véhicule est indisponible pour la location."""
    pass

class LocationDejaTerminee(Exception):
    """Exception levée lorsqu'une location est déjà terminée."""
    pass