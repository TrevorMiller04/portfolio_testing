from flask import Flask, render_template, request, redirect, url_for
import os
import csv

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/<string:new_page>")
def new_page(new_page="index.html"):
    return render_template(new_page)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_database(data)
            return redirect("/thankyou.html")
        except:
            return "Did not save to database"
    else:
        return "something went wrong"

def write_to_database(data):
    with open("database.csv", "a", newline="") as file:
            email = data['email']
            subject = data['subject']
            message = data['message']
            csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email,subject,message])
            #file.write(f"Email: {data["email"]}\nSubject: {data["subject"]}\nMessage: {data["message"]}\n\n")


if __name__ == "__main__":
    app.run(debug=True)


