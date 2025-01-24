class ValidationError(Exception):
    pass


class Dictionary:

    def __init__(self, name: str, surname: str, age: int, id: str):
        errors = []

        self.validate_constructor_data(age, errors, id, name, surname)

    def validate_constructor_data(self, age, errors, id, name, surname):
        try:
            self.name = validate_names(name)
            if self.name is False:
                errors.append(ValidationError(f"name '{name}' needs to be only characters"))
            self.surname = validate_names(surname)
            if self.surname is False:
                errors.append((f"surname '{surname}' needs to be only characters"))
            self.age = age
            if not 18 <= int(self.age) <= 60:
                errors.append(ValidationError(f"age '{age}' needs to be between 18 and 60"))
            try:
                self.id = id_preparation(id)
            except ValidationError as e:
                errors.append(e)
        finally:
            if errors:
                for error in errors:
                    print(f"Bad data for: {error}")
                raise ValueError("One or more validation errors occurred") from errors[-1]


def validate_names(name: str):
    if not name.isalpha():
        return False
    else:
        return name.lower().title()


def id_preparation(id_value: str):
    int(id_value)
    length = len(id_value)
    if length > 8: raise ValidationError(f"id '{id_value}' needs to be prepared correctly")
    return id_value.zfill(8)

def create_table_from_map(dict_table: {}) -> str:
    result_table = 'Table results \n'
    for key, val in dict_table.items():
        result_table += f"{key} - {val} \n"
    return result_table


def create_dict_table():
    dict_list = []  # список мап

    while True:
        try:
            dictionary_type = dictionary_creation()
            if (
                    dictionary_type is None
            ):
                map_res = {}
                for dict in dict_list:
                    map_res[dict.id] = (dict.name, dict.surname, dict.age)
                else:
                    res = create_table_from_map(map_res)
                    print(res)
                    break
            else:
                dict_list.append(dictionary_type)

        except ValueError:
            print("""
            CHECK DATA NAME -> string,  
            SURNAME -> string,
            ID -> string,
            age -> integer,
            """)
            break


def dictionary_creation() -> Dictionary | None:
    name = input('Enter name: ')
    if len(name) == 0: return None
    surname = input('Enter surname: ')
    if len(surname) == 0: return None
    age = input('Enter age: ')
    if len(age) == 0: return None
    id = input('Enter id: ')
    if len(id) == 0: return None
    return Dictionary(name, surname, int(age), id)


create_dict_table()
