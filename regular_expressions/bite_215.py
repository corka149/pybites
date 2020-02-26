import re

pattern = re.compile(r'PB(-[\w]{8}){4}')


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    return bool(pattern.fullmatch(key))
