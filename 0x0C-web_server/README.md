# 0x0C. Web server

## introduction

### In this project, some of the tasks will be graded on 2 aspects:

- Is your web-01 server configured according to requirements
- Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements
(meaning without any human intervention)
For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

```bash
workspace@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
workspace@ubuntu
```

### For this project, i am expected to look at these concepts :

- DNS
- Web Server
- CI/CD
- Docker
- Web stack debugging
- DevOps
- System Administration
- Site Reliability Engineering
- questioning the last life decisions i took
