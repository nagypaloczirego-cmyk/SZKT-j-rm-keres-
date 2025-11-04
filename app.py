from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

BASE_URL = "https://old.realtimenext.hu/szkt"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stops")
def stops():
    r = requests.get(f"{BASE_URL}/init_stops.php")
    return r.json()

@app.route("/departures/<stop_id>")
def departures(stop_id):
    r = requests.get(f"{BASE_URL}/getStop.php?stopId={stop_id}&limit=20")
    return r.json()

@app.route("/vehicle")
def vehicle():
    route = request.args.get("route")
    vid = request.args.get("id")
    r = requests.get(f"{BASE_URL}/getVehicleData.php?route={route}&id={vid}")
    return r.json()

if __name__ == "__main__":
    app.run(debug=True)
