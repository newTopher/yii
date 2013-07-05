<?php
/**
 * Created by IntelliJ IDEA.
 * User: Administrator
 * Date: 13-7-4
 * Time: 下午4:38
 * To change this template use File | Settings | File Templates.
 */
class UserlistController extends Controller{

    public function actionShowFollowers(){
        $muid=Yii::app()->request->getParam('muid','');
        if(!empty($muid)){
            $source=Yii::app()->python->python("Attentionlist::showFollowers",$muid);
        }
        $this->render('followeruserlist',array(
            'userlist'=> $source,
            'muid'=>$muid
        ));
    }

    public function actionShowAttentions(){
        $fuid=Yii::app()->request->getParam('fuid','');
        if(!empty($fuid)){
            $source=Yii::app()->python->python("Attentionlist::showAttentions",$fuid);
        }
        $this->render('attentionuserlist',array(
            'userlist'=> $source,
            'fuid'=>$fuid
        ));
    }
}