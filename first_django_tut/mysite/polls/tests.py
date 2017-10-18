from django.test import TestCase
from .models import Question
from django.utils import timezone
import datetime
from django.urls import reverse



# Create your tests here.
class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days=14)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


    def test_was_published_recently_with_old_question(self):

        time = timezone.now() - datetime.timedelta(days=20)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    
    def test_was_published_recently_with_recent_question(self):

        time = timezone.now() - datetime.timedelta(days=.5)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
    
class QuestionDetailViewsTests(TestCase):

    def test_future_question(self):
        
        time = timezone.now() + datetime.timedelta(days=14)
        future_question = Question.objects.create(pub_date=time,question_text='sample_text')
        url = reverse('polls:detail', args=[future_question.pk])
        response = self.client.get(url)
        self.assertEqual(int(response.status_code), int(404))
