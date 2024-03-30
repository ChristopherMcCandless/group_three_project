import unittest
from unittest.mock import MagicMock

from src.models.summarizer import Summarizer
from src.models.translator import Translator
from src.services.text_summary_service import TextSummaryService


# class TestPunctuator(unittest.TestCase):
#     def setUp(self):
#         self.punctuator = Punctuator()

#     def test_punctuate_returns_string(self):
#         result = self.punctuator.punctuate("Test input")
#         self.assertIsInstance(result, str)


class TestSummarizer(unittest.TestCase):
    def setUp(self):
        self.summarizer = Summarizer()

    def test_summarize_returns_string(self):
        result = self.summarizer.summarize("Test input")
        self.assertIsInstance(result, str)


class TestTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = Translator()

    def test_ru_en_returns_string(self):
        result = self.translator.ru_en("Тестовый ввод")
        self.assertIsInstance(result, str)

    def test_en_ru_returns_string(self):
        result = self.translator.en_ru("Test input")
        self.assertIsInstance(result, str)


class TestTextSummaryService(unittest.TestCase):
    def setUp(self):
        self.text_summary_service = TextSummaryService()

    def test_handle_returns_correct_results(self):
        #Arrange
        self.text_summary_service.translator = MagicMock()
        self.text_summary_service.summarizer = MagicMock()

        self.text_summary_service.translator.ru_en.return_value = "Test English text"
        self.text_summary_service.summarizer.summarize.return_value = "Test summary"
        self.text_summary_service.translator.en_ru.return_value = "Тестовый конспект"

        #Act
        ru_summary = self.text_summary_service.handle("Тестовый текст", useV2=False)
        
        #Assert
        self.assertEqual(ru_summary, "Тестовый конспект")


if __name__ == '__main__':
    unittest.main()