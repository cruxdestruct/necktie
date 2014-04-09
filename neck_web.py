from flask import Flask, render_template, request
import necktie, random

app = Flask(__name__)
app.config.from_object(__name__)

def rand_header():
    return random.choice(["Custom necktie knots, algorithmically generated for maximum style",
                         "Men's fashion without the pictures"])

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
    recommended = necktie.recommend_a_tie(thickness=thickness, collar=collar)
    analysis = recommended.analyze()
    rec_lines = analysis.splitlines()
    k = {'name' : recommended.analysis.name.strip("*"),
         'sequence' : str(recommended),
         'description' : rec_lines[2:7]
         }
    return render_template('show_knot.html', k = k, slug="neck_web recommends...")

@app.route("/random")
def random_knot():
    knot = necktie.linear_build()
    analysis = knot.analyze()
    knot_lines = analysis.splitlines()
    k = {'name' : knot.analysis.name.strip("*"),
         'sequence' : str(knot),
         'description' : knot_lines[2:7]
         }
    return render_template('show_knot.html', k = k, slug="behold,") 

if __name__ == "__main__":
    app.debug = True
    app.run()