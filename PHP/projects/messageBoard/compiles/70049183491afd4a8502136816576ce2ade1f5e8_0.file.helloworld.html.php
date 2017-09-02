<?php
/* Smarty version 3.1.31, created on 2017-08-01 19:51:55
  from "C:\others\githubDOC\PHP\projects\messageBoard\templates\helloworld.html" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.31',
  'unifunc' => 'content_59806b5b81e471_13545293',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '70049183491afd4a8502136816576ce2ade1f5e8' => 
    array (
      0 => 'C:\\others\\githubDOC\\PHP\\projects\\messageBoard\\templates\\helloworld.html',
      1 => 1501588313,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_59806b5b81e471_13545293 (Smarty_Internal_Template $_smarty_tpl) {
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>helloworld</title>
</head>
<body>
    <!--hello,<?php echo $_smarty_tpl->tpl_vars['name']->value;?>
-->
    <p>数据为</p>:
    <?php echo $_smarty_tpl->tpl_vars['comments']->value[0]["id"];?>

    <?php echo $_smarty_tpl->tpl_vars['comments']->value[0]['name'];?>

    <!--<?php echo $_smarty_tpl->tpl_vars['comments']->value[0][(isset($_smarty_tpl->tpl_vars['__smarty_section_reply']->value['index']) ? $_smarty_tpl->tpl_vars['__smarty_section_reply']->value['index'] : null)];?>
-->
</body>
</html><?php }
}
