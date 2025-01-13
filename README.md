# webhook-test
testing the webhook and jenkinsfile
 
pre requisites:
-Jenkins must be public (no running in localhost)
  could be running public URL with localtunnel (got 502 bad gateway)
  could be running public URL with Pinggy (currently using a trial)

In your Jenkins:
1) Put the repository link: 
example:  https://github.com/SCuellar80/webhook-test.git
2) The branch is not master but main. Change it.

In github:
1)  Webhook must point to the Jenkins public ip address and must contains /github-webhook/ after the ip address: 
  https://JenkinsPublicURL/github-webhook/
  example: https://honest-aliens-shop.loca.lt/github-webhook/
