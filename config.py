import configparser
import logging
import os

# setup config
def load_config():
    """
       Loads OpenAI API key from 'conf.ini' and sets it as an environment variable.

       Raises:
           FileNotFoundError: If 'conf.ini' is missing.
           KeyError: If 'OPEN_API_KEY' is not found in 'conf.ini'.
       """
    config = configparser.ConfigParser()
    config.read('conf.ini')
    open_api_key = config['KEY']['OPEN_API_KEY']

    os.environ["OPENAI_API_KEY"] = open_api_key

# setup logging
def setup_logging():
    """
        Configures logging to a file and logs initialization and environment info.

        Logs initialization status and the value of OPEN_API_KEY environment variable.
        """
    logging.basicConfig(
        filename='app.log',  # Log to a file
        filemode='a',  # Append to the existing log file
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    # Log environment information (useful for debugging)
    logging.info('Logging initialized')
    logging.info(f"OPEN_API_KEY set to {os.getenv("OPEN_API_KEY")}")