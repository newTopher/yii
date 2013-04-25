<?php
/*
 * 注册模块
 */
class RegisterController extends Controller{
    /*
     * 验证用户名
     */
    public function actionValidUsername($username){
        $resource=Yii::app()->python->python("User::validUserName",$username);
        if($resource){
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
        $resource=Yii::app()->python->python("User::validEmail",$email);
        if($resource){
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
     * 根据城市获取学校列表
     */
    public function actionSchoolList($cid){
        if(!empty($cid) && is_numeric($cid)){
            $resource=Yii::app()->python->python("School::schoolList",$cid);
            $result['code']=1;
            $result['msg']='success';
            $result['data']=$resource;
            return $this->rebackData($result);
        }
    }

    /*
     * 注册方法
     */
    public function actionReg(){
        $postData=array();
        $postData['username']=Yii::app()->request->getParam('username');
        $postData['email']=Yii::app()->request->getParam('email');
        $postData['password']=Yii::app()->request->getParam('password');
        $repassword=Yii::app()->request->getParam('repassword');
        $postData['name']=Yii::app()->request->getParam('name');
        $postData['sex']=Yii::app()->request->getParam('sex');
        $postData['school_id']=Yii::app()->request->getParam('school_id');
        $postData['grate']=Yii::app()->request->getParam('grade');
        $postData['birthday']=Yii::app()->request->getParam('birthday');
        $postData['user_sign']='';
        $postData['details']='';
        $postData['head_img']='';
        $postData['is_active']=0;

        if(!Yii::app()->python->python("User::validUserName",$postData['username'])){
            $result['code']=-1;
            $result['msg']='register fail,username is exists';
            return $this->rebackData($result);
        }

        if(!Yii::app()->python->python("User::validEmail",$postData['email'])){
            $result['code']=-1;
            $result['msg']='register fail,email is exists';
            return $this->rebackData($result);
        }

        $resource=Yii::app()->python->python("User::userReg",$postData);

        if(!$resource){
            $result['code']=-1;
            $result['msg']='register fail';
        }else{
            $result['code']=0;
            $result['msg']='register success';
            $result['data']=array('id'=>$resource);
        }

        return $this->rebackData($result);


    }



}