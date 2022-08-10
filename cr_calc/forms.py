from django import forms

class CalcPostForm(forms.Form):
    age = forms.IntegerField(required=True, label='Возраст', min_value=0, max_value=120)
    gender = forms.ChoiceField( required=True, choices=(('Female', 'Female'), 
                                                        ('Male', 'Male')), 
                                label='Пол', initial='Male')
    source_income = forms.ChoiceField(required=True, 
                                      choices=(('passive', 'пассивный доход'),
                                               ('employee', 'наёмный работник'),
                                               ('own_business', 'собственный бизнес'),
                                               ('unemployed', 'безработный')), 
                                      label='Источник дохода', initial='employee')
    income_last_year = forms.FloatField(required=True, label='Доход за последний год, млн')
    credit_rating = forms.ChoiceField(required=True, 
                                      choices=(('-2', '-2'),
                                               ('-1', '-1'),
                                               ('0', '0'),
                                               ('1', '1'),
                                               ('2', '2')), 
                                      label='Кредитный рейтинг', initial='0')
    requested_amount = forms.FloatField(required=True, min_value=0.1, max_value=10, label='Запрошенная сумма, млн')
    maturity_date = forms.FloatField(required=True, min_value=1, max_value=20, label='Срок погашения, лет')
    goal = forms.ChoiceField(required=True, 
                                      choices=(('mortgage', 'ипотека'),
                                               ('business_growth', 'развитие бизнеса'),
                                               ('car_credit', 'автокредит'),
                                               ('consumer', 'потребительский')), 
                                      label='Цель', initial='consumer')
