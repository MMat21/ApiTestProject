import logging
import os
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_dir="logs"
os.makedirs("logs", exist_ok=True)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(os.path.join(log_dir,"test.log"),encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)