create database bank
use bank

create table account_detail(
account_no int auto_increment primary key,
name varchar(100),
balance float);

select*from account_detail
drop table account_detail