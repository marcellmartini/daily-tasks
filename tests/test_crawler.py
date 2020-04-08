from unittest import TestCase

from tools.packtpub import crawler


class GetEbookTitleTest(TestCase):

    def test_get_free_ebook_title(self):
        # GIVEN
        url = 'https://www.packtpub.com/free-learning'
        xpath = '//*[@id="free-learning-dropin"]/div/div/div/div/div[2]/div[2]/h1'

        # WHEN
        ebook_title = crawler.get_free_ebook_title(url, xpath)

        # THEN
        self.assertEqual(ebook_title, 'Blockchain By Example')
