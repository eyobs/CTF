<?php



function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
$e = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
json_encode($e);

$str = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSFVl8REENaAw=';
echo json_decode(xor_encrypt(base64_decode($str)));
?>


