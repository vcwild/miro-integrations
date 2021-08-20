import re
from typing import Dict


def filter_keys(array: dict, keys: str) -> Dict:
    return {key: array[key] for key in array.keys() if key in keys}


def remove_html(raw_html: str) -> str:
    """Clears html tags out

    Args:
            raw_html (str): Html string

    Returns:
            str: String without html tags
    """
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


def filter_links(raw_html: str) -> str:
    filter_text = re.findall(
        "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        raw_html,
    )
    try:
        clean_text = list(filter_text)[0]
    except:
        return
    return clean_text
