import requests
import logging


def fetch_twitter_ads_data(account_id, access_token):
    """
    Fetches data from Twitter Ads API for the given account ID.
    
    Parameters:
    - account_id: The ID of the Twitter Ads account.
    - access_token: The OAuth token used to authenticate API requests.
    
    Returns:
    - A JSON object with the response data from the Twitter Ads API.
    """
    try:
        url = f"https://ads-api.twitter.com/9/accounts/{account_id}/stats"
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        params = {
            'granularity': 'TOTAL',
            'metric_groups': 'ENGAGEMENT,VIDEO',
            'start_time': '2023-07-01T00:00:00Z',
            'end_time': '2023-07-31T23:59:59Z'
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            logging.info("Successfully fetched data from Twitter Ads API")
            return response.json()
        else:
            logging.error(f"Error fetching data from Twitter Ads API: {response.status_code} - {response.text}")
            raise Exception(f"Failed to fetch Twitter Ads data: {response.status_code}")
    
    except Exception as e:
        logging.exception("Exception occurred while fetching Twitter Ads data")
        raise e
