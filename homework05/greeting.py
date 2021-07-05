from api_facade import regr_greet_api


def say_hi(name):
  return f"Hi {name} ^^."


def say_hello(name):
  return f"Hello, {name}~"


@regr_greet_api
def say_aloha(name):
  return f"Aloha, {name}!"
