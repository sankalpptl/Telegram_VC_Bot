HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["2500594"])
    API_HASH = environ["6704f1885e4cc07762e1684128da398d"]
    SESSION_STRING = environ["BQAyqgQM39V9yr4X4sO4BA33G4mBEpfKjg6fGeoN2QbzOiENKNExx6Kb_bQAu_1oEAcICk2gY6Lzb-3Dk50-UOZavtkr_H-wXYbSvv3qjBnL4v9tiqgYvVrUIjk2Oob_a997z6OPz6iGcvblA6SY4MHrOOuDn9Z_gEQCsxlEvx9F2WLhNyfTB-7FGIMPB1NrpHG1YPryfqeWQnj2xc8u23-DL2xBJ-F6ac868upT2JQxnxnN_UkJfBdTOek70JKWnu-p341RRxqxI2fezkVsODr-RXPEKM-y8v1tZNWyuSi_X3X-WEde3oODdJEqETaegdXtLCaKg_LpBlx_9wyC00-8VBwOGAA"]  # Check Readme for session
    ARQ_API_KEY = environ["OMLZAT-SXTYXT-UFMWUM-JCWMIO-ARQ"]
    DEFAULT_SERVICE = (
        environ["DEFAULT_SERVICE"]
        if "DEFAULT_SERVICE" in environ
        else "youtube"
    )

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 2500594
    API_HASH = "6704f1885e4cc07762e1684128da398d"
    ARQ_API_KEY = "OMLZAT-SXTYXT-UFMWUM-JCWMIO-ARQ"
    DEFAULT_SERVICE = "youtube"  # Must be one of "youtube"/"deezer"/"saavn"

# don't make changes below this line
ARQ_API = "https://thearq.tech"
