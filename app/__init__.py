import os

from flask_restx import Api
from flask import Blueprint
from flask_cors import CORS

from app.main.features.routes import namespaces

blueprint = Blueprint('api', __name__)
CORS(blueprint)

authorizations = {
    'token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(blueprint,
          prefix=os.environ["URL_MS"] + os.environ["API_VERSION"],
          title='MyFlaskProject',
          version=os.environ["VERSION"],
          description='API',
          security=["apiKey"],
          authorizations=authorizations
        )

for namespace in namespaces:
    api.add_namespace(namespace)
