<html>
    <head>
        <title>个人中心</title>
        <style type="text/css">
            .nickname{
                width: 80px;
                height: 50px;
                line-height: 50px;
                color:#228b22;
                display: inline-block;
            }
            .nickname a{
                font-size: 16px;
                font-weight: bold;
                color: #228b22;
            }
            .repost_box{
                display: none;
            }
            .repostid a{
                color: #cd5c5c;
            }
        </style>
        <script type="text/javascript">
             $(function(){
                 $("#repostid a").each(function(i,o){
                     $(o).click(function(){
                         $(this).next().show();
                     });
                 });
             });
        </script>
    </head>
<body>
    用户名:<a href="<?php echo $uid ;?>"><?php echo $username; ?></a><br>
    姓名:<?php echo $name; ?> <a href="<?php echo Yii::app()->createUrl('Login/Logout'); ?>">退出</a> <br>
    个性签名:<?php echo $userSign; ?><br>
    粉丝数:<a href=""><?php echo $followersCounts ?></a><br>
    关注数:<a href=""><?php echo $attentionCounts ?></a><br>
    <h1>个人中心</h1>
    发布微博
    <?php echo CHtml::beginForm('publishNewWeibo','post'); ?>
    内容:<?php echo CHtml::textField('weibocontents');  ?><br>
    <?php echo CHtml::submitButton('发表');  ?>
    <?php echo CHtml::endForm();    ?>

    <div>
            <?php foreach($newWeiboList as $k=>$v):?>
            <span class="nickname">
                <a href='<?php echo Yii::app()->createUrl('icenter/icenter',array('uid'=>$v['uid'])); ?>'><?php echo $v['username'] ;?></a>&nbsp;&nbsp;
            </span>
            <?php if($v['uid'] != $uid): ?>
            <a href="<?php echo Yii::app()->createUrl('Attention/CancelAttention',array('muid'=>$v['uid'],'fuid'=>$uid)); ?>">取消关注</a>
            <?php endif; ?>
            微博内容：<?php echo $v['text']; ?>--- 发送时间:<?php echo $v['create_time']; ?>
            --  当前微博ID:<font color="#ff4500"><?php echo $v['w_id'];?></font>---转发微博ID:<font color="#8b0000"><?php echo $v['retweeted_status']; ?></font>
            <span id="repostid" class="repostid">
                <a href="javascript::void();">转发(<?php echo $v['reposts_counts'] ; ?>)</a>
                <span class="repost_box">
                    <?php echo CHtml::beginForm('RepostWeibo','post'); ?>
                    <?php echo CHtml::hiddenField('w_id',$v['w_id']); ?>
                    转发内容:<?php echo CHtml::textField('weibocontents');  ?><br>
                    <?php echo CHtml::submitButton('转发');  ?>
                    <?php echo CHtml::endForm();    ?>
                </span>
            </span>
            <span id="commentsid" class="commentsid">
                <a href="javascript::void();">评论(<?php echo $v['comments_counts'] ; ?>)</a>
                <span class="repost_box">
                    <?php echo CHtml::beginForm('RepostWeibo','post'); ?>
                    <?php echo CHtml::hiddenField('w_id',$v['w_id']); ?>
                    转发内容:<?php echo CHtml::textField('weibocontents');  ?><br>
                    <?php echo CHtml::submitButton('转发');  ?>
                    <?php echo CHtml::endForm();    ?>
                </span>
            </span>
            <br>
            <?php endforeach ?>
    </div>

</body>



</html>