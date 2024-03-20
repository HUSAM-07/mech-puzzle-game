from flask import Flask, render_template, session, abort, redirect, url_for
import os, random, cv2
from base64 import b64encode, b64decode

app = Flask(__name__)
app.config["SECRET_KEY"] = "adasdljnsdihvu93887lasd"

@app.route("/puzzle/<mp>", methods=["GET"])
def puzzle(mp):
    files = os.listdir("static/puzzleimages")
    if mp == "random":
        image = random.choice(files)
        return redirect(url_for("puzzle", mp=b64encode(image.split(".")[0].encode("utf-8")).decode("utf-8")))
    else:
        mp = b64decode(mp).decode("utf-8")
        if mp+".jpg" in files:
            image = mp+".jpg"
        else:
            abort(404)
    
    image_path = "static/puzzleimages/" + image
    image_height , image_width = cv2.imread(image_path).shape[:2]
    return render_template("puzzle.html", image=image_path.lstrip("static/"), difficulty=0.2, max_time=300, puzzle_pieces=4, height=image_height, width=image_width)

@app.route("/blank/<mp>", methods=["GET"])
def fib(mp):
    mp = b64decode(mp).decode("utf-8")
    files = os.listdir("static/puzzleimages")
    if mp+".jpg" in files:
        image = mp+".jpg"
    else:
        abort(404)
    
    return render_template("blank.html", word=mp, image="puzzleimages/"+image)

