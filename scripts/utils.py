import os
import json
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


def save_json(data, path):
    file_path = os.path.abspath(os.path.join(os.path.pardir, path))

    with open(file_path, 'w') as fp:
        json.dump(data, fp)


def read_json(path):
    file_path = os.path.abspath(os.path.join(os.getcwd(), path))

    with open(file_path, 'r') as fp:
        data = json.load(fp)

    return data