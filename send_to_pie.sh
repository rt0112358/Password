# Generates random password.
# Adds random password to new.sql.
# Sends and loads new.sql on
#  raspi pi mysql server.

python print_pword.py > new.sql
scp new.sql pi@billbobpie.ddns.net:~/
ssh pi@billbobpie.ddns.net './load_new.sh'