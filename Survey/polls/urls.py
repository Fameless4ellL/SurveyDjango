from django.urls import path

from . import views, viewHtml

app_name = 'polls'
urlpatterns = [
    path('', viewHtml.index, name='index'),
    path('polls/<int:poll_id>/question/', viewHtml.detail, name='detail'),
    path('polls/<int:poll_id>/question/<int:question_id>', viewHtml.detail_of_details, name='detail_of_details'),
    path('polls/<int:question_id>/results/', viewHtml.results, name='results'),
    path('polls/<int:question_id>/vote/', viewHtml.vote, name='vote'),
    # rest api
    path('api/polls/', views.polls_view, name='polls_view'),
    path('api/polls/<int:poll_id>/', views.polls_detail_view, name='polls_detail_view'),
    path('api/polls/questions/', views.questions_view, name='questions_view'),
    path('api/polls/questions/<int:question_id>/', views.question_detail_view, name='question_detail_view'),
    path('api/polls/questions/<int:question_id>/choices/', views.choices_view, name='choices_view'),
    path('api/polls/questions/<int:question_id>/vote/', views.vote_view, name='vote_view'),
    path('api/polls/questions/<int:question_id>/result/', views.question_result_view, name='question_result_view')
]