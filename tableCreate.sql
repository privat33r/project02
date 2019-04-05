-- Created:29Mar Author:Ye

CREATE TABLE USERS (
  UserID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Username varchar(32) NOT NULL,
  Password varchar(256) NOT NULL
);

CREATE TABLE MESSAGES (
  MessageID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  UserID int NOT NULL,
  Message varchar(140)
);

INSERT INTO USERS(Username,Password)
  VALUES("root","yeyeyeye");
