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
    router.register('polls', PollViewSet, basename='polls')
          .register('questions',
                    QuestionViewSet,
                    basename='polls-question',
                    parents_query_lookups=['poll'])
          .register('answers',
                    AnswerViewSet,
                    basename='polls-question-answers',
                    parents_query_lookups=['question_id', 'question__poll'])
          .register('votes',
                    VoteViewSet,
                    basename='polls-question-answers-votes',
                    parents_query_lookups=['answer__question__poll', 'question__poll', 'answer'])
)

urlpatterns = router.urls
