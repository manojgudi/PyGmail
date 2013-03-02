PyGmail
=======

Its a developer script which can be attached to any automated task which takes long time and requires only supervision to read its report.
For ex: kernel compiling

It accepts command line arguments<br>

Usage:
`./sendmail -c file_containing_credentials -t to_emailid@xyz.com -s subject_line -b file_containing_body` <br>
For sending to multiple-email addresses, use double-quotes and a comma:<br>
`-t "person1@xyz.org,person2@pqr.com"`


Try `./sendmail -h`  for more options; Check *./examples/report_kernel_compile* on how to use it in bash-script

PS: Yes, maybe its not secure, but when you are AFK from your laptop; everything is **unsecured**
