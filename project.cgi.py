# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:25:51 2021

@author: arsha
"""

#!/usr/bin/env python3

print("/nContent-type: text/html\n\n" )

import cgi 

form = cgi.FieldStorage()


date = form.getvalue('date', '')
mood = form.getvalue('mood', '')
sleep = form.getvalue('sleep', '')
breakfast = form.getvalue('breakfast', '')
lunch = form.getvalue('lunch', '')
dinner = form.getvalue('dinner', '')
snacks = form.getvalue('snacks', '')
gwater = form.getvalue('gwater', '')
otherbeverage = form.getvalue('otherbeverage', '')
comments = form.getvalue('comments', '')
fn = form.getvalue('fname', '' )
ln = form.getvalue('lname', '' )
emaila = form.getvalue('emaila', '' )



print("<html>")

# save data to file 
print("Storing data to file...")
f = open("/home/amoktade/projectdata.txt", 'a') 
f.write('\n')
f.write('<submission>')
f.write('\n')
f.write('<date>')
f.write(date)
f.write('</date>')
f.write('\n')
f.write('<mood>')
f.write(mood)
f.write('</mood>')
f.write('\n')
f.write('<sleep>')
f.write(sleep)
f.write('</sleep>')
f.write('\n')
f.write('<breakfast>')
f.write(breakfast)
f.write('</breakfast>')
f.write('\n')
f.write('<lunch>')
f.write(lunch)
f.write('</lunch>')
f.write('\n')
f.write('<dinner>')
f.write(dinner)
f.write('</dinner>')
f.write('\n')
f.write('<snacks>')
f.write(snacks)
f.write('</snacks>')
f.write('\n')
f.write('<gwater>')
f.write(gwater)
f.write('</gwater>')
f.write('\n')
f.write('<otherbeverage>')
f.write(otherbeverage)
f.write('</otherbeverage>')
f.write('\n')
f.write('<comments>')
f.write(comments)
f.write('</comments>')
f.write('\n')
f.write('<firstname>') 
f.write(fn)
f.write('</firstname>')
f.write("\n")
f.write('<lastname>')
f.write(ln)
f.write('/lastname>')
f.write('\n')
f.write('<email>')
f.write(emaila)
f.write('</email>')
f.write("\n")
f.write("\n")
f.write('</submission>')
f.write("\n")
f.close()
print("done!<br>")

print("Input History<br>")
print("<br>")
print("Date: ", date, "<br>")
print("Mood: ", mood, "<br>")
print("Sleep: ", sleep, "<br>")
print("Breakfast: ", breakfast, "<br>")
print("Lunch: ", lunch, "<br>")
print("Dinner: ", dinner, "<br>")
print("Snacks: ", snacks, "<br>")
print("Glasses of Water: ", gwater, "<br>")
print("Other Beverages: ", otherbeverage, "<br>")
print("Additional Comments: ", comments, "<br>")
print("First Name: ", fn, "<br>")
print("Last Name: ", ln, "<br>")
print("Email: ",emaila, "<br>")
print("<br>")
print("Please screenshot for your own records!")


print("</html>")

