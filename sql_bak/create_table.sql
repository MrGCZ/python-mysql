create table test_O32_trade
(id int not null auto_increment,
trade_date date not null,
fund_id char(6) not null,
fund_name varchar(20),
sec_id varchar(10),
sec_name varchar(15),
trade_direct varchar(10),
trade_volume decimal(15,2),
trade_amount decimal(20,2),
insert_date datetime default now(),
primary key(id)
)engine=innodb