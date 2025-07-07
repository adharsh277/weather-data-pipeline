import requests
import os
from azure.storage.blob import BlobServiceClient

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "London"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

response = requests.get(URL)
data = response.json()

blob_conn_str = os.getenv("STORAGE_CONN_STRING")
blob_client = BlobServiceClient.from_connection_string(blob_conn_str)
container_client = blob_client.get_container_client("weather-data")

container_client.upload_blob(name=f"{CITY}_weather.json", data=str(data), overwrite=True)
