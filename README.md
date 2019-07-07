# ip-address-tracker
Simple way of tracking your ISPs dynamic ip address

I must first admit that I got a bit on this from Googles in the past but I cannot to the life of me remember where. If your searches on this topic have lead you to this and the code looks familiar please send me the link so that I can give the proper credits and props.

Anyway, so as the name on the tin states when run these scripts will check your ip address and compare it to your current ip address which should be stored in "public.txt". If they do not match, you will be sent an email which the credentials in... you guessed it... credentials.py. After doing so the ip in public.txt shall be overwritten by the new one.

I have this running on a pi which runs this script as a cronjob every 15 minutes and use a dedicated gmail address. I leave how and when the script is run up to you.
