# AutoReplier 

This program will reply automatically to emails from specific senders that you can specify. Feel free to tweak it and make it fit your needs. You can remove the need to specify the senderes by removeing the "compare_array". When removed the program will check for unseen emails and reply to them. 

***before using it make sure you fill the compare array*** 

# Sources I used 

- https://docs.python.org/3/library/imaplib.html 
- https://docs.python.org/3/library/string.html 
- https://docs.python.org/3/library/smtplib.html 
- https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/
- https://stackoverflow.com/questions/13210737/get-only-new-emails-imaplib-and-python 

# How it works 

- You are first prompted to enter your email and password (password will be hidden).
- After syncing your inbox the emails that the program will reply to are printed on the console if any.
- They are written in a "sender.txt" file than read in the next function that will send a message written in "message.txt" file 
 
# Why I needed it 

As an online tutor I always receive submissions from trainees, and I always thank them for their submission as soon as I can. So I decided to automate the procedure.
