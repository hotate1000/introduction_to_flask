-- SQLite
create table users(
    id integer primary key,
    username varchar,
    email varchar,
    password_hash varchar,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP
);