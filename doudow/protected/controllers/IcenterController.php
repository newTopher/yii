<?php
/*
 * 微博模块
 */
class IcenterController extends Controller{


     public function actionIcenter(){
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
         if($videoUrl || $musicUrl){
             $other=array('videoUrl'=>$videoUrl,'musicUrl'=>$musicUrl);
             $postData['other_attr']=$this->encode($other);
         }
         $postData['source']='Android';

         $resourceWeibo=Yii::app()->python->python("Weibo::publishNewWeibo",$postData);
		 if(is_array($resourceWeibo)){
			$resourceUser=Yii::app()->python->python("User::getUser",$resourceWeibo['uid']);
			if(is_array($resourceUser)){
				$resourceWeibo['user']=$resourceUser;
				$result['code']=0;
				$result['msg']='publish weibo success';
				$result['data']=$resourceWeibo;
			}else{
				$result['code']=$resourceWeibo;
				$result['msg']='get user info error';
			}
		 }else{
			$result['code']=$resourceWeibo;
            $result['msg']='publish weibo error';	
		 }

         return $this->rebackData($result);

     }

     public function actionRepostWeibo(){
         $postData['uid']=Yii::app()->request->getParam('uid','10');
         $postData['text']=urlencode(Yii::app()->request->getParam('weibocontents'));
         $postData['create_time']=time();
         $postData['w_id']=7;
         $postData['source']='Android';
         if(defined('OPEN_MEMCACHE')){
             $memcache=Yii::app()->memcache->getMemcache();
             $key=Yii::app()->memcache->createKey();
             if($memcache->set($key,$postData)){
                 $result=$memcache->get($key);
             }else{
                 $result['code']=-1;
                 $result['msg']='memcache error';
             }
         }else{
             $resourceWeibo=Yii::app()->python->python("Weibo::repostWeibo",$postData);
             if(is_array($resourceWeibo)){
                $result['msg']='repost weibo success';
                $result['data']=$resourceWeibo;
             }else{
                $result['code']=$resourceWeibo;
                $result['msg']='publish weibo error';
             }
         }

         return $this->rebackData($result);

     }

     public function actionDestroyWeibo(){
         $wid=Yii::app()->request->getParam('w_id');
         $resourceWeibo=Yii::app()->python->python("Weibo::destroyWeibo",$wid);
         if($resourceWeibo){
             $result['code']=0;
             $result['msg']='delete weibo success';
         }else{
             $result['msg']='delete weibo fail';
         }
         return $this->rebackData($result);
     }
}