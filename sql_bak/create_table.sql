create table test_O32_trade_2
(id int not null auto_increment,
trade_date date not null,
fund_id int not null,
fund_name varchar(20),
sec_id varchar(10),
sec_name varchar(15),
avg_price decimal(5,2),
market varchar(10),
trade_direct varchar(10),
trade_volume decimal(15,2),
trade_amount decimal(30,2),
per_trade_position decimal(4,2),
update_date datetime default now(),
primary key(id)
)engine=innodb