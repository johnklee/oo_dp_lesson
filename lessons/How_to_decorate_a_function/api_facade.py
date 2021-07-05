PUBLIC_API_STORES = {}
''' Key as api name; value as api object'''

GREET_API_NAME = 'greet_api'
''' Name of greeting API '''

BYE_API_NAME = 'bye_api'
''' Name of API to say bye'''


def regr_greet_api(_func=None, *, api_name=GREET_API_NAME):
  def regr_wrapper(func):
    PUBLIC_API_STORES[api_name] = func
    return func

  if _func is None:
    return regr_wrapper
  else:
    return regr_wrapper(_func)


def regr_bye_api(_func=None, *, api_name=BYE_API_NAME):
  def regr_wrapper(func):
    PUBLIC_API_STORES[api_name] = func
    return func

  if _func is None:
    return regr_wrapper
  else:
    return regr_wrapper(_func)
