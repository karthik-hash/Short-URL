import random
import string

def code_generator(size=6, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(6))

def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    Repeat = instance.__class__
    qs_exists = Repeat.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
