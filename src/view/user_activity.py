def show_user_activity(
	user_activity,
	from_minutes,
	message="`{}` realizou `{}` atividades nos boards nos últimos `{}` minutos."):

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
