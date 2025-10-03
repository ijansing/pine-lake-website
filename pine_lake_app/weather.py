from flask import Blueprint, render_template

weather_bp = Blueprint("weather", __name__)

LAT = 45.8246543
LON = -89.9239465
TZ = "America/Chicago"


@weather_bp.route("/weather")
def weather_page():
    return render_template("weather.html", lat=LAT, lon=LON, tz=TZ)
