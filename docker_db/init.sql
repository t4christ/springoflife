create database springs;
create user springs_user with encrypted password 'springs_password';
grant all privileges on database  springs to springs_user;