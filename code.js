for(i=0;i<10;i++) {
	document.write("<p>I will not sleep through my education. </p>")
}
for(i=0;i<10;i++) {
	document.write("<p>3 times " + (i)  + " = " + (3*i) +"</p>")
}
var n = 4;
document.write("<table>")
for(i=1;i<5;i++) {
  //start a row
  document.write("<tr>")
  //put items into columns
	document.write("<td>" + n + "</td>")
  document.write("<td>" + " x " + "</td>")
  document.write("<td>" + i + "</td>")
  document.write("<td>" + "=" + "</td>")
  document.write("<td>" + (i * n) + "</td>")
  document.write("</tr>")
}
document.write("</table>")	