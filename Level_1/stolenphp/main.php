<?php 
	include_once('session.php');
	include_once('user.php');
	include_once('common.php');
	include_once('view.php');
	include_once('lightweb3.php');
	
	/* This function returns a configuation array that is then passed
	to the lightweb renderer */
	function render_main(){
		$props = array ();
		
		if (User::isUserLoggedIn())
		{
			props['user'] = User::getLoggedOnUser();
			props['allowComments'] = True;
			props['userPng'] = User::getUserPng(User::getLoggedOnUser());
		}
		else
		{
			props['allowComments'] = False;
		}
		
		$props['renderNews'] = True;
		$props['renderSports'] = True;
		$props['renderTech'] = True;
		$props['renderFashion'] = True;
		
		return $props;
	}
	
	$props = render_main();
	
	// render the page
	// this will draw all the HTML stuf...
	View::RenderPage (basename(__FILE__, ".php", $props);
?>