kill("file:///var/www/static/drk_logo1.png")
on /register
if we define
function kill()
{
	$.getJSON ('testProfilePng', { u: btoa(url) }, showProfilePng)		
}

After much trial and error, we figure out that files are stored under /var/www
We can use the file:// protocol to have the server fetch them for us.

Now we can essentially fetch any file on the server that ends in .png
It is weird though, after doing the request, we have one cahh\nce to retrieve the file from /profilePics.
After one request, it dissapears.
Somehow we need to get from here to getting the code of login.php or something else.

Well, if we append ?.png after the URL we can trick the server into serving us login.php and other files!
Or, rather, login.php?.png hahaha.

Upon doing so, we get php code back, encoded in base64!