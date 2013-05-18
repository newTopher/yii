<?php
/**
 * Controller is the customized base controller class.
 * All controller classes for this application should extend from this base class.
 */
class Controller extends CController
{
	/**
	 * @var string the default layout for the controller view. Defaults to '//layouts/column1',
	 * meaning using a single column layout. See 'protected/views/layouts/column1.php'.
	 */
	public $layout='//layouts/column1';
	/**
	 * @var array context menu items. This property will be assigned to {@link CMenu::items}.
	 */
	public $menu=array();
	/**
	 * @var array the breadcrumbs of the current page. The value of this property will
	 * be assigned to {@link CBreadcrumbs::links}. Please refer to {@link CBreadcrumbs::links}
	 * for more details on how to specify this property.
	 */
	public $breadcrumbs=array();

    const INNERREQUST = 1;  //返回数组
    const OUTREQUEST  = 0;  //返回json数据


    public function encode($var) {
        switch (gettype($var)) {
            case 'boolean':
                return $var ? 'true' : 'false'; // Lowercase necessary!
            case 'integer':
            case 'double':
                return sprintf( '"%s"', $var);
            case 'resource':
            case 'string':
                return '"'. str_replace(array("\r", "\n", "\t", '\\\'', "/"),
                    array('\r', '\n', '\t', '\'', '\\/'),
                    addslashes($var)) .'"';
            case 'array':
                // Arrays in JSON can't be associative. If the array is empty or if it
                // has sequential whole number keys starting with 0, it's not associative
                // so we can go ahead and convert it as an array.
                if ( empty ($var) || array_keys($var) === range(0, sizeof($var) - 1)) {
                    $output = array();
                    foreach ($var as $v) {
                        $output[] = $this->encode($v);
                    }
                    return '['. implode(',', $output) .']';
                }
            // Otherwise, fall through to convert the array as an object.
            case 'object':
                $output = array();
                foreach ($var as $k => $v) {
                    $output[] =  $this->encode(strval($k)) .':'.  $this->encode($v);
                }
                return '{'. implode(',', $output) .'}';
            default:
                return 'null';
        }
    }

    public function decode( $var, $assoc = false) {
        return json_deocde( $var, $assoc);
    }


    public function rebackData($array,$data=null,$type=self::OUTREQUEST){
        if($data != null && $type=self::INNERREQUST){
           return $data;
        }else{
            echo $this->encode($array);
        }
    }

}