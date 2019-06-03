import os

config = {
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "MAX_CONTENT_LENGTH": 1024 * 1024,
    "auth_dir": "./auth",
    "storage_dir": "./storage"
}
