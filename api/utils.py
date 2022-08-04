from bs4 import BeautifulSoup as bs


def check_config(CONFIG: dict) -> dict:
    """Validates the configuration file. If it's valid, parses it and returns it.

    Args:
        CONFIG (dict): Config parameters:
            "backlog": int
            "debug": bool
            "host": str
            "log_level": str
            "port": int
            "reload": bool
            "timeout_keep_alive": int
            "workers": int

    Raises:
        ValueError: If parameters are missing in the config file.
        ValueError: If parameters doesn't have a valid type.

    Returns:
        dict: Config file parsed to match the expected format.
    """
    fields = {
        "backlog": int,
        "debug": bool,
        "host": str,
        "log_level": str,
        "port": int,
        "reload": bool,
        "timeout_keep_alive": int,
        "workers": int,
    }

    for field in fields:
        if field not in CONFIG:
            raise ValueError(f"{field} is missing in config file.")

    config = {}
    for field_name, field_value in fields.items():
        try:
            config[field_name] = field_value(CONFIG[field_name])
        except ValueError as e:
            raise ValueError(f"{field_name} is not a valid {field_value}") from e
    return config


#######################################################################################################################


def extract_data(data: bs) -> dict:
    """From a BeautifulSoup object, extracts the word, its meanings and their respective contributors.

    Args:
        data (bs): BeautifulSoup object with the HTML data.

    Returns:
        dict: Returns a dictionary with the word, its meanings and their respective contributors.
    """
    word_web = data.find("a", {"class": "word"}).text

    meanings = data.find_all("div", {"class": "meaning"})
    meanings = [meaning.text for meaning in meanings]

    contributors = data.find_all("div", {"class": "contributor"})
    contributors = [contributor.text for contributor in contributors]

    meanings_dict = {}
    for index, (meaning, contributor) in enumerate(zip(meanings, contributors)):
        meanings_dict[index] = {
            "meaning": meaning,
            "contributor": contributor,
        }

    return {"Word": word_web, "Meanings": meanings_dict}
