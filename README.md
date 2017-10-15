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
    * views.py
      ```python
      from django.conf import settings
      from django.shortcuts import render
      from templet.decorators import check_token

      @check_token
      def render_template_func(request):
          return render(request, 'template_file_path', {
              'domain': settings.DOMAIN,
              'params': '{0}={1}&vtoken={2}'.format(settings.TOKEN_CHECK_KEY, 'token_check_key', request.GET.get('vtoken', '')),
          })
      ```
    * template.html
      ```html
      {{ domain }}/xxx?{{ params|safe }}
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

## Tips
* MultipleObjectsReturned & get_or_create()
  ```python
  model, created = Model.objects.select_for_update().get_or_create(arg1=arg1, arg2=arg2)
  ```
  * Kwargs for ``get_or_create`` should be unique. Use ``unique/unique_together``
    * unique
      ```
      field = models.CharField(_(u'field'), max_length=255, blank=True, null=True, help_text=u'field_text', db_index=True, unique=True)
      ```
    * unique_together
      ```
      field1 = models.CharField(_(u'field1'), max_length=32, blank=True, null=True, help_text=u'field1_text', db_index=True)
      field2 = models.CharField(_(u'field2'), max_length=32, blank=True, null=True, help_text=u'field2_text', db_index=True)

      class Meta:
          verbose_name = _(u'verbose_name')
          verbose_name_plural = _(u'verbose_name_plural')

          unique_together = (
              ('field1', 'field2'),
          )
      ```
  * 1071, ‘Specified key was too long; max key length is 767/1000/3072 bytes’
    ```
    Prefix support and lengths of prefixes (where supported) are storage engine dependent.
    For example, a prefix can be up to 767 bytes long for InnoDB tables or 3072 bytes if the innodb_large_prefix option is enabled.
    For MyISAM tables, the prefix limit is 1000 bytes.
    The NDB storage engine does not support prefixes (see Section 21.1.6.6, “Unsupported or Missing Features in NDB Cluster”).
    ```
    * [13.1.14 CREATE INDEX Syntax](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
    * Solutions
      * Execute SQL in dbshell
        ```
        alter ignore table table_name add unique index(field(255));
        ```
      * Decrease CharField's max_length
