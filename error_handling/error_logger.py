import logging

# Configure logging
logging.basicConfig(
    filename='/var/log/app/error.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.ERROR
)

def log_error(error_message):
    """
    Log an error message to the error log.

    Args:
        error_message (str): The error message to log.
    """
    try:
        logging.error(error_message)
        print(f"Error logged: {error_message}")
    except Exception as e:
        print(f"Failed to log error: {e}")
