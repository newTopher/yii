<?php
/*
 * python处理组件
 */
class CPython extends CComponent{

    private $_socket;

    public function init(){

    }

    public function __destruct(){
        $this->_socket=null;
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
        if($this->_socket===null){
            $this->createSocket();
        }
        if(socket_connect($this->_socket,PYTHON_SERVER_HOST,PYTHON_SERVER_PORT) === false){
            throw new CException(Yii::t('python',"socket连接失败"));
        }
        $request=serialize($argsArray);
        $requestLen=strlen($request);
        $request=$requestLen.','.$request;
		$response=$this->sends($request);
        $this->_socket=null;
		return $this->response($response);		
    }

    private function createSocket(){
        try{
            $this->_socket=socket_create(AF_INET,SOCK_STREAM,0);
        }catch (CException $e){
            throw new CException(Yii::t('python',"socket创建失败"));
        }
    }

	private function sends($request){
		$requestLen=strlen($request);
		$sendLen=0;
		do{
			if(($sends=socket_write($this->_socket,$request,strlen($request))) === false){
				throw new CException(Yii::t('python',SOCKET_ERROR));
			}
			$sendLen+=$sends;
			$request=substr($request,$sends);
		}while($sendLen<$requestLen);

        $response = "";
		if (($response = socket_read($this->_socket,1400)) == false){
			throw new CException(Yii::t('python',"socket创建失败"));
		}
		if ($response == ""){
            throw new CException(Yii::t('python',"接受内容为空"));
		}
		$this->close();
		return $response;
	}

	private function response($response){
		$status=substr($response,0,1);
		$msg=substr($response,1);
		if($status == 'F'){
			throw new CException(Yii::t('python',$msg));
		}else{
			if($msg != 'N'){
				 return unserialize($msg);
			}
		}
	}


	private function close(){
		socket_close($this->_socket);
	}



}