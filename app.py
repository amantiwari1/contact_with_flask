from flask import Flask, render_template, request, url_for
import sqlite3 as sql



app = Flask("__name__")



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stud", methods = ["POST","GET"])
def stud():
    if request.method == "POST":
        name = request.form["name1"]
        email1 = request.form["email"]
        phone = request.form["pnum"]
        mess = request.form["mess"]
        
        with sql.connect("test.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO contact (name,email,phone,mess) VALUES (?,?,?,?)",(name,email1,phone,mess))
            con.commit()
        return render_template("index.html") 
    else:
        return render_template("index.html")

    


if __name__ == "__main__":
    app.run(debug=True)