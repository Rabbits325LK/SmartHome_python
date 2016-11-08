$(function(){
    console.info("loading script.js file...");
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username":user, "password":pwd};
        $.ajax({
            type:'post',
            url : '/',
            data : pd,
            cache : false,
            dataType : 'JSON',
            success : function(result){
                console.info(result);
                if(result.success == 'true'){
                    window.location.href = "/user?user="+result.data;    
                }else{
                    UIkit.notify("<i class='uk-icon-exclamation-triangle'></i> "+result.data,{status:'danger',timeout:3000,pos:'top-center'});
                }
            },
            error:function(){ 
                UIkit.notify("<i class='uk-icon-exclamation-triangle'></i> 网络错误",{status:'danger',timeout:3000,pos:'top-center'});
            }
        });
    });
});