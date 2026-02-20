from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = f"Thank you {name}, I will contact you soon!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
