scp-wrapper.py is a dumb and simple Python script that could be set as user's login shell to permit scp only access. 
That could be useful if, for example, you want to save some data, e.g. logs or currently running configuration, 
from an appliance that can do scp but don't want to grant it full shell access.

Configuration
===============
As mentioned before, the script is dumb and simple so the path to its configuration files is hardcoded.
and points to /usr/local/etc/scponly.conf.
Just update it following the format listed below:

login=dir1:dir2:dir3, etc., 

where login is a user's login and dir1, dir2, dir3, etc. are just the full paths to the directories where the user is permitted to right into.

P.S.
This script was inspired by the following article http://www.snailbook.com/faq/restricted-scp.auto.html which also has a link to a scp-wrapper script written in Perl. 
