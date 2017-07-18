# django-project-templet-cn
Django Project Templet for CN

## Usage
* Basemodels
  ```python
  from templetCN.basemodels import CreateUpdateMixin

  class OrderInfo(CreateUpdateMixin):
      xxx
  ```
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