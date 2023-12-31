# TheBasicFoodDiary
The Basic Food Diary 

**Design**

The Basic Food Diary is an HTML form that is connected to a Linux server. Within the coding of the form, is the utilization of Python3, CGI, JavaScript, and CSS. There are at least two possible users; the client and the provider. The client is the one filling out the form from which they access using any screen device with an internet connection, and the provider who has access to the server, can view each diary submission. Users can currently access the Food Diary through a URL (students.hi.gmu.edu/~amoktade/project.html). The input is stored in the server from where it can be read and manipulated to accommodate for changes. 

Given the simplistic nature of the form, I attempted to focus on various design elements using CSS to make the form a little more enjoyable, appealing, and accessible. I started off with incorporating a background image, margins, different font style for the heading, and a slight variety in input types (radio, text, textarea). To add more visual elements and add to user experience, I used emojis to help keep the form light-hearted and in hopes to capture a younger audience. Keeping in mind that individuals use their phone often, I made sure to insert an html meta tag, specifying viewport, which enables the form to be mobile friendly. The insertion of a ‘read-more-read-less’ button gave way to providing extra information that could prove helpful for the user. Each of those buttons yielded tips, reflection, and a reputable source to learn more information. Small recommendations such as these can be impactful to a user as it leads them towards information they may not have previously thought to seek. This specific button primarily used Javascript; calling a function, using src attribute, and getElementByID. Similarly, I styled all buttons to slightly pop out with rounded edges. It was a small change, but it made a difference in the way the page looked overall. 

**Implementation**

In implementing this program, I primarily worked in Python3 within Linux. This is where on our hap618 server. The form is connected by three different files on the server; an html file with the primary source code that displays the main webpage, a cgi file to execute the output of the html file which displays once the form is submitted, and a text file that stores the output executed from the cgi file. One of the key components of the source code is that which links all these files together (see Figure 1). It was important for the cgi file to be displayed to the user as it provided a screen that could capture their input for the day for their own records. In addition to having a text box to add their contact information, of the different buttons used, having the submit button was crucial to trigger the chain reaction of storing the user’s information on our home server. 
 
 
 
Figure 1: (above) Lines taken from the project.html and project.cgi file which links the three files together. 
Figure 2. (right) Source code for Tips and Recommendations button. Taken from the project.html file.

**Testing **
The code which proved to be the most troublesome was the, “Tips and Recommendations.” (Figure 2). Despite referencing the code from W3Schools, the creation and placement of the tags went through hours of trial and error to finally execute correctly. Below are screenshots taken from a test run (Figure 3).
     
Figure 3. Starting in order from the top, going left to right. Form is filled, and once “Submit” button is clicked, an alert appears. Upon pressing ‘OK’, the next page with all user’s input appears. The PuTTY file displays the input as stored in the projectdata.txt file. 

**Conclusions & Future Work** 

Overall, this project is in its most preliminary stage. It serves to provide the basic function of logging daily food intake and lifestyle habits. In the scenario proposed, both the user and provider have access to the information in which they can work collaboratively to focus on areas of improvement. It does not serve the purpose to provide solutions but is a stepping-stone to move in the right direction to self-awareness regarding food and lifestyle behaviors. 
Improving the form will be a challenge that involves making it more dynamic and interesting for a user to fill out daily. It could mean incorporating a more interactive, colorful, and user-friendly design that entices the user to fill out the Food Diary on a near daily basis. These components are generally catered to the target audience. The form now may not appeal to a younger audience as much as it may suffice for an older audience. Generally, the basic html design style is outdated. Therefore, focusing on improving it is important, especially when there is competition in the market. Some things I would like to improve on specifically is another way for users to keep track of their data, so they do not need to rely on someone who has access to the server to provide it. Instead, the user has access to a catalog of their past intakes or input history. Any type of analysis could be useful for a user that does not want to analyze and calculate their history themselves. A quick analysis against general dietary guidelines can provide a visual for successes and the need for future improvements. These are a few of the potential extensions that I plan to test out and implement for this Food Diary. 

Throughout this project, I have learned quite a bit about the basics of creating a website and the various components, languages, and programming that is utilized to just make the skeleton of one.
