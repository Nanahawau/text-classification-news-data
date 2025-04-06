# TODO declare python directory to store data.
# TODO Get 50k data per directory.


import requests
import json
import pandas as pd

# def fetch_data_from_api(api_url, params=None, headers=None, filename='output.json'):
#     """
#     Fetches data from the specified API and writes it to a file.
#
#     Args:
#         api_url (str): The URL of the API endpoint.
#         params (dict, optional): Optional query parameters for the API request. Defaults to None.
#         headers (dict, optional): Optional headers for the API request. Defaults to None.
#         filename (str): The name of the file to write the data to. Defaults to 'output.json'.
#     """
#     formatted_data = []
#     try:
#         topics = ['blockchain', 'earnings', 'mergers_and_acquisitions',
#         'ipo', 'financial_markets', 'economy_fiscal',
#         'economy_monetary', 'energy_transportation', 'finance',
#         'life_sciences', 'manufacturing', 'real_estate', 'retail_wholesale', 'technology'
#         ]
#         for item in topics:
#             formatted_url = "{}{}".format(api_url, "&topics=" + item)
#             print(f"api url to {formatted_url}")
#             # Send GET request to the API
#             response = requests.get(formatted_url, params=params, headers=headers)
#             # Check if the response was successful
#             if response.status_code == 200:
#                 print(f"Data successfully fetched from {api_url}")
#                 data = response.json()  # Parse the JSON response
#
#                 feed = data['feed']
#                 topic = item
#                 for key in feed:
#                     key["topic"] = topic
#
#                 formatted_data.extend(feed)
#             else:
#                 print(f"Failed to fetch data. Status code: {response.status_code}")
#
# #         # Write data to a file
# #         with open(filename, 'w') as file:
# #             json.dump(formatted_data, file, indent=4)
# #         print(f"Data saved to {filename}")
#
#         # Convert to DataFrame
#         df = pd.DataFrame(formatted_data)  # Assuming 'feed' contains the list of items
#
#
#         # Save as CSV
# #         df.to_csv("alphavantage.csv", index=False)
#
#         # Save as JSON
#         df.to_json("alphavantage.json", orient="records", indent=2)
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# # Example usage
# api_url='https://www.alphavantage.co/query?function=NEWS_SENTIMENT&apikey=EM99ZLQBRCK6350E&limit=1000'
# # api_url ='https://finnhub.io/api/v1/news?token=cv8vas9r01qk2jfsr5hgcv8vas9r01qk2jfsr5i0'
# params = {}
# fetch_data_from_api(api_url, params=params, filename='alphavantage.json')


def convertToJSON():
    # Read CSV
    df = pd.read_csv("alphavantage.csv")

    # Save as JSON (array of objects)
    df.to_json("alphavantage.json", orient="records", indent=2)

convertToJSON()