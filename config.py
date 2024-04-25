import configparser
import logging
import os

# setup config
def load_config():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    open_api_key = config['KEY']['OPEN_API_KEY']

    os.environ["OPENAI_API_KEY"] = open_api_key

# setup logging
def setup_logging():
    logging.basicConfig(
        filename='app.log',  # Log to a file
        filemode='a',  # Append to the existing log file
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    # Log environment information (useful for debugging)
    logging.info('Logging initialized')
    logging.info(f"OPEN_API_KEY set to {os.getenv("OPEN_API_KEY")}")