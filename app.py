import os
from dotenv import load_dotenv

load_dotenv()

# app init
from . import create_app
app = create_app(os.getenv("CONFIG_MODE"))

@app.route('/')
def hello():
    return "Hello World!"

from .students import routes
from .homework import routes
from .assignments import routes


if __name__ == "__main__":
    app.run(debug=True)
