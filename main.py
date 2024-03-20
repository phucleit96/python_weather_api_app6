from flask import Flask, render_template
import pandas as pd
import glob
app = Flask(__name__)
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[['STAID', 'STANAME                                 ']]
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pd.read_csv(f"data_small/TG_STAID{station.zfill(6)}.txt", skiprows=20, parse_dates=['    DATE'])


    return {
        "station": station,
        "date": date,
        "temperature": df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    }


if __name__ == "__main__":
    app.run(debug=True)
