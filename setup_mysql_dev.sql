-- create a MySQL server
-- DATABASSE : hbnb_dev_db
-- PASSWORD : hbnb_dev_pwd
-- SELECT privilege on the performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER
    IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES
    ON 'hbnb_dev'.*
    TO 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';

GRANT SELECT
    ON 'performance_schema'.*
    TO 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';

FLUSH PRIVILEGES;
