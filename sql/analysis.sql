
-- 1. Compare planned and actual production
SELECT
    date,
    shift,
    planned_tonnes,
    actual_tonnes,
    ROUND(
        100.0 * actual_tonnes / NULLIF(planned_tonnes, 0),
        2
    ) AS production_achievement_pct
FROM production_data;

-- 2. Find shifts with the highest downtime
SELECT
    date,
    shift,
    downtime_hours,
    scheduled_hours
FROM production_data
ORDER BY downtime_hours DESC;

-- 3. Summarise production by shift
SELECT
    shift,
    SUM(planned_tonnes) AS total_planned,
    SUM(actual_tonnes) AS total_actual
FROM production_data
GROUP BY shift
ORDER BY shift;

