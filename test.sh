
# echo "File Name: $0"
# echo "First Parameter : $1"
# echo "Second Parameter : $2"
# echo "Third Parameter : $3"
# echo "Quoted Values: $@"
# echo "Quoted Values: $*"
# echo "Total Number of Parameters : $#"


# for TOKEN in $*
# do
#    echo $TOKEN
# done

# echo 'Echoing' $? #exit status



# $ ssh-keygen -t rsa -b 4096 -C 'build@travis-ci.org' -f ./deploy_rsa
# $ travis encrypt-file deploy_rsa --add
# $ ssh-copy-id -i deploy_rsa.pub ec2-user@<your-ec2-instance>
# $ rm -f deploy_rsa deploy_rsa.pub
# $ git add deploy_rsa.enc


 # Run ssh configuration
  # - openssl aes-256-cbc -K $encrypted_0a6446eb3ae3_key -iv $encrypted_0a6446eb3ae3_iv -in deploy_rsa.enc -out /tmp/deploy_rsa -d
  # - eval "$(ssh-agent -s)"
  # - chmod 600 /tmp/deploy_rsa
  # - echo "yes" ssh-add /tmp/deploy_rsa

#  sudo docker run -it --rm certbot/certbot certonly --manual -d missions.springsoflifeg.com 


# sudo docker run -it --rm certbot/certbot certonly --manual --preferred-challenges=dns --email bakaretemitayo712@gmail.com --server https://acme-v02.api.letsencrypt.org/directory --agree-tos --manual-public-ip-logging-ok -d missions.springsoflifeg.com


# Database High Availability Strategies

# Redundancy
# System Monitoring
# Fail Over
# Load balancing
# Maximizing Performance
# Minimizing Impact of maintainance


# Database Clustering is the process of combining more than one servers or instances connecting to a single database.
# Advantages

# Fault Tolerant
# Load balancing

# Two Database Clustering Form
# Shared Nothing Architecture
# Shared Disk Architecture


#  openssl req -subj '/CN=localhost' -x509 -newkey rsa:4096 -nodes -keyout key.pem -out cert.pem -days 365
