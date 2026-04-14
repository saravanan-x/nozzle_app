from flask import Flask, render_template, request
import main

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error  = None

    if request.method == "POST":
        try:
            f  = float(request.form["thrust"])
            pc = float(request.form["pressure"])
            tc = float(request.form["temperature"])
            y  = float(request.form["gamma"])
            r  = float(request.form["gas_constant"])

            altitude        = float(request.form["altitude"])
            sy              = float(request.form["sy"])
            SF              = float(request.form["SF"])
            divergent_angle = float(request.form["divergent_angle"])
            convergent_a    = float(request.form["convergent_a"])
            length          = float(request.form["length"])
            ta              = float(request.form["ta"])
            sa              = float(request.form["sa"])
            tha             = float(request.form["tha"])

            result = main.run_simulation(
                f, pc, tc, y, r, altitude,
                sy, SF, divergent_angle, convergent_a,
                length, ta, sa, tha
            )

        except ValueError as e:
            error = f"Please fill all fields with valid numbers. ({e})"
        except Exception as e:
            error = f"Simulation error: {e}"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)