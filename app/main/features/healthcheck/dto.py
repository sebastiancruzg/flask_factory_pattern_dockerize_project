from flask_restx import Namespace, fields


class HealthcheckDto:
    api = Namespace("healthcheck", description="Healthcheck operations")

    healthcheck = api.model("Healthcheck",{
        "status": fields.String(description="Healthcheck status"),
    })
