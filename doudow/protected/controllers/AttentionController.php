<?php
/**
 * Created by IntelliJ IDEA.
 * User: Administrator
 * Date: 13-7-3
 * Time: 下午3:10
 * To change this template use File | Settings | File Templates.
 */
class AttentionController extends Controller{
    /*
     * 取消关注
    */
    public function actionCancelAttention(){
        $muid=Yii::app()->request->getParam('muid','');
        $fuid=Yii::app()->request->getParam('fuid','');
        if(!empty($muid) && !empty($fuid)){
            $uids=array('muid'=>$muid,'fuid'=>$fuid);
            $source=Yii::app()->python->python("Attentionlist::cancelAttention",$uids);
            if($source){
                echo '取消成功';
            }else{
                echo '取消失败';
            }
        }else{
            throw new CException(Yii::t('yii','取消关注参数不能为空，取消关注失败'));
        }
    }

    public function actionAddAttention(){
        $muid=Yii::app()->request->getParam('muid','');
        $fuid=Yii::app()->request->getParam('fuid','');
        if(!empty($muid) && !empty($fuid)){
            $uids=array('muid'=>$muid,'fuid'=>$fuid);
            $source=Yii::app()->python->python("Attentionlist::addAttention",$uids);
            if($source){
                echo '关注成功';
            }else{
                echo '关注失败';
            }
        }else{
            throw new CException(Yii::t('yii','关注参数不能为空，关注失败'));
        }
    }
}