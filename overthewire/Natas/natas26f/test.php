<?php

class Test
{
    public $name = 'eyob';
}

$object = new Test;
var_dump($object);   // object
var_dump(serialize($object));   // serialized object

?>