from flask_restx import Resource
from .dto import HealthcheckDto


health_ns = HealthcheckDto.api


@health_ns.route("")
class HealthcheckController(Resource):
    @health_ns.marshal_with(HealthcheckDto.healthcheck)
    def get(self):
        return {"status": "ok"}
