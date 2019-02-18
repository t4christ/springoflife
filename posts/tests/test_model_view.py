from django.test import TestCase
from taptap.models import Taptap
from django.utils import timezone
from django.urls import reverse
from accounts.models import MyUser
from posts.models import Post
# from post.views import 

# models test
class PostTest(TestCase):

    def create_post(self):
            user=MyUser(username='temitayo',password='texplode',phone_number='07063419292',first_name='akanbi',last_name='bakare',email='bakakan@gmail.com')
            return Post(user=user, slug='marshall-edikan-faith', title='marshaledikanfaith',content='This is a post for carrying out an assessment')

    def test_post_creation(self):
        w = self.create_post()
        self.assertTrue(isinstance(w, Post))
        self.assertEqual(w.__str__(), '%s'%w.title)

class PostListViewTest(TestCase):

    @classmethod
    def setUpTestViewData(cls):
        create_taptap()
        number_of_post = 15
        for post_num in range(number_of_posts):
            Post(user=user"%s"%post_num, slug='marshall-edikan-faith%s'%post_num, title='marshaledikanfaith%s'%post_num,content='This is a post for carrying out an assessment%s'%post_num)
           
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/play_tap_tap/understand/') 
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('taptap:understand_tap'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('taptap:understand_tap'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'taptap/understand.html')

