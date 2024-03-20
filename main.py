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


@app.route("/api/v1/<station>")
def all_data(station):
    df = pd.read_csv(f"data_small/TG_STAID{station.zfill(6)}.txt", skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient='records')
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    df = pd.read_csv(f"data_small/TG_STAID{station.zfill(6)}.txt", skiprows=20, parse_dates=['    DATE'])
    df['    DATE'] = df['    DATE'].astype(str)
    df_year = df[df['    DATE'].str.startswith(str(year))]
    result = df_year.to_dict(orient='records')
    return result


if __name__ == "__main__":
    app.run(debug=True)
