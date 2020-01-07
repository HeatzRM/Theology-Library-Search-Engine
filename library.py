from app import app, db

# imports the application instance
from app.models import User


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User}
