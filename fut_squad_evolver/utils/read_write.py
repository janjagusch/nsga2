"""
This module provides methods to read and write files.
File formats currently supported: Pickle, JSON.
"""


import json
import os
import pickle


def _get_extension(file_name):
    return file_name.split(".")[-1]


def _read_json(file_path):
    with open(file_path, "r") as file_pointer:
        return json.load(file_pointer)


def _read_pickle(file_path):
    with open(file_path, "rb") as file_pointer:
        return pickle.load(file_pointer)


EXTENSION_READER_MAP = {
    "json": _read_json,
    "p": _read_pickle
}


def read_file(directory, file_name, reader=None):
    if reader is None:
        extension = _get_extension(file_name)
        reader = EXTENSION_READER_MAP[extension]
    file_path = os.path.join(directory, file_name)
    return reader(file_path)


def _make_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def _write_json(file, file_path):
    with open(file_path, "w") as file_pointer:
        json.dump(file, file_pointer)


def _write_pickle(file, file_path):
    with open(file_path, "wb") as file_pointer:
        pickle.dump(file, file_pointer)


EXTENSION_WRITER_MAP = {
    "json": _write_json,
    "p": _write_pickle
}


def write_file(file, directory, file_name, writer=None, force=True):
    if force:
        _make_directory_if_not_exists(directory)
    if writer is None:
        extension = _get_extension(file_name)
        writer = EXTENSION_WRITER_MAP[extension]
    file_path = os.path.join(directory, file_name)
    writer(file, file_path)
