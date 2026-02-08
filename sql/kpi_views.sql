CREATE VIEW kpi_summary AS
SELECT
    AVG(yield_percent) AS avg_yield,
    AVG(downtime_minutes) AS avg_downtime,
    COUNT(*) AS total_records
FROM manufacturing_data;