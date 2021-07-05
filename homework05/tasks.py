import api_facade
import greeting
import bye


def do_work(
    name='Selina',
    greet_api_name=api_facade.GREET_API_NAME,
    bye_api_name=api_facade.BYE_API_NAME):
  print(api_facade.PUBLIC_API_STORES[greet_api_name](name))
  print(api_facade.PUBLIC_API_STORES[bye_api_name](name))
