<?php
class IndexController extends Controller{

    public function actionIndex(){
        $rs=Yii::app()->python->python("User::validUserName",5);
		print_r($rs);
    }



}