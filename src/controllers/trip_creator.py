from typing import Dict
import uuid

class TripCreator():
    def __init__(self, trip_repository, emails_repository) -> None:
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> Dict:
        try:
            emails = body.get('emails_to_invite')

            trip_id = str(uuid.uuid4())
            trip_infos = { **body, 'id': trip_id }

            self.__trip_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    self.__emails_repository.register_email({
                        'id': str(uuid.uuid4()),
                        'trip_id': trip_id,
                        'email': email,
                    })
            
            return {
                'body': { 'id': trip_id },
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
    