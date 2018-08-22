CREATE OR REPLACE VIEW test_jsmx_view AS
    SELECT 
        c.l_fundid, c.vc_name, a.*
    FROM
        t_jsmx a,
        t_gdxw b,
        tfundinfo c
    WHERE
        a.zqzh = b.vc_code
            AND b.l_ztbh = c.l_fundid
            AND jyrq = date_format(now(),'%Y%m%d')

