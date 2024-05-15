create database trabdev4;
use trabdev4;

create table comentario
(id int primary key auto_increment,
email varchar(100) not null,
assunto varchar(100),
escrito varchar(200));

