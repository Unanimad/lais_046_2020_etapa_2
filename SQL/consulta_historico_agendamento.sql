SELECT
    she.date
    , she.status
    , lh.name health_center
FROM scheduling_historicalevent she
    JOIN logistic_healthcenter lh on she.created_at = lh.created_at
    WHERE 1 = 1
        -- AND she.id IN () -- PODE UTILIZAR PARA FILTRAR POR EVENTO ID(S)
        -- AND/OR patient.id IN () -- PODE SER UTILIZADO, QUANDO DISPONIVEL, PARA FILTRAR POR PACIENTE
        -- AND/OR hc.id IN () -- PODE UTILIZAR PARA FILTRAR POR ESTABELECIMENTO MÉDICO PASSANDO ID(S)