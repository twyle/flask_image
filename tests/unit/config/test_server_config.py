from . import (
    ServerConfig,
    UploadDirectoryMissingException,
    UploadDirectoryNotSetException,
    UploadDirectoryUnWritable,
    PathIsNotDirectory
)
from unittest.mock import Mock
import pytest


def test_verify_server_config_raises_UploadDirectoryNotSetException():
    app = Mock()
    app.config = {}
    with pytest.raises(UploadDirectoryNotSetException):
        ServerConfig.verify_config(app)
        
def test_verify_server_config_raises_UploadDirectoryMissingException():
    app = Mock()
    app.config = {
        'UPLOAD_DIR': 'nosuchdir'
    }
    with pytest.raises(UploadDirectoryMissingException):
        ServerConfig.verify_config(app)
        
def test_verify_server_config_raises_PathIsNotDirectory():
    app = Mock()
    app.config = {
        'UPLOAD_DIR': __file__
    }
    with pytest.raises(PathIsNotDirectory):
        ServerConfig.verify_config(app)
    
def test_verify_server_config_raises_UploadDirectoryUnWritable(unwritable_dir):
    app = Mock()
    app.config = {
        'UPLOAD_DIR': unwritable_dir
    }
    with pytest.raises(UploadDirectoryUnWritable):
        ServerConfig.verify_config(app)
        
def test_verify_server_config_good(writable_dir):
    """Test that Flask app is correctly configured.
    
    This means that the UPLOAD_FOLDER is set.
    """
    app = Mock()
    app.config = {
        'UPLOAD_DIR': writable_dir
    }
    assert ServerConfig.verify_config(app) is None
    
def test_from_config(writable_dir):
    app = Mock()
    app.config = {
        'UPLOAD_DIR': writable_dir
    }
    server_config = ServerConfig.from_config(app)
    assert server_config is not None
    assert hasattr(server_config, 'upload_dir')
    assert isinstance(server_config, ServerConfig)