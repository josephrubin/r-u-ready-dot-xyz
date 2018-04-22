<?php 
	include_once('session.php');
	include_once('user.php');
	include_once('common.php');
	include_once('view.php');
	include_once('lightweb3.php');
	
	
	$props = array(
		'uname' => $_POST['user_name'];
		'password' => $_POST['password'];
		'name' => $_POST['first_name'];
		'lastName' => $_POST['last_name'];
		'png' => $_POST['profile_url'];
	);
	
	/* verify the input */
	$error = Common::VerifyInput ($props)
	
	// render the page
	// this will draw all the HTML stuf...
	View::RenderPage (basename(__FILE__, ".php"), $props, $error);
?>