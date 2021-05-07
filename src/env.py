import dotenv
import os
import httpx

dotenv.load_dotenv()

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
MIRO_AUTH_TOKEN = os.environ["MIRO_AUTH_TOKEN"]
BOARD_ID = os.environ['BOARD_ID']
USER_ID = os.environ['USER_ID']
TEAM_ID = os.environ['TEAM_ID']

SLACK_WEBHOOK_URL= os.environ['SLACK_WEBHOOK_URL']