SELECT
    lh.name as health_center
    , se.date
    , vv.name as vaccine
    , se.created_at
    , se.status

FROM scheduling_event se
    JOIN logistic_healthcenter lh on lh.id = se.health_center_id
    JOIN scheduling_event_vaccine sev on se.id = sev.event_id
    JOIN vaccination_vaccine vv on sev.vaccine_id = vv.id
    JOIN logistic_vaccinestock lv on vv.id = lv.vaccine_id

    WHERE 1 = 1
        -- AND/OR hc.id IN () -- PODE UTILIZAR PARA FILTRAR POR ESTABELECIMENTO MÉDICO PASSANDO ID(S)
        -- AND/OR se.status IN () -- PODE SER UTILIZADO PARA FILTAR POR STATUS
        -- AND/OR lv.id IN () -- PODE UTILIZAR PARA FILTRAR POR LOTE PASSANDO ID(S)
        -- AND/OR vv.id IN () -- PODE UTILIZAR PARA FILTRAR POR VACINA PASSANDO ID(S)
        -- AND/OR patient.id IN () -- PODE SER UTILIZADO, QUANDO DISPONÍVEL, PARA FILTRAR POR PACIENTE PASSANDO ID(S)
        -- AND/OR professional.id IN () -- PODE SER UTILIZADO, QUANDO DISPONÍVEL, PARA FILTRAR POR PROFISSIONAL PASSANDO ID(S)
        -- AND/OR/BETWEEN se.date BETWEEN start_at AND end_at -- PODE SER UTILIZADO PARA FILTAR ENTRE DATAS