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
    转发微博
    <?php echo CHtml::beginForm('publishNewWeibo','post'); ?>
    内容:<?php echo CHtml::textField('weibocontents');  ?><br>
    <?php echo CHtml::submitButton('publish');  ?>
    <?php echo CHtml::endForm();    ?>

    <div>
            <span>这是第一条微博</span>  <a href="">转发</a> <a href="">评论</a><br>
            <span>这是第二条微博</span>  <a href="">转发</a> <a href="">评论</a><br>
            <span>这是第三条微博</span>  <a href="">转发</a> <a href="">评论</a><br>
    </div>

</body>



</html>