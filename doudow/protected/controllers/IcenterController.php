<?php
/*
 * 微博模块
 */
class IcenterController extends Controller{


     public function actionicenter(){
         $this->render('icenter');
     }

     public function actionPublishNewWeibo(){
         $postData['uid']=Yii::app()->request->getParam('uid');
         $postData['text']=urlencode(Yii::app()->request->getParam('weibocontents'));
         $postData['create_time']=time();
         $pics=array('sourceImg'=>'source.jpg','thumbImg'=>'thumb.jpg','largeImg'=>'large.jpg');
         if(isset($pics)){
             $postData['pics']=$this->encode($pics);
         }else{
             $postData['pics']='';
         }
         $videoUrl="http://www.youku.com";
         $musicUrl="http://www.mp3.com";
         $other=array('videoUrl'=>$videoUrl,'musicUrl'=>$musicUrl);
         $postData['other_attr']=$this->encode($other);
         print_r($postData['other_attr']);

     }
}