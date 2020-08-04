#otp_generator
import random
import string
def otp_generator(size=6,a=string.ascii_lowercase+string.ascii_uppercase+string.digits):
    return ''.join(random.choice(a) for i in range(size))    
print(otp_generator())
