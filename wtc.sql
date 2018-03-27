create schema wtc;

create table wtc.stat (
  id bigserial PRIMARY KEY,
  crossid id
);

create table wtc.cross (
  id int PRIMARY KEY ,
  startdate timestamp DEFAULT now(),
  netaddr inet NOT NULL ,
  addr text NOT NULL
) ;

CREATE TABLE wtc.cams (
  id INTEGER PRIMARY KEY ,
  startdate TIMESTAMP DEFAULT now(),
  crossid INTEGER REFERENCES wtc.cross(id),
  netaddr inet NOT NULL ,
  addr text NOT NULL
);

CREATE TABLE wtc.zones (
  id INTEGER PRIMARY KEY ,
  startdate TIMESTAMP DEFAULT now(),
  camid INTEGER REFERENCES wtc.cams(id),
  zshape text DEFAULT ('poligon') NOT NULL ,
  ztype char(1) DEFAULT 's' NOT NULL,
  idbycam int NOT NULL
);

CREATE TABLE wtc.zpoints (
  id INTEGER PRIMARY KEY ,
  startdate TIMESTAMP default now(),
  enddate timestamp,
  idbyzone int NOT NULL ,
  zoneid integer references wtc.zones(id)
);

create schema wtcu;

drop TABLE entity;
create table wtcu.entity (
  id SERIAL PRIMARY KEY ,
  ownerid INTEGER,
  name text NOT NULL
);
drop table property;

create TABLE  wtcu.property (
  id serial PRIMARY KEY ,
  entityid INTEGER NOT NULL ,
  name text NOT NULL
);
drop TABLE  statdata;
create table wtcu.statdata (
  id BIGSERIAL PRIMARY KEY ,
  dt timestamp NOT NULL ,
  dint INTEGER,
  dstring text,
  propid INTEGER not null
);

CREATE TABLE objects(
  
);

INSERT  into entity (ownerid, name) VALUES (null, 'root');
insert into entity (ownerid, name) VALUES (1, 'Crosses');
insert into entity (ownerid, name) VALUES (2, 'Cameras');
insert into entity (ownerid, name) VALUES (3, 'Zones');
select * from entity;

update entity set ownerid=1 where ownerid is not null;

insert into property (entityid, name) VALUES (3,'Name');
insert into property (entityid, name) VALUES (3,'NetAddress');
insert into property (entityid, name) VALUES (3,'Address');
insert into property (entityid, name) VALUES (3,'StartDate');
insert into property (entityid, name) VALUES (3,'CrossId');

SELECT * FROM property;