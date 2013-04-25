<html>
    <head>
        <title>icenter</title>
    </head>
<body>
    <h1>Icenter</h1>
    发布微博
    <?php echo CHtml::beginForm('publishnewweibo','post'); ?>
    内容:<?php echo CHtml::textField('weibocontents');  ?><br>
    用户ID:<?php echo CHtml::textField('uid');  ?><br>
    <?php echo CHtml::submitButton('publish');  ?>
    <?php echo CHtml::endForm();    ?>

</body>



</html>