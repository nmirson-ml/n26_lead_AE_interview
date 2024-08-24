import requests
import logging


def fetch_google_ads_data(client_customer_id, developer_token, access_token):
    """
    Fetches data from Google Ads API for the given client customer ID.
    
    Parameters:
    - client_customer_id: The ID of the Google Ads client customer.
    - developer_token: The developer token from the Google Ads API.
    - access_token: OAuth token used to authenticate the API request.
    
    Returns:
    - A JSON object with the response data from the Google Ads API.
    """
    try:
        url = f"https://googleads.googleapis.com/v11/customers/{client_customer_id}/googleAds:searchStream"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'developer-token': developer_token,
        }
        query = {
            'query': "SELECT campaign.id, campaign.name, metrics.clicks, metrics.impressions FROM campaign"
        }
        
        response = requests.post(url, headers=headers, json=query)
        
        if response.status_code == 200:
            logging.info("Successfully fetched data from Google Ads API")
            return response.json()
        else:
            logging.error(f"Error fetching data from Google Ads API: {response.status_code} - {response.text}")
            raise Exception(f"Failed to fetch Google Ads data: {response.status_code}")
    
    except Exception as e:
        logging.exception("Exception occurred while fetching Google Ads data")
        raise e
