"""
Password hashing utilities.
"""
import hashlib
import secrets


def hash_password(password: str) -> str:
    """Hash password using PBKDF2 with SHA256."""
    salt = secrets.token_hex(32)
    password_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        bytes.fromhex(salt),
        100000
    )
    return f"{salt}${password_hash.hex()}"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash."""
    try:
        salt, stored_hash = hashed_password.split('$')
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            plain_password.encode('utf-8'),
            bytes.fromhex(salt),
            100000
        )
        return password_hash.hex() == stored_hash
    except:
        return False
