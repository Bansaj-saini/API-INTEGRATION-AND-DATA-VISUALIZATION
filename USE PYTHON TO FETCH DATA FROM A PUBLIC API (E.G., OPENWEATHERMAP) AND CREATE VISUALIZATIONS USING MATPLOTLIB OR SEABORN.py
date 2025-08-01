import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fetch data from OpenWeatherMap
api_key = "YOUR_API_KEY"
city = "Delhi"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
response = requests.get(url).json()

# Extract data
data = []
for item in response['list']:
    data.append({
        'Date': item['dt_txt'],
        'Temperature': item['main']['temp']
    })
df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Temperature'], marker='o')
plt.xticks(rotation=45)
plt.title(f"Temperature Forecast for {city}")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()