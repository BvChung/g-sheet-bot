import os
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('TOKEN')
guildId = int(os.getenv('MY_GUILD'))
test_channel = int(os.getenv('TEST_CHANNEL'))