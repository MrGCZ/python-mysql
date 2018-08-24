create table t_zqbd
(ID int not null auto_increment,
SCDM char(4),
QSBH char(10),
ZQZH char(12),
XWH char(8),
ZQDM char(8),
ZQLB char(4),
LTLX char(2),
QYLB char(4),
GPNF char(6),
BDSL char(20),
BDLX char(5),
BDRQ char(8),
SL char(20),
UPDATE_TIME datetime default now(),
primary key(ID)
)

