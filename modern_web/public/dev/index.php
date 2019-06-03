<?php

//$bro = get_browser($_SERVER['HTTP_USER_AGENT'].'\n\n');

//var_dump($_SERVER['HTTP_USER_AGENT']);
$ua = explode(' ',$_SERVER['HTTP_USER_AGENT']);
//var_dump($ua);

$last = end($ua);
if(explode('/',$last)[0]=='Safari')
{
	reset($ua);
	array_pop($ua);
	$last = end($ua);
}

$bro = explode('/',$last);

if($bro[0] != 'SPbCTF')
{
	echo "<p>Your browser is:$bro[0], only SPbCTF is allowed</p>";
}
else
{
	$version = explode('.', $bro[1]);
	if((int)$version[0]<=31)
	{	
		if((int)$version[0]==31 and (int)$version[1]>472)
			echo "<p>Your browser is too modern! (current: $bro[1])</p>";
		elseif((int)$version[0]==31 and (int)$version[1]<472)
			echo "<p>Your browser version is old (current: $bro[1])</p>";
		elseif((int)$version[0]<31)
			echo "<p>Your browser version is old (current: $bro[1])</p>";
		else
			echo "<h1>Nice one! flag{binsearchispower}</h1>";
	}
	elseif((int)$version[0]>31)
	{
		echo "<p>Your browser is too modern! (current: $bro[1])</p>";
	}
	echo "<br>Note: browser version should contain only one dot (could be interpreted as float)";
}
