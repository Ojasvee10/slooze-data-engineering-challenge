import time
import random
from datetime import datetime

def polite_delay():
    time.sleep(random.uniform(2, 4))

def current_timestamp():
    return datetime.utcnow().isoformat()