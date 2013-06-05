<html>
    <head>
        <title>icenter</title>
    </head>
<body>
    用户名:<?php echo $username; ?><br>
    姓名:<?php echo $name; ?><br>
    个性签名:<?php echo $userSign; ?><br>
    粉丝数:<a href=""><?php echo $followersCounts ?></a><br>
    关注数:<a href=""><?php echo $attentionCounts ?></a><br>
    <h1>Icenter</h1>
    发布微博
    <?php echo CHtml::beginForm('publishNewWeibo','post'); ?>
    内容:<?php echo CHtml::textField('weibocontents');  ?><br>
    <?php echo CHtml::submitButton('publish');  ?>
    <?php echo CHtml::endForm();    ?>

    <div>
            <?php foreach($newWeiboList as $k=>$v):?>
            <span><?php echo $v['text'] ?></span>  <a href="<?php echo Yii::app()->createUrl('Icenter/RepostWeibo',array('w_id'=>$v['w_id']))?>">转发</a> <a href="">评论</a><br>
            <?php endforeach ?>
    </div>

</body>



</html>