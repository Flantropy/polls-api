from .apiviews import(
    PollViewSet,
    QuestionViewSet,
    AnswerViewSet,
    VoteViewSet,
)
from rest_framework_extensions.routers import ExtendedDefaultRouter


# /polls/<int:pk>/questions/<int:pk>/answers/<int:pk>/votes/<int:pk>/
router = ExtendedDefaultRouter()
(
    router.register(r'polls', PollViewSet, basename='polls')
          .register(r'questions',
                    QuestionViewSet,
                    basename='polls-question',
                    parents_query_lookups=['poll_id'])
          .register(r'answers',
                    AnswerViewSet,
                    basename='polls-questions-answer',
                    parents_query_lookups=['question__poll_id', 'question_id'])
          .register(r'votes',
                    VoteViewSet,
                    basename='polls-questions-answers-vote',
                    parents_query_lookups=['answer__question__poll_id',
                                           'answer__question',
                                           'answer'])
)

urlpatterns = router.urls
