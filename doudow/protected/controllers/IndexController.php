<?php
class IndexController extends Controller{

    public function actionIndex(){
        $rs=Yii::app()->python->python("User::validUserName",1);
		echo $rs;
    }



}