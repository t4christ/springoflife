from django.test import TestCase
from comments.models import Comment
from django.utils import timezone
from django.urls import reverse
from accounts.models import MyUser
from comments.views import comment_thread
from django.urls import reverse



# models test
class CommentTest(TestCase):

    def create_comment(self):
            comment=Comment(name='temitayo',content="This is a comment from temitayo",accept_terms=True)
            return comment

    def test_user_creation(self):
        w = self.create_comment()
        self.assertTrue(isinstance(w, Comment))
        self.assertTrue(w.__str__(), '%s'%w.content)


    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Comment(name='temitayo',content="This is a comment from temitayo",accept_terms=True)



    def test_name_label(self):
        comment_w=Comment.objects.get(name='temitayo')
        field_label = comment_w._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_content_label(self):
        comment_w=Comment.objects.get(name='temitayo')
        field_label = comment_w._meta.get_field('content').verbose_name
        self.assertEquals(field_label,'content')







class CommentListViewTest(TestCase):

           
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/comments/1/') 
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('comments:thread'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('comments:thread'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'comment_thread.html')
