from django.test import TestCase
from model_mommy import mommy

from comprAgendada.hampers.models import Hamper


class TestHamper(TestCase):
    def setUp(self):
        self.hamper = (
            mommy.make(Hamper, name="#1", description="Basic hamper.")
        )

    def test_hamper_creation(self):
        self.assertTrue(isinstance(self.hamper, Hamper))
