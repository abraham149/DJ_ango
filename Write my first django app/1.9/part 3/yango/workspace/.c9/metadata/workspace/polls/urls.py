{"filter":false,"title":"urls.py","tooltip":"/polls/urls.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":4,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["urlpatterns = [","    url(r'^$', views.index, name='index'),","]",""],"id":3},{"start":{"row":4,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["urlpatterns = [","    # ex: /polls/","    url(r'^$', views.index, name='index'),","    # ex: /polls/5/","    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),","    # ex: /polls/5/results/","    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),","    # ex: /polls/5/vote/","    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),","]"]}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["app_name = 'polls'",""],"id":5}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["",""],"id":6}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":59},"end":{"row":13,"column":59},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1536219693570,"hash":"2e89fd4b7fba23d504e8d62e185b950383244af3"}