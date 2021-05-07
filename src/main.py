import httpx
from miro.client import Client
from env import (MIRO_AUTH_TOKEN, BOARD_ID, SLACK_WEBHOOK_URL)
from miro.helpers import handle_json
from services.users import get_user_activity
import json


client = Client(
	base_url="https://api.miro.com",
	auth_token=MIRO_AUTH_TOKEN,
)

time_mins = 3000000


user_activity = get_user_activity(
	client=client,
	board_id=BOARD_ID,
	from_minutes=time_mins
)

assert user_activity != {}, "No user activity recorded"

messages = ""

for user, activities in user_activity.items():
	message = "`{}` realizou `{}` atividades nos boards da Fractal nos últimos `{}` minutos."
	message = message.format(user, activities, time_mins)
	messages += "\n"
	messages += message

body = {
	'text': messages
}

json_serialized = json.dumps(body)

r = httpx.post(url=SLACK_WEBHOOK_URL, data=json_serialized, content="application/json")
