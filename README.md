# webhook-test
How to run a Jenkins pipeline in a local computer?

Any change in this Github repository will trigger a Jenkins pipeline automatically. Jenkins is running in a local computer.

Since Jenkins URL must be public (no running in localhost), we need to create a public URL of your localhost:8080 with localtunnel (got 502 bad gateway) or Pinggy (works fine so far)

Settings in github: 
1)  Webhook must point to the Jenkins public ip address and add /github-webhook/ at the end: 
  https://JenkinsPublicURL/github-webhook/ 
  example: https://mysubdomain.a.pinggy.link/github-webhook/

Configuration in Jenkins:
1) Check "GitHub hook trigger for GITScm polling"
2) Pipeline select "Pipeline script from SCM"
2.1) Repository URL: https://github.com/SCuellar80/webhook-jenkins.git
2.2) The Branch Specifier: */main
2.3) Script Path: jenkins/jenkinsfile
3) Run the first job manually (only once needed)

Now every commit will automatically trigger the pipeline described in jenkinsfile:
https://github.com/SCuellar80/webhook-jenkins/blob/main/jenkins/jenkinsfile
