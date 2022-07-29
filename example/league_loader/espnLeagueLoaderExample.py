from leeger import ESPNLeagueLoader

if __name__ == "__main__":
    # Get a League object with years 2019 and 2020 for ESPN league with ID: 12345678.
    espnLeagueLoader = ESPNLeagueLoader("12345678", [2019, 2020])
    league = espnLeagueLoader.loadLeague()

    # Save league stats to an Excel sheet.
    league.toExcel("C:\\myLeagueStats.xlsx")

    # Sometimes the same owner will have a different name in different years.
    # Here, the same owner has "John Smith" and "Johnny Smith" as their owner names in ESPN.
    # To let the library know that you want these owners to be evaluated as the same owner,
    # a dictionary with the desired owner name and their aliases can be passed in.
    ownerNamesAndAliases = {"John Smith": ["John Smith", "Johnny Smith"]}
    espnLeagueLoader = ESPNLeagueLoader("12345678", [2019, 2020], ownerNamesAndAliases=ownerNamesAndAliases)
    league = espnLeagueLoader.loadLeague()
