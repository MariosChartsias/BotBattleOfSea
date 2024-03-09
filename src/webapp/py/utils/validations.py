class validations:
    def __init__(self,dictionary):
        self.dictionary = dictionary


    def validateData(self,email):
        if email in self.dictionary:
            user_data = self.dictionary[email]
            if(user_data["checkBoxTerms"]):
                return True
            else:
                return False

    