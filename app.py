from flask import Flask, render_template, request
from model import generate_image
import os

app = Flask(__name__, static_folder="static")


@app.route("/", methods=["GET", "POST"])
def index():
    image_path = None

    if request.method == "POST":
        text = request.form.get("prompt")

        # Generate image and save to static folder
        image_path = generate_image(text)

        # Make sure only relative static path goes to HTML
        image_path = "/" + image_path.replace("\\", "/")

    return render_template("index.html", image_path=image_path)


if __name__ == "__main__":
    app.run(debug=True)



