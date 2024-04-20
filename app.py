from flask import Flask, request, jsonify
from astro import models as mod

app = Flask(__name__)

@app.route("/natal_chart", methods=['POST'])
def natal_chart_endpoint():
    data = request.get_json(cache=True)
    chart = mod.NatalChart(data['date'], data['time'], data['location'])
    chart.calculate_all()
    planets = chart.get_planet_positions().to_dict(orient='records')
    houses = chart.get_house_positions().to_dict(orient='records'),
    aspects = chart.get_aspect_matrix().to_dict(orient='records'),
    return jsonify({
        'planets': planets,
        'houses': houses,
        'aspects': aspects
    })
    
if __name__ == '__main__':
    app.run(debug=True)