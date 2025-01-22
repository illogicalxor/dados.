import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

to_date = datetime.now()
from_date = to_date - timedelta(days=180)

from_timestamp = int(from_date.timestamp())
to_timestamp = int(to_date.timestamp())

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
params = {
    "vs_currency": "usd",
    "from": from_timestamp,
    "to": to_timestamp
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    prices = data.get('prices', [])
    if not prices:
        print("Nenhum dado encontrado no intervalo solicitado.")
    else:
        dates = []
        values = []
        for timestamp, price in prices:
            date = datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')
            dates.append(date)
            values.append(price)
            print(f"Data: {date}, Preco: {price}")

        print(f"\nTotal de registros: {len(prices)}")

        plt.figure(figsize=(10, 5))
        plt.plot( values, label="Preco do Bitcoin (USD)", color='blue')
        plt.xlabel("Data")
        plt.ylabel("Preco (USD)")
        plt.title("Preco do Bitcoin nos ultimos 180 dias")
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

except requests.RequestException as e:
    print(f"Erro ao fazer a requisicao: {e}")

except Exception as e:
    print(f"Erro ao processar os dados: {e}")

