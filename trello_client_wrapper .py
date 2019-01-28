
from trello import TrelloClient
import requests
import json
import sys


class TrelloWrapper(object):
    """
    trello_wrapper using TrelloClient
    """
    def __init__(self):

        self.TRELLO_API_KEY = None
        self.TRELLO_SECRET_KEY = None
        self.TRELLO_TOKEN_KEY = None

        self._load_trello_keys()
        # create trello client object
        self.client = TrelloClient(
            api_key=self.TRELLO_API_KEY,
            api_secret=self.TRELLO_SECRET_KEY,
            token=self.TRELLO_TOKEN_KEY,
            token_secret='your-oauth-token-secret'
        )

    def _load_trello_keys(self):
        """
        load trello keys from file: token.json
        :return: none
        """
        try:
            with open('token.json') as f:
                trello_keys = json.load(f)

            self.TRELLO_API_KEY = trello_keys["TRELLO_API_KEY"]
            self.TRELLO_SECRET_KEY = trello_keys["TRELLO_SECRET_KEY"]
            self.TRELLO_TOKEN_KEY = trello_keys["TRELLO_TOKEN_KEY"]
        except (FileNotFoundError, IOError):
            print("Error: Wrong file or file path")
            sys.exit(1)
        except:
            print("Error: Could not read Trello Keys from file")
            sys.exit(1)

    def _get_queryparameters_keys(self):
        """
        create dict with key and token value for rest api calls
        :return: dict value with trello api keys
        """
        return {"key": self.TRELLO_API_KEY, "token": self.TRELLO_TOKEN_KEY}

    def _get_boards_list(self):
        """
        return list of all boards
        :return: list of boards
        """
        return self.client.list_boards()

    def _find_board_id_by_name(self,board_name):
        """
        return board id by given name
        :param board_name: 
        :return: board id
        """
        all_boards_data = self.client.list_boards()
        for board_data in all_boards_data:
            if board_data.name == board_name:
                return board_data.id

    def _get_lists(self, trello_board_id):
        """
        get all lists by give board_id
        :param trello_board_id: 
        :return: lists_of_list
        """

        api_url = "https://api.trello.com/1/boards/" + trello_board_id + "/lists"
        query_string = {"cards": "none", "card_fields": "all", "filter": "open", "fields": "all"}
        query_string.update(self._get_queryparameters_keys())
        response_data = requests.request("GET", api_url, params=query_string)
        all_lists_data = json.loads(response_data.text)
        return all_lists_data

    def _find_list_id_by_name(self, trello_board_id, list_name):
        """
        return list id by given name and board_id
        :param trello_board_id: 
        :param list_name: 
        :return: list id
        """
        all_lists_data = self._get_lists(trello_board_id)
        for list_data in all_lists_data:
            if list_data['name'] == list_name:
                return list_data['id']

    def _create_card(self, board_name, list_name):
        """create card by board name and list name.

        Args:
            board_name: board name to look for.
            list_name: list name to look for.

        Returns:
            card_id of the created card.

        """
        trello_board_id = self._find_board_id_by_name(board_name)
        trello_list_id = self._find_list_id_by_name(trello_board_id, list_name)
        api_url = "https://api.trello.com/1/cards"
        query_string = {"idList": trello_list_id, "name": "bug1", "desc": "this card add auto", "keepFromSource": "all"}
        query_string.update(self._get_queryparameters_keys())
        response_data = requests.request("POST", api_url, params=query_string)
        card_data = json.loads(response_data.text)
        return card_data['id']


def main():
    print("program start running")
    if len(sys.argv) > 1:
        if sys.argv[1] == '-help':
            print("How To:")

    trello = TrelloWrapper()
    trello._create_card('MatchmakerApp', 'Tasks')

    print("program end")

if __name__ == "__main__":
    main()
