from unittest.mock import Mock

from . import FlaskImage


def test_flask_image_not_none():
    """Test that the FlaskImage object is created."""
    flask_image = FlaskImage()
    assert flask_image is not None
    assert hasattr(flask_image, "app") is False


def test_flask_image_has_app():
    """Test that the FlaskImage has an app instance."""
    app = Mock()
    flask_image = FlaskImage()
    flask_image.init_app(app)
    assert flask_image is not None
    assert hasattr(flask_image, "app") is True
    assert flask_image.app is not None
