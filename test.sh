
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