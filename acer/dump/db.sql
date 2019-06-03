CREATE DATABASE /*!32312 IF NOT EXISTS*/ `battles` /*!40100 DEFAULT CHARACTER SET utf8 */;

DROP TABLE IF EXISTS `racecondition`;
CREATE TABLE `racecondition` (
  `login` text NOT NULL,
  `password` text NOT NULL,
  `coin` int(6) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;