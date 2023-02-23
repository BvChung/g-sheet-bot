import os
from dotenv import load_dotenv
load_dotenv()

token: str = os.getenv('TOKEN')
guildId: int = int(os.getenv('MY_GUILD'))
test_channel: int = int(os.getenv('TEST_CHANNEL'))