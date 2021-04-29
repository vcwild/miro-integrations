from typing import Dict
from httpx import Response
from miro.exceptions import (
	InvalidCredentialsException,
	InsufficientPermissions,
	ObjectNotFoundException,
	MiroException,
	UnexpectedResponseException
)

def handle_json(response: Response) -> Dict:
	if is_2xx_status_code(response.status_code):
		return response.json()

	if response.status_code == 401:
		raise InvalidCredentialsException(response.status_code)

	if response.status_code == 403:
		raise InsufficientPermissions(response.status_code)

	if response.status_code == 404:
		raise ObjectNotFoundException(response.status_code)

	if is_5xx_status_code(response.status_code):
		raise MiroException(response.status_code)

	raise UnexpectedResponseException(response.status_code)

def is_2xx_status_code(status_code: int) -> bool:
	return str(status_code).startswith('2')

def is_5xx_status_code(status_code: int) -> bool:
	return str(status_code).startswith('5')
