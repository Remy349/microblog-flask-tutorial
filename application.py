from flaskr import app, db
from flaskr.models import User, Post


@app.shell_context_processor
def make_shell_contenxt():
    return {"db": db, "User": User, "Post": Post}
