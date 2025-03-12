create table dates (
id serial primary key unique,
date timestamp unique
);

create table rooms (
date_id int,
room_number int,
count_of_windows int,
foreign key (date_id) references dates(id)
);

create table lights (
date_id int,
floor_number int,
light_number int,
is_on bool,
foreign key (date_id) references dates(id)
);

create table answer (
data_id int,
room int
);