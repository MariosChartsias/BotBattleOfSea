from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
import json
import os

class userDao(object):
    def __init__(self):
        self.session = None

    def open_session(self):
        """Connect to database and open a session."""
        script_dir = os.path.dirname(__file__)  # Get the directory of the current script
        config_path = os.path.join(script_dir, '..', 'config_files', 'config.json')

        with open(config_path) as f:
            config = json.load(f)['dbproxy']
        # Construct the database URL
        db_url = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
        # Create a database engine
        engine = create_engine(db_url)
        # Create a Session class
        Session = sessionmaker(bind=engine)
        # Open a session
        self.session = Session()

    def close_session(self):
        """Close the database session."""
        if self.session is not None:
            self.session.close()

        

    def set_personal_data(self, email, password):
        """Set personal data in the database."""
        try:
            # Construct the SQL insert statement with placeholders
            sql = text("INSERT INTO BOS_C01_PERSONAL_DATA (C01_EMAIL, C01_PASSWORD) VALUES (:email, :password)")
            # Execute the insert statement with parameter binding
            self.session.execute(sql, {"email": email, "password": password})
            # Commit the transaction
            self.session.commit()
        except Exception as e:
            # Handle any exceptions
            print("Failed to insert personal data:", e)
            self.session.rollback()
        finally:
            # Close the session
            self.close_session()

    def account_exists(self, email):
        """Check if a row with the given email exists in the database."""
        try:
            # Construct the SQL query to check if the email exists
            sql = text("SELECT EXISTS (SELECT 1 FROM BOS_C01_PERSONAL_DATA WHERE C01_EMAIL = :email)")
            # Execute the query with parameter binding
            result = self.session.execute(sql, {"email": email}).scalar()
            # Return True if a row exists with the email, False otherwise
            return bool(result)
        except Exception as e:
            # Handle any exceptions
            print("Error checking if email exists:", e)
            return False
        finally:
            # Close the session
            self.close_session()

    def areCredentialsCorrect(self, email,password):
        """Check if a row with the given email exists in the database."""
        try:
            # Construct the SQL query to check if the email exists
            sql = text("SELECT EXISTS (SELECT 1 FROM BOS_C01_PERSONAL_DATA WHERE C01_EMAIL = :email AND C01_PASSWORD = :password)")
            # Execute the query with parameter binding
            result = self.session.execute(sql, {"email": email, "password": password}).scalar()
            # Return True if a row exists with the email, False otherwise
            return bool(result)
        
        except Exception as e:
            # Handle any exceptions
            print("Error checking if email exists:", e)
            return False
        finally:
            # Close the session
            self.close_session()

    def activate_email(self, email):
        print(email)
        """Update the C01_IS_ACTIVATED column to 1 for the given email."""
        try:
            # Construct the SQL query to update the C01_IS_ACTIVATED column
            sql = text("UPDATE BOS_C01_PERSONAL_DATA SET C01_IS_ACTIVATED = 1 WHERE C01_EMAIL = :email")
            # Execute the query with parameter binding
            self.session.execute(sql, {"email": email.strip()})
            # Commit the transaction
            self.session.commit()
            # Return True indicating successful activation
            return True
        
        except Exception as e:
            # Rollback the transaction if an exception occurs
            self.session.rollback()
            # Handle any exceptions
            print("Error activating email:", e)
            return False
        finally:
            # Close the session
            self.close_session()

