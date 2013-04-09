<html>
    <body>
         <h1>register</h1>
         <?php echo CHtml::beginForm('reg','post'); ?>
         username:<?php echo CHtml::textField('username');  ?><br>
         email:<?php echo CHtml::textField('email');  ?><br>
         password:<?php echo CHtml::passwordField('password');  ?><br>
         repassword:<?php echo CHtml::passwordField('repassword');  ?><br>
         name:<?php echo CHtml::textField('name');  ?><br>
         sex:<?php echo CHtml::radioButtonList('sex','1',array(1=>'男',2=>'女'));  ?><br>
         school:<?php echo CHtml::textField('school_id');  ?><br>
         grade:<?php echo CHtml::textField('grade');  ?><br>
         birthday:<?php echo CHtml::textField('birthday');  ?><br>
         <?php echo CHtml::submitButton('register');  ?>
         <?php echo CHtml::endForm();    ?>
    </body>
</html>