#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
say_my_name(str(123), "Edi")
say_my_name()
result = type(say_my_name("Edi", str(123)))
print(result)
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
