from django.test import TestCase, Client
from .models import Book, Comment
from django.contrib.auth.models import User


class AppBookTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            id=1,
            username="name"
        )
        self.user.set_password("1234")
        self.user.save()

        self.client = Client()

        self.book = Book.objects.create(
            title="test text title",
            text="test text title",
        )
        self.book.save()

        self.comment1 = Comment.objects.create(
            text="test text title",
            comment_book_id=self.book.id,
        )
        self.comment1.save()

        self.comment2 = Comment.objects.create(
            text="test text title",
            comment_book_id=self.book.id,
        )
        self.comment2.save()

    def test_one(self):
        book = Book.objects.get(id=1)
        comment = Comment.objects.filter(comment_book=book)
        self.assertCountEqual(book.comment.all(), comment)

    def test_delete_book(self):
        book = Book.objects.get(id=1).delete()
        comment = Comment.objects.all()
        self.assertCountEqual(comment, [])

    def test_login(self):
        res = self.client.login(
            username="name",
            password="1234"
        )
        self.assertEqual(res, True)

    def test_check_code200(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_check_code404(self):
        res = self.client.get('/das_url/')
        self.assertEqual(res.status_code, 404)
