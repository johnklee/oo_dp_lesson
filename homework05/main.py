#!/usr/bin/env python3
import api_facade
from api_facade import regr_greet_api, regr_bye_api


@regr_greet_api
def greet_by_hello(name):
  return f"Hello, {name}~"


@regr_bye_api
def say_bye(name):
  return f"Bye, {name}. ^^"


def do_work(name='Selina', greet_api_name=api_facade.GREET_API_NAME, bye_api_name=api_facade.BYE_API_NAME):
  print(api_facade.PUBLIC_API_STORES[greet_api_name](name))
  print(api_facade.PUBLIC_API_STORES[bye_api_name](name))


if __name__ == '__main__':
  do_work()
