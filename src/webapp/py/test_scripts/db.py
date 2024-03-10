import sys
sys.path.append('..')

from utils.battleOfSeaDAO import*

# Usage example
databaseAccessMechanism = userDao()
databaseAccessMechanism.open_session()
#databaseAccessMechanism.set_personal_data('mariosxama@gmail.com','jahsdkjasf','123423')
#result = databaseAccessMechanism.account_exists('mariosxama@gmail.com')
result = databaseAccessMechanism.validate_account('mariosxama@hotmail.com','jahsdkjasf')
print(result)
