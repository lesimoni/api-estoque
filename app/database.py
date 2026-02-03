import fdb
import os

def get_connection():
    return fdb.connect(
        host=os.getenv("FB_HOST"),
        database=os.getenv("FB_DATABASE"),
        user=os.getenv("FB_USER"),
        password=os.getenv("FB_PASSWORD"),
        port=int(os.getenv("FB_PORT", 3050)),
        charset="ISO8859_1"
    )
