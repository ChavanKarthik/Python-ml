CREATE TABLE `train1` (
  `id_code` varchar(45) NOT NULL,
  `current_date` date DEFAULT NULL,
  `current_time` varchar(45) DEFAULT NULL,
  `source_name` varchar(45) DEFAULT NULL,
  `destination_name` varchar(45) DEFAULT NULL,
  `train_name` varchar(45) DEFAULT NULL,
  `target` varchar(45) DEFAULT NULL,
  `country_code_source` varchar(45) DEFAULT NULL,
  `longitude_source` varchar(45) DEFAULT NULL,
  `latitude_source` varchar(45) DEFAULT NULL,
  `mean_halt_times_source` varchar(45) DEFAULT NULL,
  `country_code_destination` varchar(45) DEFAULT NULL,
  `longitude_destination` varchar(45) DEFAULT NULL,
  `latitude_destination` varchar(45) DEFAULT NULL,
  `mean_halt_times_destination` varchar(45) DEFAULT NULL,
  `current_year` int(11) DEFAULT NULL,
  `current_week` int(11) DEFAULT NULL,
  `current_day` varchar(45) DEFAULT NULL,
  `is_weekend` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

LOAD DATA INFILE '/var/lib/mysql-files/Train.csv' INTO TABLE train1
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;


