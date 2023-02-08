from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    password_hash = pwd_context.hash(password)

    return password_hash


def verify_hash_password(password: str, password_hash: str):
    valid_password = pwd_context.verify(password, password_hash)

    return valid_password
