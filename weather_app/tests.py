from django.test import TestCase, Client
from django.urls import reverse
from .models import SearchHistory

class WeatherAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.city_name = "Astana"

    def test_home_page_status_code(self):
        """Проверка, что главная страница загружается"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_with_city(self):
        """Проверка, что при вводе города страница загружается"""
        response = self.client.get(reverse('home'), {'city': self.city_name})
        # Обычно 200 OK (не 302), так как данные сразу отображаются
        self.assertEqual(response.status_code, 200)

    def test_api_city_stats(self):
        """Проверка API статистики"""
        SearchHistory.objects.create(city=self.city_name, count=3)
        response = self.client.get(reverse('api_city_stats'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # Проверяем, что хотя бы один элемент - наш город
        self.assertTrue(any(entry['city'] == self.city_name for entry in data))
