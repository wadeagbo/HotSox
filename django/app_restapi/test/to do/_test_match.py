from unittest import mock
from django.test import TestCase
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse

from app_users.models import User, MessageMail, MessageChat


from .inital_test_setup import (
    TEST_USER1,
    TEST_USER2,
    token,
)

from rest_framework.test import APIClient


class TestUser(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_superuser(**TEST_USER1)
        self.user2 = User.objects.create_user(**TEST_USER2)

    def setup_match_records():
        with Session(engine) as db:
            user1 = (
                db.query(User).filter(User.username == TEST_USER1["username"]).first()
            )
            user2 = (
                db.query(User).filter(User.username == TEST_USER2["username"]).first()
            )

            match1 = UserMatch(
                user_id=user1.id,
                other_id=user2.id,
                unmatched=False,
                chatroom_uuid=uuid.uuid4(),
            )
            db.add(match1)
            db.commit()
            db.refresh(match1)

    def test_all_matches(test_db_setup):
        # setup database
        setup_match_records()

        response = client.get(
            PREFIX + "/user/matches",
            headers=token(username="admin", password="admin"),
        )
        assert response.status_code == 200
        assert isinstance(response.json()["items"], list)
        assert response.json()["items"][0]["id"] == 1
        assert response.json()["items"][0]["matched_with"] == {
            "email": "testuser2@testuser2.com",
            "username": "testuser2",
        }
        assert response.json()["items"][0]["unmatched"] == False
        assert len(response.json()["items"][0]["chatroom_uuid"]) == 36

    def test_specific_match(test_db_setup):
        # setup database
        setup_match_records()

        # check from first user perspective
        response = client.get(
            PREFIX + "/user/match/1",
            headers=token(username="admin", password="admin"),
        )
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert response.json()["id"] == 1
        assert response.json()["matched_with"] == {
            "email": "testuser2@testuser2.com",
            "username": "testuser2",
        }
        assert response.json()["unmatched"] == False
        assert len(response.json()["chatroom_uuid"]) == 36

        # check from second user perspective
        response = client.get(
            PREFIX + "/user/match/1",
            headers=token(username="testuser2", password="testuser2"),
        )
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert response.json()["id"] == 1
        assert response.json()["matched_with"] == {
            "email": "admin@admin.com",
            "username": "admin",
        }
        assert response.json()["unmatched"] == False
        assert len(response.json()["chatroom_uuid"]) == 36

    def test_specific_match(test_db_setup):
        # setup database
        setup_match_records()

        # check from first user perspective
        response = client.request(
            "DELETE",
            f"{PREFIX}/user/match/1",
            headers=token("admin", "admin"),
        )
        assert response.status_code == 204

        # check if match was set to unmatched successfully
        response = client.get(
            PREFIX + "/user/match/1",
            headers=token(username="admin", password="admin"),
        )
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert response.json()["id"] == 1
        assert response.json()["matched_with"] == {
            "email": "testuser2@testuser2.com",
            "username": "testuser2",
        }
        assert response.json()["unmatched"] == True
        assert len(response.json()["chatroom_uuid"]) == 36

        # setup database
        setup_match_records()

        # check from second user perspective
        response = client.request(
            "DELETE",
            f"{PREFIX}/user/match/2",
            headers=token("testuser2", "testuser2"),
        )

        assert response.status_code == 204

        # check if match was set to unmatched successfully
        response = client.get(
            PREFIX + "/user/match/2",
            headers=token(username="testuser2", password="testuser2"),
        )
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert response.json()["id"] == 2
        assert response.json()["matched_with"] == {
            "email": "admin@admin.com",
            "username": "admin",
        }
        assert response.json()["unmatched"] == True
        assert len(response.json()["chatroom_uuid"]) == 36
