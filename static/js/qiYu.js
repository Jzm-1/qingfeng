//七鱼客服
(function (w, d, n, a, j) {
    w[n] = w[n] || function () {
        (w[n].a = w[n].a || []).push(arguments);
    };
    j = d.createElement('script');
    j.async = true;
    j.src ='https://qiyukf.com/script/a2c587490ed80490f9097c01191beb40.js?hidden=1';
    d.body.appendChild(j);
})(window, document, 'ysf');


var userInfo={
    encryptUserId:"",
    userName:"",
    scene:"",
    type:"个人"
};

function qiYuOpen(){
    var newWindow = window.open();
    //先获取用户id等相关信息
    $.ajax({
        type: 'POST',
        url:"/userBase/user/qiYu/userInfo",
        success:function(result){
            if(result.responseCode=='0000'){
                qiYuConfig(result.object);
                //window.open(ysf('url'));
                newWindow.location.href =ysf('url');
                //ysf.open();
            }else{
                qiYuConfig(userInfo);
                newWindow.location.href =ysf('url');
                //ysf.open();
            }
        },
        error:function () {
            qiYuConfig(userInfo);
            newWindow.location.href =ysf('url');
            //ysf.open();
        }
    });

}

/**
 * 登录状态或者解锁码状态
 * @param encryptUserId
 * @param scene
 */
function qiYuUrlOpen(encryptUserId,scene){
    //先获取用户id等相关信息
    //ysf.open();
    userInfo.encryptUserId=encryptUserId;
    userInfo.scene=scene;
    userInfo.userName="";
    qiYuConfig(userInfo);

}

function qiYuUrlNoLogin(){
    //先获取用户id等相关信息
    qiYuConfig(userInfo);

}

/**
 * 自定义信息
 * @param userInfo
 */
function qiYuConfig(userInfo){
    ysf('logoff');
    if(userInfo.encryptUserId=='visitor'){
        return;
    }
    var userType="商户";
    if(userInfo.type!=undefined&&userInfo.type!=null){
        userType=userInfo.type==1?"商户":userInfo.type==2?"个人":"选号";
    }

    ysf('config', {
        "uid":encodeURIComponent(userInfo.encryptUserId),
        "data":JSON.stringify([
            {"key":"real_name", "value":userInfo.userName},
            {"key":"mobile_phone", "hidden":true},
            {"key":"email", "hidden":true},
            {"index":0, "key":"type", "label":"用户类型", "value":userType},
            {"type":"crm_param", "key":"scene", "label":"场景", "value":userInfo.scene}
        ])
    });
}