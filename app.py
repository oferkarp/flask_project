import json
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if "register" in request.form:
            name = request.form.get("username")
            phone_number = request.form.get("phone_number")

            student = {"name": name, "phone_number": phone_number}

            with open("students.json") as file:
                students = json.load(file)

            students.append(student)

            with open("students.json", "w") as file:
                json.dump(students, file)

        elif "Login" in request.form:
            name = request.form.get("username")
            phone_number = request.form.get("phone_number")

            with open("students.json") as file:
                students = json.load(file)

            logged_in = False

            for student in students:
                if student["name"] == name and student["phone_number"] == phone_number:
                    logged_in = True
                    break

            if logged_in:
                return render_template("students.html", students=students)
            else:
                return render_template("students.html", students=["error"])
            

    return render_template("index.html")

@app.route("/students", methods=["GET"])
def students():
    # Your code to retrieve and process student data goes here
    return render_template("students.html")

if __name__ == '__main__':
    app.run(debug=True, port=9000)
