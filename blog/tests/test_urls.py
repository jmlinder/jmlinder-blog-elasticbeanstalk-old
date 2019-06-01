from django.urls import resolve, reverse


class TestUrls:
    def test_post_list(self):
        path = reverse('post_list')
        assert resolve(path).view_name == 'post_list'

    def test_post_detail(self):
        path = reverse('post_detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'post_detail'

    def test_post_new(self):
        path = reverse('post_new')
        assert resolve(path).view_name == 'post_new'

    def test_post_edit(self):
        path = reverse('post_edit', kwargs={'pk': 1})
        assert resolve(path).view_name == 'post_edit'

    def test_post_draft_list(self):
        path = reverse('post_draft_list')
        assert resolve(path).view_name == 'post_draft_list'

    def test_post_publish(self):
        path = reverse('post_publish', kwargs={'pk': 1})
        assert resolve(path).view_name == 'post_publish'

    def test_post_remove(self):
        path = reverse('post_remove', kwargs={'pk': 1})
        assert resolve(path).view_name == 'post_remove'

    def test_projects(self):
        path = reverse('projects')
        assert resolve(path).view_name == 'projects'

    def test_about(self):
        path = reverse('about')
        assert resolve(path).view_name == 'about'
