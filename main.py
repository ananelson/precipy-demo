from precipy.main import render_file
from precipy.storage import GoogleCloudStorage

storage = GoogleCloudStorage()

import sys

import analytics
analytics_modules = [analytics]

if __name__ == '__main__':
    render_file(sys.argv[1], analytics_modules, storages=[storage])
