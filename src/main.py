from miro.client import Client
from env import (MIRO_AUTH_TOKEN, BOARD_ID)
from services.users import get_user_activity, get_user_activity_by_widget_type
from view.user_activity import show_user_activity
from handlers.messages import post_message

TIMER = 60

client = Client(
	base_url="https://api.miro.com",
	auth_token=MIRO_AUTH_TOKEN,
)

# ---- Routine 0

board = client.list_all_widgets(BOARD_ID)

user_activity = get_user_activity(
	client=client,
	board_id=BOARD_ID,
	from_minutes=TIMER,
)

message = "`{}` realizou `{}` atividades nos boards nos últimos `{}` minutos."

body = show_user_activity(
	user_activity=user_activity,
	from_minutes=TIMER,
	message=message
)

response = post_message(body)

# ---- Routine 1

user_activity = get_user_activity_by_widget_type(
	client=client,
	board_id=BOARD_ID,
	from_minutes=TIMER,
)

message = "`{}` criou `{}` post-its nos boards nos últimos `{}` minutos."

body = show_user_activity(
	user_activity=user_activity,
	from_minutes=TIMER,
	message=message
)

response = post_message(body)
