import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey的测试"""
    def setUp(self):
        question = 'What\'s your favorite subject ?'
        self.survey = AnonymousSurvey(question)
        self.ans=['English','Math','Physics','PE']
    def test_single_ans_store(self):
        """测试单个答案会被妥善地存储"""
        self.survey.store_response(self.ans[0])
        self.assertIn(self.ans[0],self.survey.responses)

    def test_store_three_responses(self):
        for item in self.ans:
            self.survey.store_response(item)
        for item in self.survey.responses:
            self.assertIn(item,self.ans)


unittest.main()
