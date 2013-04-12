<?php

define('PYTHON_SERVER_HOST','127.0.0.1');
define('PYTHON_SERVER_PORT','21230');
define("PARAM_TYPE_ERROR", 101);
define("SOCKET_ERROR", 102);
define("PYTHON_SERVER_EXCEPTION", 104);

$yii=dirname(__FILE__).'/../framework/yii.php';
$config=dirname(__FILE__).'/protected/config/test.php';

// remove the following line when in production mode
defined('YII_DEBUG') or define('YII_DEBUG',true);

require_once($yii);
Yii::createWebApplication($config)->run();
