var realAlert = alert;
alert = function(str)
{
	if(str == 'SPbCTF')
	{
		document.body.style.background = '#40ff40';
	}
	setTimeout(function(){realAlert(str)},0);
}
