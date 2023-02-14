import os
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('TOKEN')
test_channel = int(os.getenv('TEST_CHANNEL'))