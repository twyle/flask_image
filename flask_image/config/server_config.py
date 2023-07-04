"""This module contains the config for upload to server."""
import os
from dataclasses import dataclass
from os import access
from os.path import exists, isdir

from flask import Flask
from typing_extensions import Self

from ..exceptions import (PathIsNotDirectory, UploadDirectoryMissingException,
                          UploadDirectoryNotSetException,
                          UploadDirectoryUnWritable)
from .config import Config


@dataclass
class ServerConfig(Config):
    upload_dir: str

    @classmethod
    def from_config(cls, app: Flask) -> Self:
        ServerConfig.verify_config(app)
        upload_dir: str = app.config.get(
            "FLASK_IMAGE_UPLOAD_DIR", ""
        ) or app.config.get("UPLOAD_DIR", "")
        return cls(upload_dir=upload_dir)

    @staticmethod
    def verify_config(app: Flask) -> None:
        upload_dir: str = app.config.get(
            "FLASK_IMAGE_UPLOAD_DIR", ""
        ) or app.config.get("UPLOAD_DIR", "")
        if not upload_dir:
            raise UploadDirectoryNotSetException(
                "The Upload Directory path was not set."
            )
        if not exists(upload_dir):
            raise UploadDirectoryMissingException(
                f'The upload folder "{upload_dir}" does not exist.'
            )
        if not isdir(upload_dir):
            raise PathIsNotDirectory(f"'{upload_dir}' isn't a folder.")
        if not access(upload_dir, os.W_OK):
            raise UploadDirectoryUnWritable(
                f'The application cannot write to "{upload_dir}".'
            )
