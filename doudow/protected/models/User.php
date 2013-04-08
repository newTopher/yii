<?php
/*
 * dod_user模型
 */
class User extends CActiveRecord{
    public static function model($className=__class__){
        return parent::model($className);
    }

    public function tableName(){
        return 'dod_user';
    }

    public function primaryKey(){
        return 'id';
    }

    public function getByUsername($username){
        return User::model()->findByAttributes(array('username'=>$username),'username=:username',array(':username'=>$username));
    }

    public function getByEmail($email){
        return User::model()->findByAttributes(array('email'=>$email),'email=:email',array(':email'=>$email));
    }
}