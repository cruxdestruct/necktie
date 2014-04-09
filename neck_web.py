from flask import Flask, render_template, request
import necktie

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
    recommended = necktie.recommend_a_tie(thickness=thickness, collar=collar).analyze()
    
    rec_lines = recommended.splitlines()
    name = rec_lines[1].split()[1].strip("*").strip(":")
    sequence = " ".join(rec_lines[1].split()[2:])
    description = rec_lines[2:7]

    return render_template('step_three.html', name=name, sequence=sequence, description=description)
if __name__ == "__main__":
    app.debug = True
    app.run()