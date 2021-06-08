from typing import Dict
from env import SLACK_WEBHOOK_URL
import httpx
import json

def post_message(body: dict) -> Dict:
	if (body):
		json_serialized = json.dumps(body)
		response = httpx.post(
			url=SLACK_WEBHOOK_URL,
			data=json_serialized,
			content="application/json")
		return response
	return False
