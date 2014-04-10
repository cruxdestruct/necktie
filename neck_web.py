from flask import Flask, render_template, request
import necktie, random, urllib.parse

app = Flask(__name__)
app.config.from_object(__name__)

def rand_header():
    return random.choice(["Custom necktie knots, algorithmically generated for maximum style",
                         "Men's fashion without the pictures"])

def prepare_for_display(knot):
    analysis = knot.analyze()
    knot_lines = analysis.splitlines()
    return {'name' : knot.analysis.name.strip("*"),
         'sequence' : str(knot),
         'description' : knot_lines[2:7]
         }

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/recommend")
def recommend():
   return render_template('recommend.html')

@app.route("/step_two")
def step_two():
    thickness = request.args.get('thickness')
    return render_template('step_two.html', thickness=thickness)

@app.route("/step_three")
def step_three():
    thickness = request.args.get('thickness')
    collar = request.args.get('collar')
    if thickness == "none":
        thickness = ""
    if collar == "none":
        collar = ""
    k = prepare_for_display(necktie.recommend_a_tie(thickness=thickness, collar=collar))
    return render_template('show_knot.html', k = k, slug="neck_web recommends...")

@app.route("/random")
def random_knot():
    k = prepare_for_display(necktie.linear_build())
    return render_template('show_knot.html', k = k, slug="behold,") 

@app.route("/tie")
def tie_a_tie():
    walk = request.args.get('walk')
    if not walk: 
        knot = necktie.Knot()
        walk = str(knot)
    else:
        knot = necktie.Knot(walk)
    if knot.final() == "Ti":
        k = prepare_for_display(knot)
        return render_template('show_knot.html', k = k, slug="you tied:")
    else:
        tie_str = str(knot)
        possibilities = possibilities = [name.strip("*") for walk, name in necktie.NAMED_KNOTS.items() if tie_str == walk[:len(tie_str)]]
        choices = knot.legal_intersection()
        walk_url = urllib.parse.quote_plus(walk)
        return render_template('tie_a_tie.html', walk=tie_str, choices=choices, qs=walk_url, p=possibilities)

if __name__ == "__main__":
    app.run()