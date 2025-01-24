class Data:
    def __init__(self, list: tuple):
        if len(list) > 3:
            print("BAD FORMAT")
        self.days = int(list[0])
        self.month = int(list[1])
        self.year = int(list[2])

    def validate(self) -> bool:
        months = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        def is_leap_year(year_to_check):
            return year_to_check % 4 == 0 and (year_to_check % 100 != 0 or year_to_check % 400 == 0)

        if is_leap_year(self.year):
            months[2] = 29
        if not 1 <= self.month <= 12:
            return False

        max_days_in_month = months[self.month]
        if not 1 <= self.days <= max_days_in_month: return False;

        return True


def valid_data(data):
    try:
        date_parts = Data(tuple(data.split(".")))
        if date_parts.validate():
            return "Correct date"
        else:
            return "Not correct date"

    except ValueError:
        print("BAD FORMAT")

value = input(" Print date in format dd.MM.yyyy or wil be an exception: ")

print(valid_data(value))