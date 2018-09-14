{"filter":false,"title":"tests.py","tooltip":"/polls/tests.py","undoManager":{"mark":21,"position":21,"stack":[[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":22,"column":73},"action":"insert","lines":["import datetime","","from django.utils import timezone","from django.test import TestCase","","from .models import Question","","","class QuestionMethodTests(TestCase):","","    def test_was_published_recently_with_future_question(self):","        \"\"\"","        was_published_recently() should return False for questions whose","        pub_date is in the future.","        \"\"\"","        time = timezone.now() + datetime.timedelta(days=30)","        future_question = Question(pub_date=time)","        self.assertEqual(future_question.was_published_recently(), False)"],"id":3}],[{"start":{"row":22,"column":73},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":23,"column":0},"end":{"row":23,"column":8},"action":"insert","lines":["        "]},{"start":{"row":23,"column":8},"end":{"row":24,"column":0},"action":"insert","lines":["",""]},{"start":{"row":24,"column":0},"end":{"row":24,"column":8},"action":"insert","lines":["        "]},{"start":{"row":24,"column":8},"end":{"row":25,"column":0},"action":"insert","lines":["",""]},{"start":{"row":25,"column":0},"end":{"row":25,"column":8},"action":"insert","lines":["        "]},{"start":{"row":25,"column":8},"end":{"row":26,"column":0},"action":"insert","lines":["",""]},{"start":{"row":26,"column":0},"end":{"row":26,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":8},"action":"remove","lines":["    "],"id":5},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":25,"column":4},"end":{"row":41,"column":68},"action":"insert","lines":["def test_was_published_recently_with_old_question(self):","    \"\"\"","    was_published_recently() should return False for questions whose","    pub_date is older than 1 day.","    \"\"\"","    time = timezone.now() - datetime.timedelta(days=30)","    old_question = Question(pub_date=time)","    self.assertEqual(old_question.was_published_recently(), False)","","def test_was_published_recently_with_recent_question(self):","    \"\"\"","    was_published_recently() should return True for questions whose","    pub_date is within the last day.","    \"\"\"","    time = timezone.now() - datetime.timedelta(hours=1)","    recent_question = Question(pub_date=time)","    self.assertEqual(recent_question.was_published_recently(), True)"],"id":6}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "],"id":7},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "],"id":8},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":8},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":24,"column":0},"end":{"row":24,"column":8},"action":"insert","lines":["        "]},{"start":{"row":24,"column":8},"end":{"row":25,"column":0},"action":"insert","lines":["",""]},{"start":{"row":25,"column":0},"end":{"row":25,"column":8},"action":"insert","lines":["        "]},{"start":{"row":25,"column":8},"end":{"row":26,"column":0},"action":"insert","lines":["",""]},{"start":{"row":26,"column":0},"end":{"row":26,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":36,"column":0},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"insert","lines":["",""]},{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""]},{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"insert","lines":["",""]},{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":50,"column":0},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":51,"column":0},"end":{"row":52,"column":0},"action":"insert","lines":["",""]},{"start":{"row":52,"column":0},"end":{"row":53,"column":0},"action":"insert","lines":["",""]},{"start":{"row":53,"column":0},"end":{"row":54,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["from django.core.urlresolvers import reverse",""],"id":12}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""]},{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":57,"column":0},"end":{"row":66,"column":0},"action":"insert","lines":["def create_question(question_text, days):","    \"\"\"","    Creates a question with the given `question_text` and published the","    given number of `days` offset to now (negative for questions published","    in the past, positive for questions that have yet to be published).","    \"\"\"","    time = timezone.now() + datetime.timedelta(days=days)","    return Question.objects.create(question_text=question_text, pub_date=time)","",""],"id":15}],[{"start":{"row":56,"column":0},"end":{"row":57,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":57,"column":0},"end":{"row":58,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":70,"column":0},"end":{"row":71,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":71,"column":0},"end":{"row":72,"column":0},"action":"insert","lines":["",""]},{"start":{"row":72,"column":0},"end":{"row":73,"column":0},"action":"insert","lines":["",""]},{"start":{"row":73,"column":0},"end":{"row":74,"column":0},"action":"insert","lines":["",""]},{"start":{"row":74,"column":0},"end":{"row":75,"column":0},"action":"insert","lines":["",""]},{"start":{"row":75,"column":0},"end":{"row":76,"column":0},"action":"insert","lines":["",""]},{"start":{"row":76,"column":0},"end":{"row":77,"column":0},"action":"insert","lines":["",""]},{"start":{"row":77,"column":0},"end":{"row":78,"column":0},"action":"insert","lines":["",""]},{"start":{"row":78,"column":0},"end":{"row":79,"column":0},"action":"insert","lines":["",""]},{"start":{"row":79,"column":0},"end":{"row":80,"column":0},"action":"insert","lines":["",""]},{"start":{"row":80,"column":0},"end":{"row":81,"column":0},"action":"insert","lines":["",""]},{"start":{"row":81,"column":0},"end":{"row":82,"column":0},"action":"insert","lines":["",""]},{"start":{"row":82,"column":0},"end":{"row":83,"column":0},"action":"insert","lines":["",""]},{"start":{"row":83,"column":0},"end":{"row":84,"column":0},"action":"insert","lines":["",""]},{"start":{"row":84,"column":0},"end":{"row":85,"column":0},"action":"insert","lines":["",""]},{"start":{"row":85,"column":0},"end":{"row":86,"column":0},"action":"insert","lines":["",""]},{"start":{"row":86,"column":0},"end":{"row":87,"column":0},"action":"insert","lines":["",""]},{"start":{"row":87,"column":0},"end":{"row":88,"column":0},"action":"insert","lines":["",""]},{"start":{"row":88,"column":0},"end":{"row":89,"column":0},"action":"insert","lines":["",""]},{"start":{"row":89,"column":0},"end":{"row":90,"column":0},"action":"insert","lines":["",""]},{"start":{"row":90,"column":0},"end":{"row":91,"column":0},"action":"insert","lines":["",""]},{"start":{"row":91,"column":0},"end":{"row":92,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":78,"column":0},"end":{"row":133,"column":9},"action":"insert","lines":["class QuestionViewTests(TestCase):","    def test_index_view_with_no_questions(self):","        \"\"\"","        If no questions exist, an appropriate message should be displayed.","        \"\"\"","        response = self.client.get(reverse('polls:index'))","        self.assertEqual(response.status_code, 200)","        self.assertContains(response, \"No polls are available.\")","        self.assertQuerysetEqual(response.context['latest_question_list'], [])","","    def test_index_view_with_a_past_question(self):","        \"\"\"","        Questions with a pub_date in the past should be displayed on the","        index page.","        \"\"\"","        create_question(question_text=\"Past question.\", days=-30)","        response = self.client.get(reverse('polls:index'))","        self.assertQuerysetEqual(","            response.context['latest_question_list'],","            ['<Question: Past question.>']","        )","","    def test_index_view_with_a_future_question(self):","        \"\"\"","        Questions with a pub_date in the future should not be displayed on","        the index page.","        \"\"\"","        create_question(question_text=\"Future question.\", days=30)","        response = self.client.get(reverse('polls:index'))","        self.assertContains(response, \"No polls are available.\")","        self.assertQuerysetEqual(response.context['latest_question_list'], [])","","    def test_index_view_with_future_question_and_past_question(self):","        \"\"\"","        Even if both past and future questions exist, only past questions","        should be displayed.","        \"\"\"","        create_question(question_text=\"Past question.\", days=-30)","        create_question(question_text=\"Future question.\", days=30)","        response = self.client.get(reverse('polls:index'))","        self.assertQuerysetEqual(","            response.context['latest_question_list'],","            ['<Question: Past question.>']","        )","","    def test_index_view_with_two_past_questions(self):","        \"\"\"","        The questions index page may display multiple questions.","        \"\"\"","        create_question(question_text=\"Past question 1.\", days=-30)","        create_question(question_text=\"Past question 2.\", days=-5)","        response = self.client.get(reverse('polls:index'))","        self.assertQuerysetEqual(","            response.context['latest_question_list'],","            ['<Question: Past question 2.>', '<Question: Past question 1.>']","        )"],"id":18}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":19}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["from django.core.urlresolvers import reverse",""],"id":20}],[{"start":{"row":140,"column":0},"end":{"row":159,"column":66},"action":"insert","lines":["class QuestionIndexDetailTests(TestCase):","    def test_detail_view_with_a_future_question(self):","        \"\"\"","        The detail view of a question with a pub_date in the future should","        return a 404 not found.","        \"\"\"","        future_question = create_question(question_text='Future question.', days=5)","        url = reverse('polls:detail', args=(future_question.id,))","        response = self.client.get(url)","        self.assertEqual(response.status_code, 404)","","    def test_detail_view_with_a_past_question(self):","        \"\"\"","        The detail view of a question with a pub_date in the past should","        display the question's text.","        \"\"\"","        past_question = create_question(question_text='Past Question.', days=-5)","        url = reverse('polls:detail', args=(past_question.id,))","        response = self.client.get(url)","        self.assertContains(response, past_question.question_text)"],"id":26}],[{"start":{"row":60,"column":0},"end":{"row":136,"column":0},"action":"remove","lines":["","def create_question(question_text, days):","    \"\"\"","    Creates a question with the given `question_text` and published the","    given number of `days` offset to now (negative for questions published","    in the past, positive for questions that have yet to be published).","    \"\"\"","    time = timezone.now() + datetime.timedelta(days=days)","    return Question.objects.create(question_text=question_text, pub_date=time)","","","","","","","","","","","","class QuestionViewTests(TestCase):","    def test_index_view_with_no_questions(self):","        \"\"\"","        If no questions exist, an appropriate message should be displayed.","        \"\"\"","        response = self.client.get(reverse('polls:index'))","        self.assertEqual(response.status_code, 200)","        self.assertContains(response, \"No polls are available.\")","        self.assertQuerysetEqual(response.context['latest_question_list'], [])","","    def test_index_view_with_a_past_question(self):","        \"\"\"","        Questions with a pub_date in the past should be displayed on the","        index page.","        \"\"\"","        create_question(question_text=\"Past question.\", days=-30)","        response = self.client.get(reverse('polls:index'))","        self.assertQuerysetEqual(","            response.context['latest_question_list'],","            ['<Question: Past question.>']","        )","","    def test_index_view_with_a_future_question(self):","        \"\"\"","        Questions with a pub_date in the future should not be displayed on","        the index page.","        \"\"\"","        create_question(question_text=\"Future question.\", days=30)","        response = self.client.get(reverse('polls:index'))","        self.assertContains(response, \"No polls are available.\")","        self.assertQuerysetEqual(response.context['latest_question_list'], [])","","    def test_index_view_with_future_question_and_past_question(self):","        \"\"\"","        Even if both past and future questions exist, only past questions","        should be displayed.","        \"\"\"","        create_question(question_text=\"Past question.\", days=-30)","        create_question(question_text=\"Future question.\", days=30)","        response = self.client.get(reverse('polls:index'))","        self.assertQuerysetEqual(","            response.context['latest_question_list'],","            ['<Question: Past question.>']","        )","","    def test_index_view_with_two_past_questions(self):","        \"\"\"","        The questions index page may display multiple questions.","        \"\"\"","        create_question(question_text=\"Past question 1.\", days=-30)","        create_question(question_text=\"Past question 2.\", days=-5)","        response = self.client.get(reverse('polls:index'))","        self.assertQuerysetEqual(","            response.context['latest_question_list'],","            ['<Question: Past question 2.>', '<Question: Past question 1.>']","        )",""],"id":27}],[{"start":{"row":61,"column":0},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":62,"column":0},"end":{"row":63,"column":0},"action":"insert","lines":["",""]},{"start":{"row":63,"column":0},"end":{"row":64,"column":0},"action":"insert","lines":["",""]},{"start":{"row":64,"column":0},"end":{"row":65,"column":0},"action":"insert","lines":["",""]},{"start":{"row":65,"column":0},"end":{"row":66,"column":0},"action":"insert","lines":["",""]},{"start":{"row":66,"column":0},"end":{"row":67,"column":0},"action":"insert","lines":["",""]},{"start":{"row":67,"column":0},"end":{"row":68,"column":0},"action":"insert","lines":["",""]},{"start":{"row":68,"column":0},"end":{"row":69,"column":0},"action":"insert","lines":["",""]},{"start":{"row":69,"column":0},"end":{"row":70,"column":0},"action":"insert","lines":["",""]},{"start":{"row":70,"column":0},"end":{"row":71,"column":0},"action":"insert","lines":["",""]},{"start":{"row":71,"column":0},"end":{"row":72,"column":0},"action":"insert","lines":["",""]},{"start":{"row":72,"column":0},"end":{"row":73,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":64,"column":0},"end":{"row":129,"column":9},"action":"insert","lines":["def create_question(question_text, days):","    \"\"\"","    Creates a question with the given `question_text` and published the","    given number of `days` offset to now (negative for questions published","    in the past, positive for questions that have yet to be published).","    \"\"\"","    time = timezone.now() + datetime.timedelta(days=days)","    return Question.objects.create(question_text=question_text, pub_date=time)","","","class QuestionViewTests(TestCase):","    def test_index_view_with_no_questions(self):","        \"\"\"","        If no questions exist, an appropriate message should be displayed.","        \"\"\"","        response = self.client.get(reverse('polls:index'))","        self.assertEqual(response.status_code, 200)","        self.assertContains(response, \"No polls are available.\")","        self.assertQuerysetEqual(response.context['latest_question_list'], [])","","    def test_index_view_with_a_past_question(self):","        \"\"\"","        Questions with a pub_date in the past should be displayed on the","        index page.","        \"\"\"","        create_question(question_text=\"Past question.\", days=-30)","        response = self.client.get(reverse('polls:index'))","        self.assertQuerysetEqual(","            response.context['latest_question_list'],","            ['<Question: Past question.>']","        )","","    def test_index_view_with_a_future_question(self):","        \"\"\"","        Questions with a pub_date in the future should not be displayed on","        the index page.","        \"\"\"","        create_question(question_text=\"Future question.\", days=30)","        response = self.client.get(reverse('polls:index'))","        self.assertContains(response, \"No polls are available.\")","        self.assertQuerysetEqual(response.context['latest_question_list'], [])","","    def test_index_view_with_future_question_and_past_question(self):","        \"\"\"","        Even if both past and future questions exist, only past questions","        should be displayed.","        \"\"\"","        create_question(question_text=\"Past question.\", days=-30)","        create_question(question_text=\"Future question.\", days=30)","        response = self.client.get(reverse('polls:index'))","        self.assertQuerysetEqual(","            response.context['latest_question_list'],","            ['<Question: Past question.>']","        )","","    def test_index_view_with_two_past_questions(self):","        \"\"\"","        The questions index page may display multiple questions.","        \"\"\"","        create_question(question_text=\"Past question 1.\", days=-30)","        create_question(question_text=\"Past question 2.\", days=-5)","        response = self.client.get(reverse('polls:index'))","        self.assertQuerysetEqual(","            response.context['latest_question_list'],","            ['<Question: Past question 2.>', '<Question: Past question 1.>']","        )"],"id":29}]]},"ace":{"folds":[],"scrolltop":952,"scrollleft":0,"selection":{"start":{"row":83,"column":0},"end":{"row":83,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":7,"state":"start","mode":"ace/mode/python"}},"timestamp":1536849396010,"hash":"9f4e631f069f8ca77fd999f82e5fc2e22b82d24b"}