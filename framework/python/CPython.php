<?php
/*
 * python处理组件
 */
class CPython extends CComponent{

    private static $_socket;

    public function init(){

    }

    public function python(){
        $argsLen=func_num_args();
        $argsArray=func_get_args();
        if($argsLen<1){
            throw new CException(Yii::t('python',"参数不能少于1"));
        }
        if(!is_string($argsArray[0])){
            throw new CException(Yii::t('python',"第一二个参数为python模块参数必须为字符串"));
        }
        if(self::$_socket===null){
            self::createSocket();
        }
        if(socket_connect(self::$_socket,PYTHON_SERVER_HOST,PYTHON_SERVER_PORT) === false){
            throw new CException(Yii::t('python',"socket连接失败"));
        }
        $request=serialize($argsArray);
        $requestLen=strlen($request);
        $request=$requestLen.','.$request;
        echo $request;

    }

    private static function createSocket(){
        try{
            self::$_socket=socket_create(AF_INET,SOCK_STREAM,0);
        }catch (CException $e){
            throw new CException(Yii::t('python',"socket创建失败"));
        }
    }



}