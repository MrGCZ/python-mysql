CREATE OR REPLACE VIEW test_jsmx_view AS
    SELECT 
        c.l_fundid 账户编号, c.vc_name 产品名称,scdm 市场代码scdm,jllx 记录类型jllx,
        jyfs 交易方式jyfs,jsfs 交收方式jsfs,ywlx 业务类型ywlx,qsbz 清算标志qsbz,
        ghlx 过户类型ghlx,jsbh 交收编号jsbh,cjbh 成交编号cjbh,sqbh 申请编号sqbh,
        wtbh 委托编号wtbh,jyrq 交易日期jyrq,qsrq 清算日期qsrq,jsrq 交收日期jsrq,
        qtrq 其他日期qtrq,wtsj 委托时间wtsj,cjsj 成交时间cjsj,xwh1 业务单元一xwh1,
        xwh2 业务单元二xwh2,xwhy,jshy,tghy,zqzh 证券账号zqzh,zqdm1 证券代码一zqdm1,
        zqdm2 证券代码二zqdm2,zqlb 证券类别zqlb,ltlx 流通类型ltlx,qylb 权益类别qylb,
        gpnf 挂牌年份gpnf,mmbz 买卖标志mmbz,sl 交收数量sl,cjsl 成交数量cjsl,zjzh 资金账号zjzh,
        bz 币种bz,jg1 价格1jg1,jg2 价格2jg2
    FROM
        t_jsmx a,
        t_gdxw b,
        tfundinfo c
    WHERE
        a.zqzh = b.vc_code
            AND b.l_ztbh = c.l_fundid
            AND jyrq = date_format(now(),'%Y%m%d')

