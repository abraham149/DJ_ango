{"filter":false,"title":"models.py","tooltip":"/polls/models.py","undoManager":{"mark":23,"position":23,"stack":[[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":15,"column":42},"action":"insert","lines":["class Question(models.Model):","    question_text = models.CharField(max_length=200)","    pub_date = models.DateTimeField('date published')","","","class Choice(models.Model):","    question = models.ForeignKey(Question, on_delete=models.CASCADE)","    choice_text = models.CharField(max_length=200)","    votes = models.IntegerField(default=0)"],"id":3}],[{"start":{"row":15,"column":42},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":4},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":4},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "],"id":5},{"start":{"row":17,"column":4},"end":{"row":18,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":17,"column":4},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "],"id":7}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["S"],"id":8},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["H"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["O"]}],[{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"remove","lines":["O"],"id":9},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"remove","lines":["H"]},{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"remove","lines":["S"]}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":6,"column":0},"end":{"row":8,"column":68},"action":"insert","lines":["from django.utils.encoding import python_2_unicode_compatible","","@python_2_unicode_compatible  # only if you need to support Python 2"],"id":12}],[{"start":{"row":8,"column":68},"end":{"row":9,"column":0},"action":"remove","lines":["",""],"id":13}],[{"start":{"row":11,"column":53},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":4},"end":{"row":13,"column":33},"action":"insert","lines":["def __str__(self):","        return self.question_text"],"id":15}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":68},"action":"insert","lines":["@python_2_unicode_compatible  # only if you need to support Python 2"],"id":16}],[{"start":{"row":20,"column":4},"end":{"row":22,"column":0},"action":"insert","lines":["def __str__(self):","        return self.choice_text",""],"id":17}],[{"start":{"row":22,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":23,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["",""]},{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""]},{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":19}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["import datetime",""],"id":20}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":33},"action":"insert","lines":["from django.utils import timezone"],"id":22}],[{"start":{"row":17,"column":33},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]},{"start":{"row":18,"column":8},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":19,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "],"id":24}],[{"start":{"row":19,"column":4},"end":{"row":20,"column":75},"action":"insert","lines":["def was_published_recently(self):","        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)"],"id":25}],[{"start":{"row":20,"column":75},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":21,"column":0},"end":{"row":21,"column":8},"action":"insert","lines":["        "]},{"start":{"row":21,"column":8},"end":{"row":22,"column":0},"action":"insert","lines":["",""]},{"start":{"row":22,"column":0},"end":{"row":22,"column":8},"action":"insert","lines":["        "]},{"start":{"row":22,"column":8},"end":{"row":23,"column":0},"action":"insert","lines":["",""]},{"start":{"row":23,"column":0},"end":{"row":23,"column":8},"action":"insert","lines":["        "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":18,"column":8},"end":{"row":18,"column":8},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1536177593252,"hash":"38d7f1f998a30a58b1a25eeaddb286424c5edbe0"}