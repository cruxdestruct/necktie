from flask import Flask, render_template, request
import necktie, re

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
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
    name = recommended.analysis.name.strip("*")
    sequence = str(recommended)
    description = rec_lines[2:7]

    return render_template('step_three.html', name=name, sequence=sequence, description=description)
if __name__ == "__main__":
    app.debug = True
    app.run()