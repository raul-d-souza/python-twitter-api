def parse_secret(auth):
    secret = auth.split("=")
    return secret[1]
