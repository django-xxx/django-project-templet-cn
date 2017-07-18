# django-project-templet-cn
Django Project Templet for CN

## Usage
* Basemodels
  ```python
  from templetCN.basemodels import CreateUpdateMixin

  class OrderInfo(CreateUpdateMixin):
      xxx
  ```
* Email Server Error
  * When DEBUG is False, Django will email the users listed in the ADMINS setting
  * whenever your code raises an unhandled exception and results in an internal server error (HTTP status code 500)
  * Uncomment url pattern in ``/api/urls.py`` to test.
* JSON Response
  ```python
  from utils.error.errno_utils import ProfileStatusCode
  from utils.error.response_utils import response
  
  def response_templet(request):
      # return response(ProfileStatusCode.PROFILE_NOT_FOUND)
      return response()
  ```
* Redis Usage
  ```python
  from utils.redis.connect import r
  
  # r.keys()
  ```
* WeChat OAuth2 & JSAPI
  * OAuth2
    * Url: http://a.com/we/oauth2?redirect_url=redirect_url
  * JSAPI
    * Url: http://a.com/we/jsapi_signature
    * Method: Get/POST/JSONP
    * Params: url - current page's url
