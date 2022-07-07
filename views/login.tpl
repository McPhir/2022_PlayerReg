<!DOCTYPE html>
<html>
<head>
<title>Player Registration</title>
<link rel="stylesheet" href="static/styles.css">
</head>

<body>
<div id = "main" class="main">
    % include('header.html')
<div class="hero">
    <div class="herotext">
      <p> Macleans Football Player Registration</p>
    </div>
  </div>
  <form action="/login" method="post">
    <div class="form-container">
      <div>Username: <input name="username" type="text" /></div>
      <div>Password: <input name="password" type="password" /></div>
      <div><input value="Login" type="submit" /></div>
    </div>
  </form>

  <div>{{loggedon[0]}},{{loggedon[1]}},{{loggedon[2]}}</div>
  % include('slideshowinclude.html')
</div>
</div>
% include('footer.html')
</body>
</html>