# Configuration for database and environment variables

import os

def get_database_config():
    return {
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'USER': os.getenv('DB_USER', 'user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
        'NAME': os.getenv('DB_NAME', 'database')
    }

if __name__ == '__main__':
    config = get_database_config()
    print(config)