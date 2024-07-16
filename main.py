from flask import Flask, render_template
import yfinance as yf
from prophet import Prophet
import plotly.graph_objs as go

app = Flask(__name__)

def predict(ticker):
    data = yf.download(ticker)
    data = data.reset_index()
    data[['ds', 'y']] = data[['Date', 'Close']]
    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Predicted'))
    fig.add_trace(go.Scatter(x=data['ds'], y=data['y'], name='Actual'))
    graphJSON = fig.to_json()

    return graphJSON

@app.route('/predict/<ticker>', methods=['GET'])
def main(ticker):
    return render_template('graph.html', graphJSON=predict(ticker))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
