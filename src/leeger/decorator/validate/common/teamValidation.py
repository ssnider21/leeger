from src.leeger.exception.InvalidTeamFormatException import InvalidTeamFormatException
from src.leeger.model.Team import Team


def checkAllTypes(team: Team) -> None:
    """
    Checks all types that are within the Team object.
    """

    if type(team.ownerId) != str:
        raise InvalidTeamFormatException("Team owner ID must be type 'str'.")
    if type(team.name) != str:
        raise InvalidTeamFormatException("Team name must be type 'str'.")