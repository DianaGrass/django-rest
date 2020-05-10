from django.test import TestCase, Client
from .models import Book, Comment
from django.contrib.auth.models import User


# Create your tests here.
class AppBookTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            id=1,
            username="test name"
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
