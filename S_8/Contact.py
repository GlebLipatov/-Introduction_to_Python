class Contact:

    def __init__(self, id: int, first_name: str, last_name: str, phone_number: str, comment: str):
        self.id = id
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.phone_number = phone_number
        self.comment = comment.lower()

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def set_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def set_comment(self, new_comment):
        self.comment = new_comment

    def get_contact_data(self) -> list:
        return [str(self.id), self.first_name, self.last_name, self.phone_number, self.comment]

    def get_data_to_save(self) -> str:
        return f'{self.id};{self.first_name};{self.last_name};{self.phone_number};{self.comment}\n'