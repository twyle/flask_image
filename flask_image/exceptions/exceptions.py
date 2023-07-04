class UploadDirectoryNotSetException(Exception):
    """Raised when the path to upload Directory is not set."""


class UploadDirectoryMissingException(Exception):
    """Raised when the upload directory does not exist."""


class UploadDirectoryUnWritable(Exception):
    """Raised when the application is unable to write to upload directory."""


class PathIsNotDirectory(Exception):
    """Riased when the provided upload path is not a folder."""
