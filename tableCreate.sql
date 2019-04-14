-- Created:29Mar Author:Ye

CREATE TABLE USERS1 (
  UserID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Username varchar(32) NOT NULL,
  Password varchar(256) NOT NULL,
  Admin int DEFAULT 0 NOT NULL
);

CREATE TABLE MESSAGES1 (
  MessageID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  UserID int NOT NULL,
  Message varchar(140) NOT NULL,
  Timestamp DATETIME NOT NULL
);

INSERT INTO USERS1 (Username,Password,Admin)
  VALUES("root","9c03c5265606e5da39ca2dcc5982d1be88ec2749904860cf37948bb6ee3fe501",1);
