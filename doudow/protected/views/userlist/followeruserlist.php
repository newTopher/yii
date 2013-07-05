<html>
<head>
<title>粉丝列表</title>

</head>
<body>
 <h1>粉丝列表</h1>
 <span>
     <?php foreach($userlist as $value):?>
     <div>用户名:<a href=""><?php echo $value['username']; ?></a>--- 用户id:<?php echo $value['id']; ?></div>
     <?php endforeach; ?>
 </span>
</body>
</html>