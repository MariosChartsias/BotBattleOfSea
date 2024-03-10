from email_validator import validate_email, EmailNotValidError

class validations:
    error_message=None
    def __init__(self,dictionary):
        print(dictionary)
        self.dictionary = dictionary


    def fullvalidation(self,email):
        if(not email.strip()): return 'complete all fields'
        email_message = self.validate_email(email) 
        checkBox_message = self.validateCheckBox(email)
        password_message= self.validateConfirmedPassword(email)
        if(email_message is not None):
            return email_message
        if(checkBox_message is not None):
            return checkBox_message
        if(password_message is not None):
            return password_message
        return None

    def validate_email(self, email):
        if email.strip() and self.dictionary:
            try:
                emailinfo = validate_email(email, check_deliverability=False)
                # After this point, use only the normalized form of the email address,
                # especially before going to a database query.
                ######email = emailinfo.normalized
                #print(f"Email address: {email} is valid")
                return None
            except EmailNotValidError as e:
                # The exception message is human-readable explanation of why it's
                # not a valid (or deliverable) email address.
                print(str(e))
                return 'email is not valid'
        else:
            print("Email address not found in dictionary")
            return False
        
    def validateCheckBox(self,email):
        if email.strip() and self.dictionary:
            if(self.dictionary["checkBoxTerms"]):
                return None
            else:
                #print("CheckBox is False")
                return 'Accept Terms'
            
    def validateConfirmedPassword(self,email):
        if email.strip() and self.dictionary:
            
            if(self.dictionary["password"] == self.dictionary["confirm_password"]):
                return None
            else:
                #print("Passwords are different")
                return "Passwords are different"

