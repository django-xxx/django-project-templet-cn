# -*- coding: utf-8 -*-

from StatusCode import BaseStatusCode, StatusCodeField


class ParamStatusCode(BaseStatusCode):
    """ 4000xx 参数相关错误码 """
    PARAM_NOT_FOUND = StatusCodeField(400000, 'Param Not Found', description=u'参数不存在')


class ProfileStatusCode(BaseStatusCode):
    """ 4001xx 用户相关错误码 """
    PROFILE_NOT_FOUND = StatusCodeField(400101, 'Profile Not Found', description=u'用户不存在')


class PhoneStatusCode(BaseStatusCode):
    """ 4002xx 手机相关错误码 """
    INVALID_PHONE = StatusCodeField(400200, 'Invalid Phone', description=u'非法手机号')
    PHONE_NOT_FOUND = StatusCodeField(400201, 'Phone Not Found', description=u'手机号不存在')
    PHONE_ALREADY_EXISTS = StatusCodeField(400202, 'Phone Already Exists', description=u'手机号已存在')


class OrderStatusCode(BaseStatusCode):
    """ 4040xx 订单／支付相关错误码 """
    UNIFIED_ORDER_FAIL = StatusCodeField(404000, 'Unified Order Fail', description=u'统一下单失败')
    ORDER_NOT_FOUND = StatusCodeField(404001, 'Order Not Found', description=u'订单不存在')
    # 订单支付状态
    ORDER_NOT_PAY = StatusCodeField(404011, 'Order Not Pay', description=u'订单未支付')
    ORDER_PAYING = StatusCodeField(404012, 'Order Paying', description=u'订单支付中')
    ORDER_PAY_FAIL = StatusCodeField(404013, 'Order Pay Fail', description=u'微信支付失败')
    # 通知校验状态
    SIGN_CHECK_FAIL = StatusCodeField(404090, 'Sign Check Fail', description=u'签名校验失败')
    FEE_CHECK_FAIL = StatusCodeField(404091, 'FEE Check Fail', description=u'金额校验失败')


class PayStatusCode(BaseStatusCode):
    """ 4041xx 支付相关错误码 """


class WithdrawStatusCode(BaseStatusCode):
    """ 4042xx 提现相关错误码 """
    BALANCE_INSUFFICIENT = StatusCodeField(404200, 'Balance Insufficient', description=u'提现金额不足')


class TokenStatusCode(BaseStatusCode):
    """ 4090xx 票据相关错误码 """
    TOKEN_NOT_FOUND = StatusCodeField(409001, 'Token Not Found', description=u'票据不存在')


class SignatureStatusCode(BaseStatusCode):
    """ 4091xx 签名校验错误 """
    SIGNATURE_ERROR = StatusCodeField(409101, 'Signature Error', description=u'签名错误')


class GVCodeStatusCode(BaseStatusCode):
    """ 4092xx 图形验证码相关错误码 """
    GRAPHIC_VCODE_ERROR = StatusCodeField(409201, 'Graphic VCode Error', description=u'图形验证码错误')


class SVCodeStatusCode(BaseStatusCode):
    """ 4093xx 短信验证码相关错误码 """
    SMS_QUOTA_LIMIT = StatusCodeField(409300, 'SMS Quota Limit', description=u'短信次数超限')
    SMS_VCODE_ERROR = StatusCodeField(409301, 'SMS VCode Error', description=u'验证码错误，请稍后重试')
    SMS_VCODE_HAS_SEND = StatusCodeField(409302, 'SMS VCode Has Send', description=u'验证码已发送，请勿重复获取')


class InsufficientStatusCode(BaseStatusCode):
    """ 4095xx 不足相关错误码 """
    BALANCE_INSUFFICIENT = StatusCodeField(409501, 'Balance Insufficient', description=u'余额不足')
    INTEGRAL_INSUFFICIENT = StatusCodeField(409502, 'Integral Insufficient', description=u'积分不足')


class PermissionStatusCode(BaseStatusCode):
    """ 4099xx 权限相关错误码 """
    PERMISSION_DENIED = StatusCodeField(409900, 'Permission Denied', description=u'权限不足')
    UPLOAD_PERMISSION_DENIED = StatusCodeField(409910, 'Upload Permission Denied', description=u'上传权限不足')
    UPDATE_PERMISSION_DENIED = StatusCodeField(409930, 'Update Permission Denied', description=u'更新权限不足')
