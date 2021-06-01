from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from polls.apiviews import PollViewSet


class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200,
            msg=f'Expected Response Code 200, received {response.status_code} instead.'
        )
