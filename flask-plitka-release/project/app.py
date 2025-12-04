from flask import Flask, render_template, request
from plitka import Ptitle

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        need_m2 = float(request.form["need_m2"])
        color = request.form["color"]
        tile_index = int(request.form["tile_index"])

        tile = Ptitle[tile_index]
        result = tile.calc_order(need_m2, color)

    return render_template("index.html", Ptitle=Ptitle, result=result)


if __name__ == "__main__":
    app.run(debug=True)
