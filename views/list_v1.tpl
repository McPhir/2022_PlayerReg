<!DOCTYPE html>
<html>
<head>
<title>List of python things</title>
 <link rel="stylesheet" href="/static/styles.css"/>
</head>

<body>
<!-- good practice to put a main div within the body - prevents too wide a page -->
<div class=main>
<h1>Macleans College Player Registration</h1>
<p>Use this to update player details</p>
<p>Today is {{day}}</p>

<table>
<tr><th>First Name</th><th>Last Name</th><th>Date of Birth</th></tr>
%for p in players:
  <tr><td>{{p.firstname}}</td><td>{{p.lastname}}</td><td>{{p.DOB}}</td></tr>
%end
</table>
</div>
</body>
</html>