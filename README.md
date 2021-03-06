# blanket
Blanket is an easy to use payload encryptor for securely transferring data between distributed applications

## Features
- AES256 Encrpytion
- Randomly generated one-time use keys
- Randomly generated one-time use secrets
- Randomly generated payload padding and structure
- Embedded payload signature to prevent man-in-the-middle attacks
- Self-contained payload

## Example Usage

```python
payload = "Hey there"

blanket = Blanket()
blanket.cover(payload)
```

### Output

`936MTgxOTE3MDE3MTIyMTgxNg==936CKC3wWCi2bKAaLE5fXAMt72ONgJ39cXPzV7L4FA671i9kWiNLzio/vlmRCFgkHPvSTX9DPfL9tOvMQEjUoI8fhrN5Eh7/FaZtW1zn1JZWZ6x3ycGU+udTxcUCOQ4PIu2JcjMtSSN2D9Z8/iYKa8rdzIetqteaOgmnZdDkEcvNvc/VetXOb5pP8JDyU0q51RtaGXFF55KqDbDM9XH2xbJTyOw8wyCZswQXos2saIdZgnnm005Pbmslc0FzPua1a7eVwR11uCPsG2T/fmvIoagkBySG8aJ9kULpot7vZl634jQZnzGQ5NkCQHxQNbGRvfQxca8OhZjsZymLDRKUfPISLgQL7MlV95rXW/s8LDeIkT4x6EC8aw1AJ6/I6eG9iiu936I/oAoewcqmG+NFPCnOSVQMIqbY3k6Hta4dg3UXzLMogzyKvzqRdHtpoCYD6Lc0hZpwo5vb26Sn40KEJXNDb/GgV3z/vEVjxZ4d6Guq1/NbFzdW4sstu+k7QWe5BBvJOtoZNHpPZsp9qrbPN2rQ2CWhucBMVV/YMFRAQZ85AyEQCbedELnY3VDKiEkDyKUs4v8da6UesAilPi33iTN9h6kQ==936pQVae6PEHYZVMlrcnMOqn5fW3in5VIliHi4Hryv+HdM=`

## Created by

![alt text](http://dev.jeffinko.guru/logo4.png "JeffinkoGuru")