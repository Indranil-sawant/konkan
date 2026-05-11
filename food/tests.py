from django.test import TestCase
from .models import Category, Tag, FoodItem
from users.models import Profile
from django.contrib.auth.models import User


class FoodModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile = Profile.objects.create(user=self.user, username='testuser')
        
        self.category = Category.objects.create(name='Seafood')
        self.tag = Tag.objects.create(name='Spicy')
        
        self.food_item = FoodItem.objects.create(
            name='Fish Curry',
            uploaded_by=self.profile,
            price=250.0,
            rating=4.5,
            description='Spicy Konkani fish curry',
            best_time_to_eat='Lunch'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Seafood')
        self.assertEqual(str(self.category), 'Seafood')

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, 'Spicy')
        self.assertEqual(str(self.tag), 'Spicy')

    def test_food_item_creation(self):
        self.assertEqual(self.food_item.name, 'Fish Curry')
        self.assertEqual(self.food_item.uploaded_by, self.profile)
        self.assertEqual(self.food_item.price, 250.0)
        self.assertEqual(self.food_item.rating, 4.5)
        self.assertEqual(self.food_item.description, 'Spicy Konkani fish curry')
        self.assertEqual(self.food_item.best_time_to_eat, 'Lunch')

    def test_food_item_str(self):
        self.assertEqual(str(self.food_item), 'Fish Curry')
