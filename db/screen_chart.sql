-- daily_unlock
CREATE TABLE IF NOT EXISTS daily_unlock (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `date` DATE NOT NULL,
    `device_id` VARCHAR(150) NOT NULL,
    `total_unlocks` INT DEFAULT 0,
    `0_2_unlocks` INT DEFAULT 0,
    `3_5_unlocks` INT DEFAULT 0,
    `6_8_unlocks` INT DEFAULT 0,
    `9_11_unlocks` INT DEFAULT 0,
    `12_14_unlocks` INT DEFAULT 0,
    `15_17_unlocks` INT DEFAULT 0,
    `18_20_unlocks` INT DEFAULT 0,
    `21_23_unlocks` INT DEFAULT 0,
    UNIQUE (`date`, `device_id`)
);

-- daily_durations
CREATE TABLE IF NOT EXISTS daily_durations (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `date` DATE NOT NULL,
    `device_id` VARCHAR(150) NOT NULL,
    `total_duration` DOUBLE DEFAULT 0,
    `0_2_duration` DOUBLE DEFAULT 0,
    `3_5_duration` DOUBLE DEFAULT 0,
    `6_8_duration` DOUBLE DEFAULT 0,
    `9_11_duration` DOUBLE DEFAULT 0,
    `12_14_duration` DOUBLE DEFAULT 0,
    `15_17_duration` DOUBLE DEFAULT 0,
    `18_20_duration` DOUBLE DEFAULT 0,
    `21_23_duration` DOUBLE DEFAULT 0,
    UNIQUE (`date`, `device_id`)
);

-- Inserting data into daily_unlock
INSERT INTO daily_unlock (`date`, `device_id`, `total_unlocks`, `0_2_unlocks`, `3_5_unlocks`, `6_8_unlocks`, `9_11_unlocks`, `12_14_unlocks`, `15_17_unlocks`, `18_20_unlocks`, `21_23_unlocks`)
SELECT 
    DATE(FROM_UNIXTIME(`timestamp`/1000)) as `date`,
    `device_id`, 
    COUNT(*) as `total_unlocks`,
    SUM(CASE WHEN HOUR(FROM_UNIXTIME(`timestamp`/1000)) BETWEEN 0 AND 2 THEN 1 ELSE 0 END) as `0_2_unlocks`,
    SUM(CASE WHEN HOUR(FROM_UNIXTIME(`timestamp`/1000)) BETWEEN 3 AND 5 THEN 1 ELSE 0 END) as `3_5_unlocks`,
    SUM(CASE WHEN HOUR(FROM_UNIXTIME(`timestamp`/1000)) BETWEEN 6 AND 8 THEN 1 ELSE 0 END) as `6_8_unlocks`,
    SUM(CASE WHEN HOUR(FROM_UNIXTIME(`timestamp`/1000)) BETWEEN 9 AND 11 THEN 1 ELSE 0 END) as `9_11_unlocks`,
    SUM(CASE WHEN HOUR(FROM_UNIXTIME(`timestamp`/1000)) BETWEEN 12 AND 14 THEN 1 ELSE 0 END) as `12_14_unlocks`,
    SUM(CASE WHEN HOUR(FROM_UNIXTIME(`timestamp`/1000)) BETWEEN 15 AND 17 THEN 1 ELSE 0 END) as `15_17_unlocks`,
    SUM(CASE WHEN HOUR(FROM_UNIXTIME(`timestamp`/1000)) BETWEEN 18 AND 20 THEN 1 ELSE 0 END) as `18_20_unlocks`,
    SUM(CASE WHEN HOUR(FROM_UNIXTIME(`timestamp`/1000)) BETWEEN 21 AND 23 THEN 1 ELSE 0 END) as `21_23_unlocks`
FROM 
    screen
WHERE 
    screen_status = 3
GROUP BY 
    DATE(FROM_UNIXTIME(`timestamp`/1000)), `device_id`;

INSERT INTO daily_durations (`date`, `device_id`, `total_duration`, `0_2_duration`, `3_5_duration`, `6_8_duration`, `9_11_duration`, `12_14_duration`, `15_17_duration`, `18_20_duration`, `21_23_duration`)
WITH PairedEvents AS (
    SELECT 
        s1.timestamp AS start_time,
        COALESCE(MIN(s2.timestamp), UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(s1.timestamp/1000)), INTERVAL 1 DAY))*1000) AS end_time,
        s1.device_id
    FROM 
        screen s1
    LEFT JOIN 
        screen s2 ON s1.device_id = s2.device_id AND s2.timestamp > s1.timestamp AND s2.screen_status = 0
    WHERE 
        s1.screen_status = 3
    GROUP BY 
        s1.timestamp, s1.device_id
)

SELECT 
    DATE(FROM_UNIXTIME(p.start_time/1000)) AS `date`,
    p.`device_id`,
    SUM(GREATEST(0, LEAST(p.end_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 1 DAY))*1000) - p.start_time)) / 1000 AS `total_duration`,
    SUM(GREATEST(0, LEAST(p.end_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 3 HOUR))*1000) - GREATEST(p.start_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 0 HOUR))*1000))) / 1000 AS `0_2_duration`,
    SUM(GREATEST(0, LEAST(p.end_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 6 HOUR))*1000) - GREATEST(p.start_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 3 HOUR))*1000))) / 1000 AS `3_5_duration`,
    SUM(GREATEST(0, LEAST(p.end_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 9 HOUR))*1000) - GREATEST(p.start_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 6 HOUR))*1000))) / 1000 AS `6_8_duration`,
    SUM(GREATEST(0, LEAST(p.end_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 12 HOUR))*1000) - GREATEST(p.start_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 9 HOUR))*1000))) / 1000 AS `9_11_duration`,
    SUM(GREATEST(0, LEAST(p.end_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 15 HOUR))*1000) - GREATEST(p.start_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 12 HOUR))*1000))) / 1000 AS `12_14_duration`,
    SUM(GREATEST(0, LEAST(p.end_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 18 HOUR))*1000) - GREATEST(p.start_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 15 HOUR))*1000))) / 1000 AS `15_17_duration`,
    SUM(GREATEST(0, LEAST(p.end_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 21 HOUR))*1000) - GREATEST(p.start_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 18 HOUR))*1000))) / 1000 AS `18_20_duration`,
    SUM(GREATEST(0, LEAST(p.end_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 24 HOUR))*1000) - GREATEST(p.start_time, UNIX_TIMESTAMP(DATE_ADD(DATE(FROM_UNIXTIME(p.start_time/1000)), INTERVAL 21 HOUR))*1000))) / 1000 AS `21_23_duration`
FROM 
    PairedEvents p
GROUP BY 
    DATE(FROM_UNIXTIME(p.start_time/1000)), p.`device_id`;

-- Create weekly_unlocks table
DROP TABLE IF EXISTS weekly_unlocks;

CREATE TABLE weekly_unlocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    week_start DATE,
    device_id VARCHAR(150),
    Monday INT,
    Tuesday INT,
    Wednesday INT,
    Thursday INT,
    Friday INT,
    Saturday INT,
    Sunday INT,
    UNIQUE (week_start, device_id)
);

INSERT INTO weekly_unlocks (week_start, device_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
SELECT 
    sub.week_start,
    sub.device_id,
    MAX(CASE WHEN DAYOFWEEK(du.date) = 2 THEN du.total_unlocks ELSE NULL END) as Monday,
    MAX(CASE WHEN DAYOFWEEK(du.date) = 3 THEN du.total_unlocks ELSE NULL END) as Tuesday,
    MAX(CASE WHEN DAYOFWEEK(du.date) = 4 THEN du.total_unlocks ELSE NULL END) as Wednesday,
    MAX(CASE WHEN DAYOFWEEK(du.date) = 5 THEN du.total_unlocks ELSE NULL END) as Thursday,
    MAX(CASE WHEN DAYOFWEEK(du.date) = 6 THEN du.total_unlocks ELSE NULL END) as Friday,
    MAX(CASE WHEN DAYOFWEEK(du.date) = 7 THEN du.total_unlocks ELSE NULL END) as Saturday,
    MAX(CASE WHEN DAYOFWEEK(du.date) = 1 THEN du.total_unlocks ELSE NULL END) as Sunday
FROM 
    (SELECT DISTINCT device_id, DATE_SUB(date, INTERVAL (DAYOFWEEK(date) - 1) DAY) as week_start FROM daily_unlock) as sub
LEFT JOIN 
    daily_unlock du ON sub.device_id = du.device_id AND YEARWEEK(du.date) = YEARWEEK(sub.week_start)
GROUP BY 
    sub.week_start, sub.device_id;

-- Create weekly_durations table
DROP TABLE IF EXISTS weekly_durations;

CREATE TABLE weekly_durations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    week_start DATE,
    device_id VARCHAR(150),
    Monday DOUBLE,
    Tuesday DOUBLE,
    Wednesday DOUBLE,
    Thursday DOUBLE,
    Friday DOUBLE,
    Saturday DOUBLE,
    Sunday DOUBLE,
    UNIQUE (week_start, device_id)
);

INSERT INTO weekly_durations (week_start, device_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
SELECT 
    sub.week_start,
    sub.device_id,
    MAX(CASE WHEN DAYOFWEEK(dd.date) = 2 THEN dd.total_duration ELSE NULL END) as Monday,
    MAX(CASE WHEN DAYOFWEEK(dd.date) = 3 THEN dd.total_duration ELSE NULL END) as Tuesday,
    MAX(CASE WHEN DAYOFWEEK(dd.date) = 4 THEN dd.total_duration ELSE NULL END) as Wednesday,
    MAX(CASE WHEN DAYOFWEEK(dd.date) = 5 THEN dd.total_duration ELSE NULL END) as Thursday,
    MAX(CASE WHEN DAYOFWEEK(dd.date) = 6 THEN dd.total_duration ELSE NULL END) as Friday,
    MAX(CASE WHEN DAYOFWEEK(dd.date) = 7 THEN dd.total_duration ELSE NULL END) as Saturday,
    MAX(CASE WHEN DAYOFWEEK(dd.date) = 1 THEN dd.total_duration ELSE NULL END) as Sunday
FROM 
    (SELECT DISTINCT device_id, DATE_SUB(date, INTERVAL (DAYOFWEEK(date) - 1) DAY) as week_start FROM daily_durations) as sub
LEFT JOIN 
    daily_durations dd ON sub.device_id = dd.device_id AND YEARWEEK(dd.date) = YEARWEEK(sub.week_start)
GROUP BY 
    sub.week_start, sub.device_id;
