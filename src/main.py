from pprint import pprint
from miro.client import Client
from env import (MIRO_AUTH_TOKEN, BOARD_ID, TEAM_ID)

client = Client(
	"https://api.miro.com",
	MIRO_AUTH_TOKEN,
)

# board = client.get_board_members(BOARD_ID)

board = client.list_all_team_members(TEAM_ID)
