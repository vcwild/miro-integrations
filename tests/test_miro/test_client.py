
import os
import dotenv
from miro.client import Client
# from tests.env_vars import (
# 	MIRO_AUTH_TOKEN, BOARD_ID, TEAM_ID, USER_ID
# )

# set env
dotenv.load_dotenv()
MIRO_AUTH_TOKEN = os.environ.get("MIRO_AUTH_TOKEN")
BOARD_ID = os.environ['BOARD_ID']
USER_ID = os.environ['USER_ID']
TEAM_ID = os.environ['TEAM_ID']

client = Client(
	"https://api.miro.com",
	MIRO_AUTH_TOKEN
)

def check_if_subset(expected, response):
	return set(expected).issubset(set(response))

# tests
def test_get_widgets_should_return_dict():
	response = client.get_widgets(BOARD_ID)
	expected_response = {
		'type': 'widget'
	}
	assert type(response) == dict
	assert check_if_subset(expected_response, response)

def test_get_board_should_return_board():
	response = client.get_board(BOARD_ID)
	expected_response = {
		'type': 'board'
	}
	assert check_if_subset(expected_response, response)

def test_get_board_members_should_return_board_members():
	response = client.get_board_members(BOARD_ID)
	expected_response = {
		'type': 'board'
	}
	assert check_if_subset(expected_response, response)


# def test_get_logs_should_return_dict():
#	response = client.get_logs()

#	assert response == "banana"

def test_get_team_should_return_dict():
	response = client.get_team(TEAM_ID)
	assert type(response) == dict

def test_get_team_boards_should_return_board():
	response = client.get_team_boards(TEAM_ID)
	expected_response = {
		'type': 'board'
	}
	assert check_if_subset(expected_response, response)

def test_get_user_should_return_user():
	response = client.get_user(USER_ID)
	expected_response = {
		'company',
		'createdAt',
		'email'
	}
	assert check_if_subset(expected_response, response)
