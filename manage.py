import os
import traceback
from werkzeug.exceptions import HTTPException

import app.main.features.models
from app import api, blueprint
from app.main import create_app, db
from app.main.utils.core_helpers import log_error

app = create_app(os.getenv("RUN_MODE"))
app.register_blueprint(blueprint)

app.app_context().push()

# ERROR HANDLING
@app.errorhandler(Exception)
def handle_internal_error(error):
    db.session.rollback()
    traceback.print_exc()
    log_error(error)

    status_code = (
        error.code
        if hasattr(error, "code") and isinstance(error.code, int)
        else 500
    )

    response = {
        "success": False,
        "error": f"{error.__class__.__name__}: {str(error)}",
        "message": "Error del servidor"
    }
    return response, status_code


@api.errorhandler(HTTPException)
def handle_http_exception_api(error):
    traceback.print_exc()
    message = (
        error.description["message"]
        if isinstance(error.description, dict)
        else error.description
    )

    error_str = (
        error.description["error"]
        if isinstance(error.description, dict)
        else error.description
    )

    error_res = {
        "message": message,
        "success": False,
        "error": error_str
    }

    return error_res, error.code

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.debug)
