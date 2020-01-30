from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Mineral


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral_1 = Mineral.objects.create(
            name="Abernathyite",
            image_caption="Pale yellow abernathyite crystals and green...",
            color="Green",
            group="Arsenates"
        )
        self.mineral_2 = Mineral.objects.create(
            name="test name",
            image_caption="test caption",
            group="Silicates"
        )
        self.color = 'White'

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_1, resp.context['match'])
        self.assertIn(self.mineral_2, resp.context['match'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral_1.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(
            reverse('minerals:detail', kwargs={'pk': self.mineral_1.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_1.name, resp.context['mineral'].values())
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')

    def test_mineral_by_letter(self):
        resp = self.client.get(
            reverse('minerals:letterlist', kwargs={'letter': 'a'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_1, resp.context['match'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')

    def test_mineral_by_group(self):
        resp = self.client.get(
            reverse('minerals:group', kwargs={'group': 'Arsenates'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_1, resp.context['match'])
        self.assertNotIn(self.mineral_2, resp.context['match'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')

    def test_search(self):
        resp = self.client.get(reverse('minerals:search'), {'q': 'Green'})
        resp2 = self.client.get(reverse('minerals:search'), {'q': 'test'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_1, resp.context['results'])
        self.assertTemplateUsed(resp, 'minerals/mineral_search.html')
        self.assertEqual(resp2.status_code, 200)
        self.assertIn(self.mineral_2, resp2.context['results'])
        self.assertTemplateUsed(resp2, 'minerals/mineral_search.html')

    def test_more(self):
        resp = self.client.get(
            reverse('minerals:more', kwargs={'group': 'Color'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.color, resp.context['match'])
        self.assertTemplateUsed(resp, 'minerals/mineral_more.html')

    def test_special(self):
        resp = self.client.get(
            reverse('minerals:special',
                    kwargs={'special': 'Green', 'group': 'Color'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_1, resp.context['match'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')