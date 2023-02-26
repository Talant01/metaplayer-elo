def expected_win_rate(team1_elo, team2_elo):
    """
    Calculates the expected win rate of two teams based on their Elo ratings.

    Parameters:
    team1_elo (float): The Elo rating of team 1.
    team2_elo (float): The Elo rating of team 2.

    Returns:
    float: The expected win rate of team 1, as a percentage between 0 and 1.
    """
    exponent = (team2_elo - team1_elo) / 400.0
    expected_win = 1.0 / (1.0 + pow(10, exponent))
    return expected_win


def normalize_dict(data):
    """
    Normalize the values of a dictionary to be between 0 and 1.

    Parameters:
    data (dict): The dictionary to normalize.

    Returns:
    dict: The normalized dictionary.
    """
    total = sum(data.values())

    total = 1 if total == 0 else total

    return {key: val/total for key, val in data.items()}