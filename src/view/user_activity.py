def show_user_activity(
	user_activity,
	from_minutes,
	message="`{}` `{}` `{}`."):

	if user_activity == {}:
		raise TypeError("No user activity recorded")

	messages = ""
	for user, activities in user_activity.items():
		message = message.format(user, activities, from_minutes)
		messages += "\n"
		messages += message

	body = {
		'text': messages
	}

	return body

def show_user_reports(user_reports, from_minutes):
	messages = ""
	for user, values in user_reports.items():
		str_values = ", ".join([str(item) for item in values])
		message = "**{}** publicou há {} minutos: {}".format(user, from_minutes, str_values)
		messages += message

	body = {
		'text': messages
	}

	return body
