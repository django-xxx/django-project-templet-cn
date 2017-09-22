# django-project-templet-cn
Django Project Templet for CN

## Usage
* Basemodels
  ```python
  from templet.basemodels import CreateUpdateMixin

  class OrderInfo(CreateUpdateMixin):
      xxx
  ```
* Command
  * sendredpack/transfers
* Email Server Error
  * When DEBUG is False, Django will email the users listed in the ADMINS setting
  * whenever your code raises an unhandled exception and results in an internal server error (HTTP status code 500)
  * Request api ``/uniapi/error`` to test.
  * If mail not send, may limited by mail service.
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
* V Token
  * Decorator check ``vtoken``
    ```
    from django.shortcuts import render
    from templet.decorators import check_token

    @check_token
    def render_template_func(request):
        return render(request, 'template_file_path', {})
    ```
* WeChat OAuth2 & JSAPI
  * OAuth2
    * URL: http://a.com/we/oauth2?redirect_url=redirect_url
  * JSAPI
    * URL: http://a.com/we/jsapi_signature
    * Method: Get/POST/JSONP
    * Params: url - current page's url
  * Share Redirect URL
    * [JSSDK自定义分享接口的策略调整](https://mp.weixin.qq.com/s/hAdtKl2i4ilyo9HxT1kXyw)
  * In order to use ``request.wechat``, should add middleware
    ```
    MIDDLEWARE = [
        ...
        'detect.middleware.UserAgentDetectionMiddleware',
        ...
    ]
    ```
