from urllib.parse import urlparse


def is_valid_url_structure(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False