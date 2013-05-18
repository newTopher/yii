<?php
/*
 * 微博模块
 */
class IcenterController extends Controller{


     public function actionIcenter(){
         $user=Yii::app()->session['uid'];
         $attentionUserList=Yii::app()->python->python("Attentionlist::getUserAttentionList",$user['id']);
         if(is_array($attentionUserList)){
             $pageInfo=array();
             $pageInfo['page']=Yii::app()->request->getParam('page',1);
             $pageInfo['everyPageRows']=25;
             $newWeiboList=Yii::app()->python->python("Weibo::getCurrNewWeiboList",$attentionUserList,$pageInfo);
         }else{
             throw new CException(Yii::t('yii','获取用户关注列表失败 weibo error'));
         }
         $this->render('icenter',array(
             'username'=>$user['username'],
             'name'    =>$user['name'],
             'userSign'=>$user['user_sign'],
             'followersCounts'=>$user['followers_counts'],
             'attentionCounts'=>$user['attention_counts']
         ));
     }

     public function actionPublishNewWeibo(){
         $postData['uid']=Yii::app()->session['uid']['id'];
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
			//$resourceUser=Yii::app()->python->python("User::getUser",$resourceWeibo['uid']);
            /*
            if(!defined('REST')){
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

            }
            */
            $resourceWeibo['user']=Yii::app()->session['uid'];
            $result['code']=0;
            $result['data']=$resourceWeibo;
            $this->rebackData($result);

		 }else{
             throw new CException(Yii::t('yii','publish weibo error'));
		 }

     }

     public function actionRepostWeibo(){
         $postData['uid']=Yii::app()->session['uid']['id'];
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