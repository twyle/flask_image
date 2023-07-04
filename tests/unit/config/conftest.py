import pytest
from tempfile import TemporaryDirectory
from os import chmod
import stat

@pytest.fixture
def unwritable_dir():
    with TemporaryDirectory() as temp_dir_path:
        chmod(temp_dir_path, stat.S_IREAD)
        yield temp_dir_path
        
@pytest.fixture
def writable_dir():
    with TemporaryDirectory() as temp_dir_path:
        yield temp_dir_path