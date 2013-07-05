<html>
<head>
<title>关注列表</title>

</head>
<body>
 <h1>关注列表</h1>
 <span>
     <?php foreach($userlist as $value):?>
     <div>用户名:<a href=""><?php echo $value['username']; ?></a>--- 用户id:<?php echo $value['id']; ?>---
         <a href="<?php echo Yii::app()->createUrl('Attention/CancelAttention',array('fuid'=>$fuid,'muid'=>$value['id'])); ?>">取消关注</a> </div>
     <?php endforeach; ?>
 </span>
</body>
</html>