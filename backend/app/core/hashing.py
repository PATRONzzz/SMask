from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


class Hasher:
    """Веритификация пороля"""

    @staticmethod
    def verify_password(password, hashed_password):
        return password_hash.verify(password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return password_hash.hash(password)
