# webhook-test
Testing that the webhook from github triggers a jenkins pipeline automatically on a personal computer
 
pre requisites:
-Jenkins must be public (no running in localhost)
  so, create a public URL with localtunnel (got 502 bad gateway)
  or Pinggy (works fine so far)

In github: 
1)  Webhook must point to the Jenkins public ip address and add /github-webhook/ at the end: 
  https://JenkinsPublicURL/github-webhook/ 
  example: https://mysubdomain.a.pinggy.link/github-webhook/

In Jenkins configuration:
1) Check <GitHub hook trigger for GITScm polling>
2) Pipeline <Pipeline script from SCM>
2.1) Repository URL: https://github.com/SCuellar80/webhook-jenkins.git
2.2) The Branch Specifier: */main
2.3) Script Path: jenkins/jenkinsfile
3) Run the first job manually (only once needed)

Now every commit will automatically trigger the pipeline described in jenkinsfile
