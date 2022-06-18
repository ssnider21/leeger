from dataclasses import dataclass

from src.leeger.enum.MatchupType import MatchupType
from src.leeger.model.Matchup import Matchup
from src.leeger.model.abstract.UniqueId import UniqueId


@dataclass(kw_only=True)
class Week(UniqueId):
    weekNumber: int
    matchups: list[Matchup]

    @property
    def isPlayoffWeek(self) -> bool:
        isPlayoffWeek = False
        for matchup in self.matchups:
            if matchup.matchupType == MatchupType.PLAYOFF:
                isPlayoffWeek = True
                break
        return isPlayoffWeek or self.isChampionshipWeek

    @property
    def isChampionshipWeek(self) -> bool:
        isChampionshipWeek = False
        for matchup in self.matchups:
            if matchup.matchupType == MatchupType.CHAMPIONSHIP:
                isChampionshipWeek = True
                break
        return isChampionshipWeek
