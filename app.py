from flask import Flask, render_template
import os


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")


@app.route('/')
def home():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')