# Weather Station API
![DEMO](https://i.imgur.com/Yfe04ip.gif)
This is a simple Flask application that serves weather data from different weather stations.

## Endpoints

The application has three main endpoints:

- `/api/v1/<station>/<date>`: This endpoint returns weather data for a specific station and date. The `station` parameter should be the ID of the station, and the `date` parameter should be the date you want data for, in the format `YYYY-MM-DD`.

- `/api/v1/<station>`: This endpoint returns all weather data for a specific station. The `station` parameter should be the ID of the station.

- `/api/v1/yearly/<station>/<year>`: This endpoint returns all weather data for a specific station and year. The `station` parameter should be the ID of the station, and the `year` parameter should be the year you want data for.

## Data

The weather data is read from CSV files named `TG_STAID<station>.txt`, where `<station>` is the ID of the station. Each CSV file has a 'DATE' column for the date and a 'TG' column for the temperature.

## Running the Application

To run the application, simply execute the `main.py` script with Python. The application will start a server on `localhost:5000` (or another port if you specify it), and you can access the endpoints from there.

## Dependencies

The application depends on Flask and pandas. You can install these with pip:

```bash
pip install flask pandas