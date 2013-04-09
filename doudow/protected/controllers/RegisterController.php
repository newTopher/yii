<?php
/*
 * 注册模块
 */
class RegisterController extends Controller{
    /*
     * 验证用户名
     */
    public function actionValidUsername($username){
         $userModel=new User();
         $result=array();
         if($userModel->getByUsername($username)){
             $result['code']=1;
             $result['msg']='success';
         }else{
             $result['code']=0;
             $result['msg']='success';
         }
         return $this->rebackData($result);
      }

    /*
     * 验证邮箱
     */
    public function actionValidEmail($email){
         $userModel=new User();
         $result=array();
         if($userModel->getByEmail($email)){
             $result['code']=1;
             $result['msg']='success';
         }else{
             $result['code']=0;
             $result['msg']='success';
         }
         return $this->rebackData($result);
    }

    /*
     * 注册页面显示
     */
    public function actionShowReg(){
         $this->render("reg");
    }

    /*
     * 注册
     */
    public function actionReg(){
        echo $username=Yii::app()->request->getParam('username');

    }



}