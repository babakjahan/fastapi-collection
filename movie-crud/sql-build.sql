CREATE DATABASE `movie_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `movie_db`.`tbl_movies` (
  `id_movies` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(256) NULL,
  `year` INT NULL,
  `storyline` TEXT(2000) NULL,
  PRIMARY KEY (`id_movies`));
