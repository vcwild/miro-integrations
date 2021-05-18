from itertools import groupby
from filters import filter_keys
from env import (BOARD_ID, MIRO_AUTH_TOKEN)
from services.users import (
	get_user_activity,
	get_user_activity_by_widget_type,
	get_user_data_with_text_fields,
	get_user_reports
)
from view.user_activity import (show_user_activity, show_user_reports)
from handlers.messages import post_message
from miro.client import Client

TIMER = 3200

client = Client(
	base_url="https://api.miro.com",
	auth_token=MIRO_AUTH_TOKEN
)

user_activity = get_user_data_with_text_fields(
	client=client,
	board_id=BOARD_ID,
	from_minutes=TIMER
)

user_reports = get_user_reports(user_activity)

body = show_user_reports(user_reports, TIMER)

response = post_message(body)

# # ---- Routine 0

# user_activity = get_user_activity(
# 	client=client,
# 	board_id=BOARD_ID,
# 	from_minutes=TIMER,
# )

# message = "`{}` realizou `{}` atividades nos boards nos últimos `{}` minutos."

# body = show_user_activity(
# 	user_activity=user_activity,
# 	from_minutes=TIMER,
# 	message=message
# )

# response = post_message(body)

# # ---- Routine 1

# user_activity = get_user_activity_by_widget_type(
# 	client=client,
# 	board_id=BOARD_ID,
# 	from_minutes=TIMER,
# )

# message = "`{}` criou `{}` post-its nos boards nos últimos `{}` minutos."

# body = show_user_activity(
# 	user_activity=user_activity,
# 	from_minutes=TIMER,
# 	message=message
# )

# response = post_message(body)
