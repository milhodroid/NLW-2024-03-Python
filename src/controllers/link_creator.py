import uuid
from typing import Dict

class LinkCreator:
    def __init__(self, link_repository) -> None:
        self.__link_repository = link_repository

    def create(self, body, trip_id) -> Dict:
        try:
            link_id = str(uuid.uuid4())
            link_infos = {
                'id': link_id,
                'trip_id': trip_id,
                'link': body['url'],
                'title': body['title']
            }

            self.__link_repository.register_link(link_infos)
            return {
                'body': {
                    'linkId': link_id
                },
                'status_code': 201
            }
        except Exception as exception:
            return {
                'body': {
                    'error': 'Bad Request',
                    'message': str(exception) 
                },
                'status_code': 400
            }
    