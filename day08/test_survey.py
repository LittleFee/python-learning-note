import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey的测试"""
    def test_single_ans_store(self):
        """测试单个答案会被妥善地存储"""
        question='What\'s your favorite subject ?'
        survey=AnonymousSurvey(question)
        survey.store_response('english')
        self.assertIn('english',survey.responses)

    def test_store_three_responses(self):
        question = 'What\'s your favorite subject ?'
        survey=AnonymousSurvey(question)
        ans=['English','Math','Physics','PE']
        for item in ans:
            survey.store_response(item)
        for item in survey.responses:
            self.assertIn(item,ans)


unittest.main()
