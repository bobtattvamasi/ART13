from django.test import TestCase
from .models import Artist


class ArtistModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Artist.objects.create(name='Van Gogh', nationality='Dutch', birth_year=1853, death_year=1890, biography='Artist biography')

    def test_name_label(self):
        artist = Artist.objects.get(id=1)
        field_label = artist._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_nationality_label(self):
        artist = Artist.objects.get(id=1)
        field_label = artist._meta.get_field('nationality').verbose_name
        self.assertEqual(field_label, 'nationality')

    def test_biography_max_length(self):
        artist = Artist.objects.get(id=1)
        max_length = artist._meta.get_field('biography').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_name_comma_nationality(self):
        artist = Artist.objects.get(id=1)
        expected_object_name = f'{artist.name}, {artist.nationality}'
        self.assertEqual(expected_object_name, str(artist))