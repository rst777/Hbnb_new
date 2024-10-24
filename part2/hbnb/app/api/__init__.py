"""API v1 endpoints"""

from flask_restx import Api
from app.api.v1.users import api as user_api
from app.api.v1.places import api as place_api
from app.api.v1.reviews import api as review_api
from app.api.v1.amenities import api as amenity_api

__all__ = ['place_api', 'review_api', 'amenity_api', 'user_api']
