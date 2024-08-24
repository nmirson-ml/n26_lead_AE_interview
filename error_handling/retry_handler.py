import time
import logging

# Configure logging for retries
logging.basicConfig(
    filename='/var/log/app/retry.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def retry_on_failure(func, max_retries=3, delay=5):
    """
    Retry a function upon failure.

    Args:
        func (function): The function to retry.
        max_retries (int): Maximum number of retries before failing.
        delay (int): Delay between retries in seconds.

    Returns:
        The return value of the function, or None if retries are exhausted.
    """
    retries = 0
    while retries < max_retries:
        try:
            result = func()
            logging.info(f"Function executed successfully: {func.__name__}")
            return result
        except Exception as e:
            retries += 1
            logging.error(f"Error executing {func.__name__}: {e}. Retrying {retries}/{max_retries}...")
            time.sleep(delay)
    logging.error(f"Function {func.__name__} failed after {max_retries} retries.")
    return None
