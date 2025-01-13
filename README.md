# webhook-test
testing the webhook

pre requisites:
-Jenkins must be public (no running in localhost)
  or running with localtunnel and disabled s 

In your Jenkins:
-Put the repository link: 
  example:  https://github.com/SCuellar80/webhook-test.git
The branch is not master but main. Change it.

In github:
-Webhook must point to the Jenkins public ip address and must contains /github-webhook/ after the ip address: 
  example: https://honest-aliens-shop.loca.lt/github-webhook/
