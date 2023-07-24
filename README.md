# DJANGO
Description:
Django databases and app creation across cryptographic
tools in httplib, urlib3 and crypto hashing with django.

CRYPTOGRAPHY_BACKEND
Default: cryptography.hazmat.backends.default_backend()

CRYPTOGRAPHY_DIGEST
Default: cryptography.hazmat.primitives.hashes.SHA256

The digest algorithm to use for signing and key generation.

CRYPTOGRAPHY_KEY
Default: None

When value is None a key will be derived from SECRET_KEY. Otherwise the value will be used for the key.

CRYPTOGRAPHY_SALT
Default: 'django-cryptography'

Drop-in Replacements
SIGNING_BACKEND
The default can be replaced with a a Cryptography based version.

SIGNING_BACKEND = 'django_cryptography.core.signing.TimestampSigner'
