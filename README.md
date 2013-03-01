PyGmail
=======

Its a developer script which can be attached to any automated task which takes long time and requires only supervision to read its report.
For ex: kernel compiling

It accepts command line <br>

Usage:
`./sendmail -c file_containing_credentials -t to_emailid@xyz.com -s subject_line -b file_containing_body`

Try `./sendmail -h`  for more options

Check ./examples/report_kernel_compile

PS: Yes, maybe its not secure, but when you are AFK from your laptop; everything is **unsecured**
