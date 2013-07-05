<?php
/**
 * Created by IntelliJ IDEA.
 * User: Administrator
 * Date: 13-7-5
 * Time: 下午2:12
 * To change this template use File | Settings | File Templates.
 */
class CommentController extends Controller{

    public function  actionPubComment(){
        if(Yii::app()->request->getIsPostRequest()){
           $uid=Yii::app()->request->getParam('uid','');
           $wid=Yii::app()->request->getParam('w_id','');
           $commentContents=Yii::app()->request->getParam('comment_contents','');
           if(!empty($uid) && !empty($wid) && !empty($commentContents)){
               $source=Yii::app()->python->python();
           }
        }
    }
}