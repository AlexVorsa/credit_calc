import math

class helper():
    def calc(info):
        """
        """
        # const
        retirement_age = 65.0
        base_rate = 10.0
        max_amount_value = 0.0
        approved_amount = 0.0


        res = dict()
        res['Approve'] = 'Кредит одобрен'
        res['Approved_amount'] = None
        res['Annual'] = None

        if (info['age'] + info['maturity_date']) > retirement_age:
           res['Approve'] = 'Кредит не одобрен'
        if info['credit_rating'] == '-2':
            res['Approve'] = 'Кредит не одобрен'
        if info['source_income'] == 'unemployed':
            res['Approve'] = 'Кредит не одобрен'
        if (info['requested_amount'] / info['maturity_date']) > (info['income_last_year']/3):
            res['Approve'] = 'Кредит не одобрен'
        
        if res['Approve'] == 'Кредит одобрен':
            if info['source_income'] == 'passive':
                max_amount_value = 1.0

            if info['source_income'] == 'employee':
                if info['credit_rating'] == '-1':
                    max_amount_value = 1.0
                elif info['credit_rating'] in ('0', '1', '2'):
                    max_amount_value = 5.0
            
            if info['source_income'] == 'own_business':
                if info['credit_rating'] == '-1':
                    max_amount_value = 1.0
                elif info['credit_rating'] == '0':
                    max_amount_value = 5.0
                elif info['credit_rating'] in ('1', '2'):
                    max_amount_value = 10.0

            if info['goal'] == 'mortgage':
                base_rate -= 2
            elif info['goal'] == 'business_growth':
                base_rate -= 0.5
            elif info['goal'] == 'consumer':
                base_rate += 1.5

            if info['credit_rating'] == '-1':
                base_rate += 1.5
            elif info['credit_rating'] == '1':
                base_rate -= 0.25
            elif info['credit_rating'] == '2':
                base_rate -= 0.75

            if info['source_income'] == 'passive':
                base_rate += 0.5
            elif info['source_income'] == 'employee':
                base_rate -= 0.25
            elif info['source_income'] == 'own_business':
                base_rate += 0.25        
            
            if info['requested_amount'] < max_amount_value:
                approved_amount = info['requested_amount']
            else:
                approved_amount = max_amount_value
            
            base_rate += math.log10(approved_amount) * (-1)

            annual = (approved_amount * (base_rate/100 + ((base_rate/100)/(((1 + base_rate/100)**info['maturity_date']) -1))))
            # annuall = (approved_amount * (1 + (info['maturity_date'] * base_rate/100))) / info['maturity_date']

            res['Approved_amount'] = approved_amount
            res['Annual'] = round(annual, 3)
            res['Rate'] = base_rate
        return res