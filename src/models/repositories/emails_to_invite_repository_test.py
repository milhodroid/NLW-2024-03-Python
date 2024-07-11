import pytest
import uuid
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason='database interaction')
def test_register_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails_trips_infos = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'email': 'milho@email.com'
    }

    emails_to_invite_repository.register_email(emails_trips_infos)

@pytest.mark.skip(reason='database interaction')
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    print()
    print(emails)