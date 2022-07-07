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
  %for p in players:
  <tr>
    <td>
      <a href="/edit?id={{p.studentid}}">{{p.firstname}}</a></td>
    <td>
      <a href="/edit?id={{p.studentid}}">{{p.lastname}}</a></td>
    <td>{{p.DOB}}</td>
    <td><a href="/delete?id={{p.studentid}}">delete player from database</a></td>
  </tr>
  %end
</table>
</div>
</body>
</html>
