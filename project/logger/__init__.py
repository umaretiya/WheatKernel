import logging
from datetime import datetime 
import pandas as pd
import os


LOG_DIR = "logs_data"

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

def get_log_file_name():
    return f"log_{get_current_time_stamp}.log"

LOG_FILE_NAME = get_log_file_name()

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

fmtstr = "[%(asctime)s]^; %(levelname)s^; %(filename)s^; %(funcName)s()^; Line:%(lineno)d^; %(message)s"
datestr = "%m/%d/%Y %I:%M:%S %p"

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    filemode="w",
    format=fmtstr,
    datefmt=datestr,
    )


def get_log_dataframe(file_path):
    data = []
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))
    log_df = pd.DataFrame(data)
    columns = ["Time stamp","Log Level","file name","function name","line number","message"]
    log_df.columns = columns
    
    log_df['log_message'] = log_df['Time stamp'].astype(str) + ":$" + log_df['message']
    return log_df[["log_message"]]
    