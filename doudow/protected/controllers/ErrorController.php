<?php
/*
 * 错误处理
 */
class ErrorController extends Controller{

    public function actionError(){
        $result=array();
        $result['code']='-1';
        $result['msg']='请求非法';
        $this->rebackData($result);
    }
}