"""This module contains the base configuration."""
from abc import ABC, abstractclassmethod, abstractstaticmethod

from flask import Flask
from typing_extensions import Self


class Config(ABC):
    """This is the base configuration class.

    The configuration for AWS, Google and Local Server
    all inherit from this class.
    """

    @abstractclassmethod
    def from_config(cls, app: Flask) -> Self:
        """Configure from the Flask App configuration."""
        raise NotImplementedError()

    @abstractstaticmethod
    def verify_config(app: Flask) -> None:
        """Verify that the Flask Config has all the neccessary config."""
        raise NotImplementedError()
