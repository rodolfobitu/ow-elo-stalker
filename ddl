create SCHEMA ow;

create table ow.users (
  id serial PRIMARY KEY,
  battletag varchar(30) UNIQUE,
  region varchar(30),
  platform varchar(30)
);

create table ow.users_ranked (
  timestamp timestamp without time zone default (now() at time zone 'utc'),
  user_id int4 references ow.users(id),
  elo integer
);
