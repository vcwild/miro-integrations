import dotenv
import os

dotenv.load_dotenv()

MIRO_AUTH_TOKEN = os.environ.get("MIRO_AUTH_TOKEN")
BOARD_ID = os.environ['BOARD_ID']
USER_ID = os.environ['USER_ID']
TEAM_ID = os.environ['TEAM_ID']
