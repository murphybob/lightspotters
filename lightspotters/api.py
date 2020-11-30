import json
import logging
from http.client import HTTPException

from flask import request, jsonify, Blueprint
from flask_expects_json import expects_json

from lightspotters.models import Spot, db

log = logging.getLogger(__name__)
api = Blueprint('api', __name__)


@api.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": str(e.description),
    })
    response.content_type = "application/json"
    return response


@api.route('/spot', methods=['post'])
@expects_json({
    'type': 'object',
    'properties': {
        'name': {'type': 'string'}
    },
    'required': ['name'],
    'additionalProperties': False
})
def create_spot():
    new_spot = Spot(**request.json)
    db.session.add(new_spot)
    db.session.commit()
    log.info("Created new spot", new_spot.id, new_spot.name)
    return jsonify({
        'id': new_spot.id,
        'name': new_spot.name
    })


@api.route('/spot/<int:spot_id>', methods=['get'])
def get_spot(spot_id: str):
    spot = Spot.query.filter(Spot.id == spot_id).one()
    return jsonify({
        'id': spot.id,
        'name': spot.name
    })
