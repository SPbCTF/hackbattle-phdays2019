<!DOCTYPE html>
<head>
<script src="check.js"></script>
</head>
<body>
<h1>Simple XSS challenge</h1>
<p>Pop an alert with 'SPbCTF' in you browser using XSS payload to win! (using browser's console is not allowed)</p>
<p>$_GET['spbctf']=<?=$_GET['spbctf'];?>;</p>
</body>
