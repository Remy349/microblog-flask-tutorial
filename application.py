from flaskr import create_app, db, cli
from flaskr.models import User, Post

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_contenxt():
    return {"db": db, "User": User, "Post": Post}
