from miro.helpers import handle_json
import pytest
from httpx import Response
from miro.exceptions import (
	InvalidCredentialsException,
	InsufficientPermissions,
	ObjectNotFoundException,
	MiroException,
	UnexpectedResponseException
)

def test_handle_json_should_return_dict_if_status_code_2xx():
	param = Response(
		status_code=200,
		json={'hello': 'test'}
	)
	response = handle_json(param)
	assert response == {'hello': 'test'}

def test_handle_json_should_raise_invalid_credentials_error():
	response = Response(
		status_code=401,
		json={'hello': 'test'}
	)
	with pytest.raises(InvalidCredentialsException):
		handle_json(response)

def test_handle_json_should_raise_insufficient_permissions_error():
	response = Response(
		status_code=403,
		json={'hello': 'test'}
	)
	with pytest.raises(InsufficientPermissions):
		handle_json(response)

def test_handle_json_should_raise_obj_not_found_error():
	response = Response(
		status_code=404,
		json={'hello': 'test'}
	)
	with pytest.raises(ObjectNotFoundException):
		handle_json(response)

def test_handle_json_should_raise_miro_exception():
	response = Response(
		status_code=500,
		json={'hello': 'test'}
	)
	with pytest.raises(MiroException):
		handle_json(response)

def test_handle_json_should_raise_unexpected_response_exception():
	response = Response(
		status_code=1111,
		json={'hello': 'test'}
	)
	with pytest.raises(UnexpectedResponseException):
		handle_json(response)
