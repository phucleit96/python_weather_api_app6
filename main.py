from flask import Flask, render_template
import pandas as pd

# Initialize Flask application
app = Flask(__name__)

# Load station data
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[['STAID', 'STANAME                                 ']]


# Home route that renders a table of station data
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


# Route that returns weather data for a specific station and date
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Load the weather data for the specified station
    df = pd.read_csv(f"data_small/TG_STAID{station.zfill(6)}.txt", skiprows=20, parse_dates=['    DATE'])

    # Return the temperature for the specified date
    return {
        "station": station,
        "date": date,
        "temperature": df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    }


# Route that returns all weather data for a specific station
@app.route("/api/v1/<station>")
def all_data(station):
    # Load the weather data for the specified station
    df = pd.read_csv(f"data_small/TG_STAID{station.zfill(6)}.txt", skiprows=20, parse_dates=['    DATE'])

    # Convert the DataFrame to a dictionary and return it
    result = df.to_dict(orient='records')
    return result


# Route that returns all weather data for a specific station and year
@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    # Load the weather data for the specified station
    df = pd.read_csv(f"data_small/TG_STAID{station.zfill(6)}.txt", skiprows=20, parse_dates=['    DATE'])

    # Filter the DataFrame to keep only the rows for the specified year
    df['    DATE'] = df['    DATE'].astype(str)
    df_year = df[df['    DATE'].str.startswith(str(year))]

    # Convert the DataFrame to a dictionary and return it
    result = df_year.to_dict(orient='records')
    return result


# Run the application
if __name__ == "__main__":
    app.run(debug=True)