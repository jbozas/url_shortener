import secrets


class Tokenize:
    async def generate_shorter_link():
        url_shorted = secrets.token_urlsafe(6)
        return url_shorted
