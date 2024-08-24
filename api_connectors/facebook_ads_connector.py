import requests
import logging


def fetch_facebook_ads_data(ad_account_id, access_token):
    """
    Fetches data from Facebook Ads API for the given ad account.
    
    Parameters:
    - ad_account_id: The ID of the Facebook Ads account.
    - access_token: The OAuth token used to authenticate API requests.
    
    Returns:
    - A JSON object with the response data from the Facebook Ads API.
    """
    try:
        url = f"https://graph.facebook.com/v13.0/act_{ad_account_id}/insights"
        params = {
            'access_token': access_token,
            'date_preset': 'last_30d',
            'fields': 'campaign_name,clicks,impressions'
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            logging.info("Successfully fetched data from Facebook Ads API")
            return response.json()
        else:
            logging.error(f"Error fetching data from Facebook Ads API: {response.status_code} - {response.text}")
            raise Exception(f"Failed to fetch Facebook Ads data: {response.status_code}")
    
    except Exception as e:
        logging.exception("Exception occurred while fetching Facebook Ads data")
        raise e