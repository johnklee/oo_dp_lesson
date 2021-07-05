from api_facade import regr_bye_api 


def say_goodbye(name):
  return f"Goodbye, {name}!"


@regr_bye_api
def say_seeu(name):
  return f"See you, {name}~"


def say_takecare(name):
  return f"Take care! {name}." 
