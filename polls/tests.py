from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from polls.apiviews import PollViewSet, QuestionViewSet, AnswerViewSet, VoteViewSet


class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'

    def test_users_unable_to_create_polls(self):
        self.factory.post(self.uri)
        self.assertEqual(1, 0)

    def tests_users_able_to_access_list_of_polls(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        print(self.client.defaults.keys())
        self.assertEqual(
            response.status_code, 200,
            msg=f'Expected Response Code 200, received {response.status_code} instead.'
        )

    def test_users_dont_see_outdated_polls(self):
        self.assertEqual(1, 0)

    def test_superuser_able_to_create_polls(self):
        self.assertEqual(1, 0)


class TestQuestion(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = QuestionViewSet.as_view({'get': 'list'})
        self.uri = '/questions/'

    def test_list(self):
        self.assertEqual(1, 0)

    def test_users_unable_to_create_questions(self):
        self.assertEqual(1, 0)

    def tests_users_able_to_access_list_of_questions(self):
        self.assertEqual(1, 0)

    def test_superuser_able_to_create_questions(self):
        self.assertEqual(1, 0)


class TestAnswer(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = AnswerViewSet.as_view({'get': 'list'})
        self.uri = '/answers/'

    def test_list(self):
        self.assertEqual(1, 0)

    def test_users_unable_to_create_answers(self):
        self.assertEqual(1, 0)

    def tests_users_able_to_access_list_of_answers(self):
        self.assertEqual(1, 0)

    def test_superuser_able_to_create_answers(self):
        self.assertEqual(1, 0)


class TestVote(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = VoteViewSet.as_view({'get': 'list'})
        self.uri = '/votes/'

    def test_list(self):
        self.assertEqual(1, 0)

    def test_users_can_vote_anonymously(self):
        self.assertEqual(1, 0)

    def test_users_unable_to_change_votes_they_dont_own(self):
        self.assertEqual(1, 0)
