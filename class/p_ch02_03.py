class Car():
    """
    Car class
    Author: Lee
    Date: 2020.08.17
    Description: Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0


    def __init__(self, company, details):
        self._company = company
        # self.car_count = 10
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance method
    # Self: 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance method
    def get_price(self):
        return 'Before Car Price -> company : {}. price : {}'.format(self._company, self._details.get('price'))

    # Instance method
    def get_price_calc(self):
        return 'After Car Price -> company : {}. price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please enter 1 or more')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')

    # Static method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not bmw.'




# Self 의미   
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})


# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보(직접 접근)
print(car1._details.get('price'))
print(car2._details.get('price'))

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격 정보(인상 후)
print(car1.get_price_calc())
print(car2.get_price_calc())

Car.raise_price(2)

# 가격 정보(인상 후)
print(car1.get_price_calc())
print(car2.get_price_calc())

print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car1))