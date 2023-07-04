"""This script contains the main class for uploading images."""
from __future__ import annotations

from typing import Union

from flask import Flask
from werkzeug.datastructures import FileStorage


class FlaskImage:
    """An interface for uploading images."""

    def __init__(self, app: Union[Flask, None] = None) -> None:
        """Initialize the FlaskImage Extension.

        Parameters
        ----------
        app: Optional[Flask]
            The Flask App Instance.
        """
        if app is not None:
            self.init_app(app=app)

    def init_app(self, app: Flask) -> None:
        """Initialize the FlaskImage Extension when using the factory pattern.

        app: Flask
            The Flask App Instance.
        """
        self.app = app

    def server_upload(self, image_data: FileStorage) -> str:
        """Upload Image to the local server."""
        raise NotImplementedError()

    def server_redis_upload(self, image_data: FileStorage) -> str:
        """Upload Image to local server with redis task."""
        raise NotImplementedError()

    def server_celery_upload(self, image_data: FileStorage) -> str:
        """Upload Image to local server with celery task."""
        raise NotImplementedError()
