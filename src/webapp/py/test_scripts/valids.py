import sys
sys.path.append('..')

from utils.validations import*

valid_data = {
    'username': 'john_doe',
    'email': 'johne@12.com',
    'password': 'strongPassword123',
    'confirm_password': 'strsgPassword123',
    'checkBoxTerms': True
}

invalid_email_data = {
    'username': 'jane_doe',
    'email': 'janedoe@example',  # Invalid email format
    'password': 'password123',
    'confirm_password': 'password123',
    'checkBoxTerms': True
}

password_mismatch_data = {
    'username': 'alice_smith',
    'email': 'alice@example.com',
    'password': 'secretPassword',
    'confirm_password': 'differentPassword',  # Password mismatch
    'checkBoxTerms': True
}


validator_instance = validations(valid_data)
result = validator_instance.fullvalidation(valid_data['email'])
print(result)