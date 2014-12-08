function r()
{

	var username=document.getElementById("username");

	var pass=document.getElementById("password");
	if(username.value=="")
	{
		alert("please enter username");
		username.focus();
		return false;
	}
	if(pass.value=="")
	{
		alert("please enter password");
		return false;
	}
return true;
}