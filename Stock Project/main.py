import finnhub

# Configure API key
configuration = finnhub.Configuration(
    api_key={
        'token': '<brpldinrh5rbpquq9qp0>' # Replace this
    }
)


finnhub_client = finnhub.DefaultApi(finnhub.ApiClient(configuration))

# Stock candles
print(finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249))
