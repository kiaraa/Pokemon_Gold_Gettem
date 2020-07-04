from unittest import TestCase

from DataManipulation.TrainerEditor import TrainerEditor


class Test(TestCase):

    def test_get_trainer_object_gets_first_trainer_name(self):

        trainer_editor = TrainerEditor()
        trainer = trainer_editor.get_trainer_object(0)
        self.assertEqual(trainer.get_name(), "JOEY", "This is not youngster Joey!")