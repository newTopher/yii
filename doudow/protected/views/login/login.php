<html>
    <body>
        <h1>login</h1>
        <?php echo CHtml::beginForm('login','post'); ?>
        email:<?php echo CHtml::textField('email');  ?><br>
        password:<?php echo CHtml::passwordField('password');  ?><br>
        <?php echo CHtml::submitButton('login');  ?>
        <?php echo CHtml::endForm();    ?>
    </body>
</html>