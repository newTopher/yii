<?php
/*
 * 登陆模块
 */
class LoginController extends Controller{

    /*
     * 登陆页面
     */
    public function actionShowLogin(){
        $this->render("login");
    }


    /*
     * 登陆
     */
    public function actionLogin(){
        $postData=array();
        $postData['email']=Yii::app()->request->getParam('email');
        $postData['password']=Yii::app()->request->getParam('password');

        $resource=Yii::app()->python->python("User::userLogin",$postData);
        if(is_array($resource)){
            $result['code']=0;
            $result['msg']='login success';
            $result['data']=$resource;
        }else{
            $result['code']=-1;
            $result['msg']='login fail,username or password error';
        }

        return $this->rebackData($result);

    }



}
