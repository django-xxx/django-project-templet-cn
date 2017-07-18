# -*- coding: utf-8 -*-

from StatusCode import BaseStatusCode, StatusCodeField


class ProfileStatusCode(BaseStatusCode):
    """ 用户相关错误码 4001xx """
    PROFILE_NOT_FOUND = StatusCodeField(400101, 'Profile Not Found', description=u'用户不存在')
    # 手机号
    PHONE_ALREADY_EXISTS = StatusCodeField(400105, 'Phone Already Exists', description=u'手机号已经存在')


class OrderStatusCode(BaseStatusCode):
    """ 订单／支付相关错误码 4040xx """
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
    """ 支付相关错误码 4041xx """


class WithdrawStatusCode(BaseStatusCode):
    """ 提现相关错误码 4042xx """
    BALANCE_INSUFFICIENT = StatusCodeField(404200, 'Balance Insufficient', description=u'提现金额不足')


class TokenStatusCode(BaseStatusCode):
    """ 票据相关错误码 4090xx """
    TOKEN_NOT_FOUND = StatusCodeField(409901, 'Token Not Found', description=u'票据不存在')
