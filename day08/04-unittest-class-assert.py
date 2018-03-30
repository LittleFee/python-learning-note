# 各种断言方法
# assertEqual(a, b)  核实a == b
# assertNotEqual(a, b)  核实a != b
# assertTrue(x)  核实x为True
# assertFalse(x)  核实x为False
# assertIn(item, list)  核实item在list中
# assertNotIn(item, list)  核实item不在list中
# 你只能在继承unittest.TestCase的
# 类中使用这些方法
from survey import AnonymousSurvey

question = 'What language do you like ?'
survey = AnonymousSurvey(question)

survey.show_question()
print('Enter \'q\' anytime to quit')
while True:

    ans = input('Language: ')
    if ans.lower() == 'q':
        break
    survey.store_response(ans)

survey.show_results()