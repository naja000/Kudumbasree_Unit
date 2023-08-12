/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - kudmbasree
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`kudmbasree` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `kudmbasree`;

/*Table structure for table `advertisement` */

DROP TABLE IF EXISTS `advertisement`;

CREATE TABLE `advertisement` (
  `aid` int(50) NOT NULL AUTO_INCREMENT,
  `kudumbasree_id` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `advertisement` */

insert  into `advertisement`(`aid`,`kudumbasree_id`,`date`,`description`,`image`) values 
(1,'4','2021-12-01','danis','/static/advertisement/Screenshot (1).png'),
(2,'4','2021-12-02','danis','/static/advertisement/Screenshot (1).png'),
(3,'4','2021-12-01','mustafa','/static/advertisement/Screenshot (1).png');

/*Table structure for table `booking_main` */

DROP TABLE IF EXISTS `booking_main`;

CREATE TABLE `booking_main` (
  `book_id` int(50) NOT NULL AUTO_INCREMENT,
  `user_id` int(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `amount` bigint(50) DEFAULT NULL,
  `kud_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `booking_main` */

insert  into `booking_main`(`book_id`,`user_id`,`date`,`status`,`amount`,`kud_lid`) values 
(1,3,'2021-12-10','pending',56,7),
(2,2,'2021-12-14','pending',60,8);

/*Table structure for table `booking_sub` */

DROP TABLE IF EXISTS `booking_sub`;

CREATE TABLE `booking_sub` (
  `bsid` int(50) NOT NULL AUTO_INCREMENT,
  `book_id` int(50) DEFAULT NULL,
  `product_id` int(50) DEFAULT NULL,
  `qty` int(50) DEFAULT NULL,
  PRIMARY KEY (`bsid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `booking_sub` */

insert  into `booking_sub`(`bsid`,`book_id`,`product_id`,`qty`) values 
(1,1,1,45),
(2,2,7,778);

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cid` int(50) NOT NULL AUTO_INCREMENT,
  `u_id` varchar(50) DEFAULT NULL,
  `total_amount` bigint(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `cart` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(50) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `fromlid` varchar(50) DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`date`,`fromlid`,`feedback`) values 
(1,'2021-12-23','2','hnjm,dgrh');

/*Table structure for table `festival` */

DROP TABLE IF EXISTS `festival`;

CREATE TABLE `festival` (
  `fest_id` int(50) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  `name` varchar(70) DEFAULT NULL,
  PRIMARY KEY (`fest_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `festival` */

insert  into `festival`(`fest_id`,`date`,`time`,`description`,`image`,`name`) values 
(6,'2022-01-01','10:49:00','danish daniman','/static/festval/Screenshot (1).png','daniman'),
(9,'2021-12-04','16:14:00','danish','/static/festval/Screenshot (2).png','daniman');

/*Table structure for table `kudmbasree` */

DROP TABLE IF EXISTS `kudmbasree`;

CREATE TABLE `kudmbasree` (
  `kudumbasree_id` int(50) NOT NULL AUTO_INCREMENT,
  `login_id` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `member_count` int(50) DEFAULT NULL,
  `leader_name` varchar(50) DEFAULT NULL,
  `leader_phoneno` bigint(50) DEFAULT NULL,
  `leader_photo` varchar(500) DEFAULT NULL,
  `staus` varchar(50) DEFAULT NULL,
  `email_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`kudumbasree_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `kudmbasree` */

insert  into `kudmbasree`(`kudumbasree_id`,`login_id`,`name`,`place`,`area`,`post`,`pin`,`district`,`member_count`,`leader_name`,`leader_phoneno`,`leader_photo`,`staus`,`email_id`) values 
(3,'2','kkkk','kkk','llll','mmm',0,'cccc',233,'jjj',1234,'/static/festval/Screenshot (2).png','approved','dd@gmail.com'),
(5,'1','ddd','qqqq','bb','llll',34,'wayanad',23,'lkikk',4567,'ssss','approved','rr@gmail.com'),
(6,'4','rrr','uuu','gv','bnb',0,'bbnb',55,'vvh',0,'/static/festval/Screenshot (2).png','approved','ff@gmail.com'),
(7,'7','danish','danish','danish','danish',5682,'danish',56,'danish',543354354,'ml','approved','danish@gmail.com'),
(8,'8','daniman','daniman','daniman','daniman',2376,'daniman',26,'danish',123456,'wssxxws','pending','daniman@gmail.com'),
(9,'4','mustafa','mellatur','sdsad','dhsg',727,'palakkad',90,'danish',25874654,'/static/kudumbasree/Screenshot (3).png','approved','mustafa@gmail.com');

/*Table structure for table `kudumbasree_complaint` */

DROP TABLE IF EXISTS `kudumbasree_complaint`;

CREATE TABLE `kudumbasree_complaint` (
  `kc_id` int(50) NOT NULL AUTO_INCREMENT,
  `from_id` varchar(50) DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `ksree_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`kc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `kudumbasree_complaint` */

insert  into `kudumbasree_complaint`(`kc_id`,`from_id`,`complaint`,`reply`,`date`,`status`,`ksree_lid`) values 
(3,'3','yyyy','dyhtryrtyrtyr','2021-12-14','replied',3),
(4,'2','xxxxxxxxxx','danish','2021-12-22','replied',5);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(50) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'doc@gmail.com','11','kudumbasree'),
(3,'kudumbasree@gmail.com','danish','kudumbasree'),
(4,'mustafa@gmail.com','1','kudumbasree');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `nid` int(50) NOT NULL AUTO_INCREMENT,
  `notification` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`nid`,`notification`,`date`) values 
(7,'danish2','2022-01-01'),
(8,'danish daniman','2021-12-26'),
(12,'daniman 3','2021-12-26'),
(13,'qwery','2021-12-26'),
(16,'danish','2021-12-26');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(50) NOT NULL AUTO_INCREMENT,
  `quantity` int(50) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  `kudumbasree_id` int(50) DEFAULT NULL,
  `product_name` varchar(50) DEFAULT NULL,
  `amount` bigint(50) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`quantity`,`details`,`kudumbasree_id`,`product_name`,`amount`,`image`) values 
(1,44,'abcdefghij',2,'danish',77,'/static/product/Screenshot (5).png'),
(2,1221,'likuyhgt',1,'daniman',99,'/static/product/Screenshot (5).png'),
(6,10,'sdfajfadghgfd',4,'soap',28,'/static/product/Screenshot (5).png'),
(7,100,'sdfajfadghgfd',4,'rice',60,'/static/product/Screenshot (4).png');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `ratingid` int(50) NOT NULL AUTO_INCREMENT,
  `pid` varchar(50) DEFAULT NULL,
  `u_id` varchar(50) DEFAULT NULL,
  `rating` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`ratingid`),
  KEY `ratingid` (`ratingid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`ratingid`,`pid`,`u_id`,`rating`,`date`) values 
(1,'2','3','5','2021-10-15'),
(2,'6','2','4','2021-12-21');

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `kudumbasree_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `file` varchar(50) DEFAULT NULL,
  `descriptions` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `report` */

insert  into `report`(`rid`,`kudumbasree_id`,`date`,`file`,`descriptions`) values 
(1,2,'2021-12-24','/static/festval/Screenshot (2).png','danish'),
(2,4,'2021-12-01','/static/festval/Screenshot (2).png','danish'),
(5,4,'2021-11-30','/static/festval/Screenshot (3).png','daniman'),
(6,0,'2021-12-01',NULL,'danish'),
(7,0,'2021-12-02',NULL,'babu'),
(8,0,'2021-12-03',NULL,'babu2'),
(9,0,'2021-12-04',NULL,'prabhu'),
(10,0,'2021-12-01',NULL,'da'),
(11,0,'2021-12-02',NULL,'da'),
(12,0,'2021-12-11',NULL,'di'),
(13,4,'0000-00-00',NULL,'danish'),
(14,4,'2021-11-30',NULL,'sdwdwdwdwdcwd'),
(15,4,'2021-12-02',NULL,'dd'),
(16,0,'0000-00-00','',''),
(17,4,'2021-12-01','/static/upload_file/Screenshot (1).png','kalladi'),
(18,4,'2021-12-02','/static/upload_file/Screenshot (1).png','manarakad');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `u_id` int(50) NOT NULL AUTO_INCREMENT,
  `l_id` int(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_no` bigint(50) DEFAULT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`u_id`,`l_id`,`name`,`place`,`post`,`pin`,`district`,`email`,`phone_no`) values 
(2,3,'danish','melattur','post',78899999,'hgfkhdgfdsgf','danish@gmail.com',88888888888),
(4,2,'anu','vatalkara','posr',54332,'calicut','a@g,c',99999999999);

/*Table structure for table `user_complaint` */

DROP TABLE IF EXISTS `user_complaint`;

CREATE TABLE `user_complaint` (
  `uc_id` int(50) NOT NULL AUTO_INCREMENT,
  `from_id` varchar(50) DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`uc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `user_complaint` */

insert  into `user_complaint`(`uc_id`,`from_id`,`complaint`,`reply`,`date`,`status`) values 
(1,'2','ssssss','1111111111','2020-12-26','replied'),
(2,'3','dddddd','danish','2021-12-22','replied'),
(3,'4','not good','danish','2021-12-07','replied');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
