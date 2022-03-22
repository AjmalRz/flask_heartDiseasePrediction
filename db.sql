/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - heart_didease
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`heart_didease` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `heart_didease`;

/*Table structure for table `docter` */

DROP TABLE IF EXISTS `docter`;

CREATE TABLE `docter` (
  `docter_id` int(11) NOT NULL AUTO_INCREMENT,
  `iog_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `specialistion` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`docter_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `docter` */

insert  into `docter`(`docter_id`,`iog_id`,`name`,`qualification`,`gender`,`specialistion`,`email`,`phone`) values 
(1,2,'Vishnu sudhin','MBBS,MD','Male','Cardiology','vishnusudhin4@gmail.com',8129523332);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'vishnu','vishnu','docter'),
(4,'shan','shan','user'),
(5,'aishu','aishu','user');

/*Table structure for table `question` */

DROP TABLE IF EXISTS `question`;

CREATE TABLE `question` (
  `q_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) DEFAULT NULL,
  `question` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`q_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `question` */

insert  into `question`(`q_id`,`u_id`,`question`,`reply`,`date`) values 
(1,12,'Why i feel pain on my left\r\nside of my chest','pending','2021-04-11'),
(2,12,'why i feel heart pain while am sleeping','pending','2021-04-11'),
(3,5,'why i feel bad in night','sleep in time every day..make dially routin','2021-04-11');

/*Table structure for table `treatment` */

DROP TABLE IF EXISTS `treatment`;

CREATE TABLE `treatment` (
  `treatment_id` int(11) NOT NULL AUTO_INCREMENT,
  `doc_id` int(11) DEFAULT NULL,
  `treatment_name` varchar(50) DEFAULT NULL,
  `deatails` varchar(50) DEFAULT NULL,
  `fee` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`treatment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `treatment` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `mobile` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`log_id`,`name`,`age`,`gender`,`mobile`,`email`) values 
(1,4,'Muhammed shan','22','Male',9078654321,'shan@123.com'),
(2,5,'aishwarya','19','Female',9078654321,'aishu@hm.com');

/*Table structure for table `view_feedback` */

DROP TABLE IF EXISTS `view_feedback`;

CREATE TABLE `view_feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `feedback` text,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `view_feedback` */

insert  into `view_feedback`(`feedback_id`,`user_id`,`feedback`,`date`) values 
(1,12,'very good','2021-04-11'),
(2,5,'good','2021-04-11'),
(3,4,'bad','2021-04-11');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
