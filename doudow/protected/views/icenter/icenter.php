<html>
    <head>
        <title>icenter</title>
    </head>
<body>
    <h1>Icenter</h1>
    转发微博
    <?php echo CHtml::beginForm('repostWeibo','post'); ?>
    内容:<?php echo CHtml::textField('weibocontents');  ?><br>
    用户ID:<?php echo CHtml::textField('uid');  ?><br>
    转发ID:<?php echo CHtml::textField('w_id');  ?><br>
    <?php echo CHtml::submitButton('publish');  ?>
    <?php echo CHtml::endForm();    ?>

</body>



</html>