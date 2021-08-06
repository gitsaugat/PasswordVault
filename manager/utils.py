from hashlib import sha1, sha256  
import random

class PasswordEncoder:

    def encode_password(self , password , secret_key ):

        encoded_password = password.encode()
        encoded_secret_key = secret_key.encode()

        attempt_first_encoded_password = sha1(encoded_password).hexdigest()
        attempt_first_encoded_secret_key = sha256(encoded_secret_key).hexdigest()

        random_generated_number = random.random()

        attempt_first_encoded_random_number = sha256(random_generated_number).hexdigest()

        attempt_last_password = attempt_first_encoded_password+attempt_first_encoded_secret_key+'.'+attempt_first_encoded_random_number

        attempt_last_encoded_password = sha1(attempt_last_password).hexdigest()

        return attempt_last_encoded_password

    def decode_password(self , password , random_number , secret_key):


