create table t_sjsfx
(ID int not null auto_increment,
FXJSZH char(8),
FXTGDY char(8),
FXZQDM char(10),
FXZQZH char(25),
FXYWLB char(6),
FXDDBH char(12),
FXWTGS decimal(18,2),
FXQRGS decimal(18,2),
FXZJJE decimal(20,2),
FXCWDH char(6),
FXFSRQ char(10),
FXBYBZ char(2),
UPDATE_TIME datetime default now(),
primary key(ID)
)
