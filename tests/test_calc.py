import pytest

from tests.helper.cr_calc_page import CommonHelper

CASE_PASSIVE = [
    {'credit_rating': '0', 'goal': 'business_growth', 'expected_payment': '0.264', 'expected_rate': '10.0'},
    {'credit_rating': '1', 'goal': 'car_credit', 'expected_payment': '0.265', 'expected_rate': '10.25'},
    {'credit_rating': '2', 'goal': 'consumer', 'expected_payment': '0.272', 'expected_rate': '11.25'},
    {'credit_rating': '2', 'goal': 'business_growth', 'expected_payment': '0.259', 'expected_rate': '9.25'},
    {'credit_rating': '-1', 'goal': 'consumer', 'expected_payment': '0.288', 'expected_rate': '13.5'},
    {'credit_rating': '0', 'goal': 'mortgage', 'expected_payment': '0.254', 'expected_rate': '8.5'}
]

@pytest.mark.parametrize('case', CASE_PASSIVE)
def test_direct_scenario_passive(case, browser):
    page = CommonHelper(browser)
    page.go_to_site()

    page.enter_input('#id_age', '25')
    page.set_select_option('#id_gender', 'Male')
    page.set_select_option('#id_source_income', 'passive')
    page.enter_input('#id_income_last_year', '5')
    page.set_select_option('#id_credit_rating', case['credit_rating'])
    page.enter_input('#id_requested_amount', '1')
    page.enter_input('#id_maturity_date', '5')
    page.set_select_option('#id_goal', case['goal'])
    page.click_submit_button()

    errors = page.check_error_forms()
    assert not errors, 'Unexpected error message'

    assert page.get_value('result') == 'Результат: Кредит одобрен', 'Unexpected result'
    assert page.get_value('amount') == 'Одобренная сумма: 1.0 млн. рублей', 'Unexpected amount'
    expected_payment = case['expected_payment']
    assert page.get_value('annual_payment') == f'Ежегодный платеж: {expected_payment} млн. рублей', 'Unexpected annual payment'
    expected_rate = case['expected_rate']
    assert page.get_value('rate') == f'Процент ставки по кредиту: {expected_rate}%', 'Unexpected rate'


CASE_EMPLOYEE = [
    {'credit_rating': '0', 'goal': 'car_credit', 'expected_payment': '0.262', 'expected_rate': '9.75'},
    {'credit_rating': '1', 'goal': 'consumer', 'expected_payment': '0.271', 'expected_rate': '11.0'},
    {'credit_rating': '2', 'goal': 'mortgage', 'expected_payment': '0.244', 'expected_rate': '7.0'},
    {'credit_rating': '-1', 'goal': 'mortgage', 'expected_payment': '0.259', 'expected_rate': '9.25'},
    {'credit_rating': '-1', 'goal': 'consumer', 'expected_payment': '0.283', 'expected_rate': '12.75'},
    {'credit_rating': '0', 'goal': 'mortgage', 'expected_payment': '0.249', 'expected_rate': '7.75'},
    {'credit_rating': '1', 'goal': 'business_growth', 'expected_payment': '0.257', 'expected_rate': '9.0'},
    {'credit_rating': '2', 'goal': 'car_credit', 'expected_payment': '0.257', 'expected_rate': '9.0'}
]

@pytest.mark.parametrize('case', CASE_EMPLOYEE)
def test_direct_scenario_employee(case, browser):
    page = CommonHelper(browser)
    page.go_to_site()

    page.enter_input('#id_age', '25')
    page.set_select_option('#id_gender', 'Male')
    page.set_select_option('#id_source_income', 'employee')
    page.enter_input('#id_income_last_year', '5')
    page.set_select_option('#id_credit_rating', case['credit_rating'])
    page.enter_input('#id_requested_amount', '1')
    page.enter_input('#id_maturity_date', '5')
    page.set_select_option('#id_goal', case['goal'])
    page.click_submit_button()

    errors = page.check_error_forms()
    assert not errors, 'Unexpected error message'

    assert page.get_value('result') == 'Результат: Кредит одобрен', 'Unexpected result'
    assert page.get_value('amount') == 'Одобренная сумма: 1.0 млн. рублей', 'Unexpected amount'
    expected_payment = case['expected_payment']
    assert page.get_value('annual_payment') == f'Ежегодный платеж: {expected_payment} млн. рублей', 'Unexpected annual payment'
    expected_rate = case['expected_rate']
    assert page.get_value('rate') == f'Процент ставки по кредиту: {expected_rate}%', 'Unexpected rate'


CASE_BUSINESS = [
    {'credit_rating': '1', 'goal': 'mortgage', 'expected_payment': '0.25', 'expected_rate': '8.0'},
    {'credit_rating': '2', 'goal': 'mortgage', 'expected_payment': '0.247', 'expected_rate': '7.5'},
    {'credit_rating': '-1', 'goal': 'business_growth', 'expected_payment': '0.272', 'expected_rate': '11.25'},
    {'credit_rating': '-1', 'goal': 'car_credit', 'expected_payment': '0.276', 'expected_rate': '11.75'},
    {'credit_rating': '0', 'goal': 'consumer', 'expected_payment': '0.276', 'expected_rate': '11.75'}
]

@pytest.mark.parametrize('case', CASE_BUSINESS)
def test_direct_scenario_business(case, browser):
    page = CommonHelper(browser)
    page.go_to_site()

    page.enter_input('#id_age', '25')
    page.set_select_option('#id_gender', 'Male')
    page.set_select_option('#id_source_income', 'own_business')
    page.enter_input('#id_income_last_year', '5')
    page.set_select_option('#id_credit_rating', case['credit_rating'])
    page.enter_input('#id_requested_amount', '1')
    page.enter_input('#id_maturity_date', '5')
    page.set_select_option('#id_goal', case['goal'])
    page.click_submit_button()

    errors = page.check_error_forms()
    assert not errors, 'Unexpected error message'

    assert page.get_value('result') == 'Результат: Кредит одобрен', 'Unexpected result'
    assert page.get_value('amount') == 'Одобренная сумма: 1.0 млн. рублей', 'Unexpected amount'
    expected_payment = case['expected_payment']
    assert page.get_value('annual_payment') == f'Ежегодный платеж: {expected_payment} млн. рублей', 'Unexpected annual payment'
    expected_rate = case['expected_rate']
    assert page.get_value('rate') == f'Процент ставки по кредиту: {expected_rate}%', 'Unexpected rate'


CASE_NOT_APPROVED = [
    {'age': '60', 'maturity_date': '6', 'credit_rating': '0', 'source_income': 'employee', 'requested_amount': '1', 'income_last_year': '5'},
    {'age': '35', 'maturity_date': '6', 'credit_rating': '-2', 'source_income': 'employee', 'requested_amount': '1', 'income_last_year': '5'},
    {'age': '35', 'maturity_date': '6', 'credit_rating': '0', 'source_income': 'unemployed', 'requested_amount': '1', 'income_last_year': '5'},
    {'age': '35', 'maturity_date': '6', 'credit_rating': '0', 'source_income': 'employee', 'requested_amount': '1', 'income_last_year': '0.1'}
]

@pytest.mark.parametrize('case', CASE_NOT_APPROVED)
def test_direct_not_approved(case, browser):
    page = CommonHelper(browser)
    page.go_to_site()

    page.enter_input('#id_age', case['age'])
    page.set_select_option('#id_gender', 'Male')
    page.set_select_option('#id_source_income', case['source_income'])
    page.enter_input('#id_income_last_year', case['income_last_year'])
    page.set_select_option('#id_credit_rating', case['credit_rating'])
    page.enter_input('#id_requested_amount', case['requested_amount'])
    page.enter_input('#id_maturity_date', case['maturity_date'])
    page.set_select_option('#id_goal', 'consumer')
    page.click_submit_button()

    errors = page.check_error_forms()
    assert not errors, 'Unexpected error message'

    assert page.get_value('result') == 'Результат: Кредит не одобрен', 'Unexpected result'


CASE_AGE = [
    {'age': '', 'message': 'Обязательное поле.'},
    {'age': '125', 'message': 'Убедитесь, что это значение меньше либо равно 120.'},
    {'age': 'QW!RT', 'message': 'Обязательное поле.'},
    {'age': '0.5', 'message': 'Введите целое число.'},
    {'age': '-5', 'message': 'Убедитесь, что это значение больше либо равно 0.'}
]

@pytest.mark.parametrize('case', CASE_AGE)
def test_input_age(case, browser):
    page = CommonHelper(browser)
    page.go_to_site()
      
    page.enter_input('#id_income_last_year', '5')
    page.enter_input('#id_requested_amount', '1')
    page.enter_input('#id_maturity_date', '5')
        
    page.enter_input('#id_age', case['age'])
    page.click_submit_button()

    errors = page.check_error_forms()
    assert len(errors) == 1, 'Recieved unexpected number of errors'
    assert errors[0].text == case['message'], 'Unexpected error message'


CASE_INCOME_LAST_YEAR = [
    {'income': '', 'message': 'Обязательное поле.'},
    {'income': 'QW!RT', 'message': 'Обязательное поле.'}
]

@pytest.mark.parametrize('case', CASE_INCOME_LAST_YEAR)
def test_input_income_last_year(case, browser):
    page = CommonHelper(browser)
    page.go_to_site()

    page.enter_input('#id_age', '25')    
    page.enter_input('#id_requested_amount', '1')
    page.enter_input('#id_maturity_date', '5')
        
    page.enter_input('#id_income_last_year', case['income'])
    page.click_submit_button()

    errors = page.check_error_forms()
    assert len(errors) == 1, 'Recieved unexpected number of errors'
    assert errors[0].text == case['message'], 'Unexpected error message'


CASE_REQUESTED_AMOUNT = [
    {'requested_amount': '', 'message': 'Обязательное поле.'},
    {'requested_amount': 'QW!RT', 'message': 'Обязательное поле.'},
    {'requested_amount': '-5', 'message': 'Убедитесь, что это значение больше либо равно 0.1.'},
    {'requested_amount': '10.1', 'message': 'Убедитесь, что это значение меньше либо равно 10.'}
]

@pytest.mark.parametrize('case', CASE_REQUESTED_AMOUNT)
def test_input_requested_amount(case, browser):
    page = CommonHelper(browser)
    page.go_to_site()

    page.enter_input('#id_age', '25')
    page.enter_input('#id_income_last_year', '5')     
    page.enter_input('#id_maturity_date', '5')
        
    page.enter_input('#id_requested_amount', case['requested_amount'])
    page.click_submit_button()

    errors = page.check_error_forms()
    assert len(errors) == 1, 'Recieved unexpected number of errors'
    assert errors[0].text == case['message'], 'Unexpected error message'


CASE_MATURITY_DATE = [
    {'maturity_date': '', 'message': 'Обязательное поле.'},
    {'maturity_date': 'QW!RT', 'message': 'Обязательное поле.'},
    {'maturity_date': '0', 'message': 'Убедитесь, что это значение больше либо равно 1.'},
    {'maturity_date': '21', 'message': 'Убедитесь, что это значение меньше либо равно 20.'}
]

@pytest.mark.parametrize('case', CASE_MATURITY_DATE)
def test_input_maturity_date(case, browser):
    page = CommonHelper(browser)
    page.go_to_site()

    page.enter_input('#id_age', '25')
    page.enter_input('#id_income_last_year', '5')
    page.enter_input('#id_requested_amount', '1')
        
    page.enter_input('#id_maturity_date', case['maturity_date'])
    page.click_submit_button()

    errors = page.check_error_forms()
    assert len(errors) == 1, 'Recieved unexpected number of errors'
    assert errors[0].text == case['message'], 'Unexpected error message'


def test_combobox(browser):
    page = CommonHelper(browser)
    page.go_to_site()

    el_goal = page.get_value('id_goal').split('\n')
    stripped_el_goal = [e.strip() for e in el_goal]

    assert stripped_el_goal == ['ипотека', 'развитие бизнеса', 'автокредит', 'потребительский'], "Unexpected option in combobox Goal"

    el_gender = page.get_value('id_gender').split('\n')
    stripped_el_gender = [e.strip() for e in el_gender]

    assert stripped_el_gender == ['Female', 'Male'], "Unexpected option in combobox Male"

    el_source = page.get_value('id_source_income').split('\n')
    stripped_el_source = [e.strip() for e in el_source]

    assert stripped_el_source == ['пассивный доход', 'наёмный работник', 'собственный бизнес', 'безработный'], \
        "Unexpected option in combobox Source income"

    el_rating = page.get_value('id_credit_rating').split('\n')
    stripped_el_rating = [e.strip() for e in el_rating]

    assert stripped_el_rating == ['-2', '-1', '0', '1', '2'], "Unexpected option in combobox Credit Rating"