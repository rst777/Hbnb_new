"""API v1 endpoints"""

from flask_restx import Api
from app.api.v1.user import api as user_api
from app.api.v1.place import api as place_api
from app.api.v1.review import api as review_api
from app.api.v1.amenity import api as amenity_api

__all__ = ['place_api', 'review_api', 'amenity_api']