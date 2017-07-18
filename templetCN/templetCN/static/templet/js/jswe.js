!(function(e, t) {
    var config = {
        wxconfig: 'http://api.pai.ai/wx/jsapi_signature',
        callback: 'callback'
    }, wxData = {
        debug: false,
        imgUrl: '',
        link: '',
        desc: '',
        title: '',
        timeLine: ''
    }, wxConfig = {
        hide: false,
        close: false
    }, jsApiList = [
        'checkJsApi',
        'onMenuShareTimeline',
        'onMenuShareAppMessage',
        'onMenuShareQQ',
        'onMenuShareWeibo',
        'hideMenuItems',
        'showMenuItems',
        'hideAllNonBaseMenuItem',
        'showAllNonBaseMenuItem',
        'translateVoice',
        'startRecord',
        'stopRecord',
        'onRecordEnd',
        'playVoice',
        'pauseVoice',
        'stopVoice',
        'uploadVoice',
        'downloadVoice',
        'chooseImage',
        'previewImage',
        'uploadImage',
        'downloadImage',
        'getNetworkType',
        'openLocation',
        'getLocation',
        'hideOptionMenu',
        'showOptionMenu',
        'closeWindow',
        'scanQRCode',
        'chooseWXPay',
        'openEnterpriseRedPacket',
        'openProductSpecificView',
        'addCard',
        'chooseCard',
        'openCard'
    ], wxApiFun

    function isOpenOnPC() {  // 判断当前网页是否在 PC 浏览器中打开
        var ua = navigator.userAgent
        return /windows nt/i.test(ua) || /macintosh/i.test(ua) || /linux x86_64/i.test(ua)
    }

    function isOpenInWeixin() {  // 判断当前网页是否在微信内置浏览器中打开
        return /micromessenger/i.test(navigator.userAgent)
    }

    function getWeixinVersion() {
        var ua = navigator.userAgent,
            mt = ua.match(/micromessenger\/([\d.]+)/i)
        return (mt ? mt[1] : '')
    }

    // This function checks whether Wechat is the appointed version or not
    // Cmp: http://jsperf.com/regexp-test-vs-indexof-ignore-upper-and-lower
    function isWeixinVersion(version) {
        // return new RegExp('micromessenger/' + version , 'i').test(navigator.userAgent)
        return navigator.userAgent.toLowerCase().indexOf('micromessenger/' + version) != -1
    }

    function hideOptionMenu() {
        wxConfig.hide = true
        fixedWxData()
    }

    function showOptionMenu() {
        wxConfig.hide = false
        fixedWxData()
    }

    function closeWindow() {
        wxConfig.close = true
        fixedWxData()
    }

    function wxReady(data) {
        data = typeof data === 'object' ? data : JSON.parse(data)
        wx.config({
            debug: wxData.debug,
            appId: data.appId,
            timestamp: data.timestamp,
            nonceStr: data.nonceStr,
            signature: data.signature,
            jsApiList: jsApiList
        })

        var callbacks = {
            trigger: function (res) {
                // alert('用户点击发送给朋友')
                if (JSWE.wxTrigger) {JSWE.wxTrigger(res)}
            },
            success: function (res) {
                // alert('已分享')
                if (JSWE.wxSuccess) {JSWE.wxSuccess(res)}
            },
            cancel: function (res) {
                // alert('已取消')
                if (JSWE.wxCancel) {JSWE.wxCancel(res)}
            },
            fail: function (res) {
                // alert(JSON.stringify(res))
                if (JSWE.wxFail) {JSWE.wxFail(res)}
            }
        }, shareInfo = function(flag) {
            var _share = {
                title: flag ? wxData.title : (wxData.timeLine || wxData.desc),
                link: wxData.link,
                imgUrl: wxData.imgUrl,
                trigger: callbacks.trigger,
                success: callbacks.success,
                cancel: callbacks.cancel,
                fail: callbacks.fail
            }
            if (flag) _share.desc = wxData.desc
            return _share
        }, wxShareApi = function() {
            // 2. 分享接口
            // 2.1 监听“分享给朋友”，按钮点击、自定义分享内容及分享结果接口
            wx.onMenuShareAppMessage(shareInfo(1))
            // 2.2 监听“分享到朋友圈”按钮点击、自定义分享内容及分享结果接口
            wx.onMenuShareTimeline(shareInfo(0))
            // 2.3 监听“分享到QQ”按钮点击、自定义分享内容及分享结果接口
            wx.onMenuShareQQ(shareInfo(1))
            // 2.4 监听“分享到微博”按钮点击、自定义分享内容及分享结果接口
            wx.onMenuShareWeibo(shareInfo(1))
        }, wxMenuApi = function () {
            // 8. 界面操作接口
            // 8.1 隐藏右上角菜单
            // 8.2 显示右上角菜单
            if (wxConfig.hide) {wx.hideOptionMenu()} else {wx.showOptionMenu()}
            // 8.7 关闭当前窗口
            if (wxConfig.close) {wx.closeWindow()}
        }, wxApi = function () {
            wxShareApi()
            wxMenuApi()
        }

        wx.ready(wxApi)

        return wxApiFun = wxApi
    }

    if (isOpenInWeixin() || isOpenOnPC()) {
        if ('undefined' !== typeof JSWE_CONF_UPDATE) JSWE_CONF_UPDATE(config)
        $.ajax({
            url: config.wxconfig,
            type: 'get',
            dataType: 'jsonp',
            jsonpCallback: config.callback,
            data: {
                url: window.location.href.split('#')[0]
            },
            success: wxReady
        })
    }

    function initWxData(data, flag) {
        for(var d in data) {if (d in wxData) wxData[d] = data[d]}
        if (flag) fixedWxData()
    }

    function changeWxData(key, value, flag) {
        if (key in falDwxDataata) {wxData[key] = value}
        if (flag) fixedWxData()
    }

    function fixedWxData() {
        if ('undefined' !== typeof wxApiFun) wxApiFun()
    }

    // 5 图片接口
    // 5.1 拍照、本地选图
    var images = {
        localIds: [],
        serverIds: []
    };
    // function chooseImage(count, directUpload, isShowProgressTips) {
    function chooseImage(choose_params) {
        if ('undefined' === typeof choose_params) choose_params = {}
        wx.chooseImage({
            count: choose_params.count || 9, // 默认9
            sizeType: choose_params.sizeType || ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
            sourceType: choose_params.sourceType || ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
            success: function (res) {
                images.localIds = res.localIds; // 返回选定照片的本地ID列表，localId可以作为img标签的src属性显示图片
                // 判断是否直接上传
                if (choose_params.directUpload) {setTimeout(uploadImages({localIds: images.localIds, isShowProgressTips: choose_params.isShowProgressTips || 1}), 100)}
                // 拍照、本地选图成功后的回调函数
                if (JSWE.wxChooseImageSuccess) {JSWE.wxChooseImageSuccess(res)}
            }
        });
    }

    // 5.2 图片预览
    function previewImage(preview_params) {
        wx.previewImage({
            current: preview_params.current, // 当前显示图片的链接，不填则默认为 urls 的第一张
            urls: preview_params.urls // 需要预览的图片链接列表
        });
    }

    // 5.3 上传图片
    // function uploadImage(localId, isShowProgressTips) {
    function uploadImage(upload_params) {
        // 上传图片为异步处理，重复上传同一图片，返回的serverId也是不同的
        wx.uploadImage({
            localId: upload_params.localId, // 需要上传的图片的本地ID，由chooseImage接口获得
            isShowProgressTips: upload_params.isShowProgressTips || 1, // 默认为1，显示进度提示
            success: function (res) {
                images.serverIds.push(res.serverId); // 返回图片的服务器端ID
                // 上传图片成功后的回调函数
                if (JSWE.wxUploadImageSuccess) {JSWE.wxUploadImageSuccess(res)}
            }
        });
    }

    // function uploadImages(localIds, isShowProgressTips) {
    function uploadImages(upload_params) {
        var localIds = upload_params.localIds, isShowProgressTips = upload_params.isShowProgressTips || 1
        images.serverIds = [];
        for (var idx in localIds) {uploadImage({localId: localIds[idx], isShowProgressTips: isShowProgressTips})}
    }

    // 9 微信原生接口
    // 9.1.1 扫描二维码并返回结果
    // 9.1.2 扫描二维码并返回结果
    function　scanQRCode(scan_params) {
        if ('undefined' === typeof scan_params) scan_params = {}
        wx.scanQRCode({
            needResult: scan_params.needResult || 0,  // 默认为0，0扫描结果由微信处理，1直接返回扫描结果
            scanType: scan_params.scanType || ['qrCode', 'barCode'],  // 可以指定扫二维码还是一维码，默认二者都有
            success: function (res) {  // 当 needResult 为 1 时，扫码返回的结果
                if (JSWE.wxScanQRCodeSuccess) {JSWE.wxScanQRCodeSuccess(res)}
            }
        });
    }

    // QRCode & BarCode is different
    function parseScanQRCodeResultStr(resultStr) {
        var strs = resultStr.split(',')
        return strs[strs.length - 1]
    }

    // 10 微信支付接口
    // 10.1 发起一个支付请求
    function　chooseWXPay(wxpay_params) {
        wx.chooseWXPay({
            timestamp: wxpay_params.timeStamp, // 支付签名时间戳，注意微信jssdk中的所有使用timestamp字段均为小写。但最新版的支付后台生成签名使用的timeStamp字段名需大写其中的S字符
            nonceStr: wxpay_params.nonceStr, // 支付签名随机串，不长于 32 位
            package: wxpay_params.package, // 统一支付接口返回的prepay_id参数值，提交格式如：prepay_id=***）
            signType: wxpay_params.signType, // 签名方式，默认为'SHA1'，使用新版支付需传入'MD5'
            paySign: wxpay_params.paySign, // 支付签名
            success: function (res) {
                // 支付成功后的回调函数
                if (JSWE.wxPaySuccess) {JSWE.wxPaySuccess(res)}
            }
        })
    }

    // xx 微信原生企业红包接口
    // xx.1 发起一个发送原生企业红包请求
    function　openEnterpriseRedPacket(wxredpack_params) {
        wx.openEnterpriseRedPacket({
            timeStamp: wxredpack_params.timeStamp, // 红包签名时间戳，注意原生企业红包接口timeStamp字段名需大写其中的S字符，而支付接口timeStamp字段名无需大写其中的S字符。但最新版的支付后台生成签名使用的timeStamp字段名需大写其中的S字符
            nonceStr: wxredpack_params.nonceStr, // 红包签名随机串，不长于 32 位
            package: encodeURIComponent(wxredpack_params.package), // 发放红包接口返回的prepay_id参数值，提交格式如：prepay_id=***）
            signType: wxredpack_params.signType, // 签名方式，默认为'SHA1'，使用新版支付需传入'MD5'
            paySign: wxredpack_params.paySign, // 红包签名
            success: function (res) {
                // 发送原生企业红包成功后的回调函数
                if (JSWE.wxEnterpriseRedPacketSuccess) {JSWE.wxEnterpriseRedPacketSuccess(res)}
            }
        })
    }

    var v = {
        version: '1.0.5',

        // Basic Vars
        config: config,
        wxData: wxData,
        jsApiList: jsApiList,

        // Weixin Function
        isOpenInWeixin: isOpenInWeixin,
        getWeixinVersion: getWeixinVersion,
        isWeixinVersion: isWeixinVersion,

        // Menu Function
        hideOptionMenu: hideOptionMenu,
        showOptionMenu: showOptionMenu,
        closeWindow: closeWindow,

        // Share Function
        initWxData: initWxData,
        changeWxData: changeWxData,
        fixedWxData: fixedWxData,

        // Image Function
        images: images,
        chooseImage: chooseImage,
        previewImage: previewImage,
        uploadImage: uploadImage,
        uploadImages: uploadImages,

        // Scan Function
        scanQRCode: scanQRCode,
        parseScanQRCodeResultStr: parseScanQRCodeResultStr,

        // Pay Function
        chooseWXPay: chooseWXPay,

        // EnterpriseRedPacket Function
        openEnterpriseRedPacket: openEnterpriseRedPacket
    }
    e.JSWE = e.V = v
})(window)
