DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
  id SERIAL,
  name varchar(200) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TEMPORARY SEQUENCE artistid START 1;

insert into artists values(1,'Kate Bush');
insert into artists values(2,'Tom waits');

DROP TABLE IF EXISTS records;

CREATE TABLE records (
  id SERIAL,
  name varchar(200) DEFAULT NULL,
  title varchar(200) DEFAULT NULL,
  description text DEFAULT NULL,
  year int,
  artistname varchar(200) DEFAULT NULL,
  worth varchar(200) DEFAULT NULL,
  damage text DEFAULT NULL,
  serial_nr varchar(200) DEFAULT NULL,
  cover_image text DEFAULT NULL,
  PRIMARY KEY (id)
);

insert into records values(1,'Hounds of Love','','chou zhu''s fav', 1985, 'Kate Bush', '100 Pound','','','https://tubbs-on-aws.s3.eu-central-1.amazonaws.com/Katebushhoundsoflove_wiki.png');
insert into records values(2,'The Kick Inside','','my fav', 1978, 'Kate Bush', '500 Pound','','','https://tubbs-on-aws.s3.eu-central-1.amazonaws.com/The_Kick_Inside_(Album_Artwork).png');
insert into records values(3,'50 words of snow','','the best of kate', 2011, 'Kate Bush', '500 dollors','','','https://upload.wikimedia.org/wikipedia/en/thumb/0/06/Kate_Bush_-_50_Words_for_Snow.png/220px-Kate_Bush_-_50_Words_for_Snow.png');
