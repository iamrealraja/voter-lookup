
create table state (
	code char(2) primary key,
	name text,
	last_updated datetime default (current_timestamp at time zone 'utc')
);

create table voterid (
	state char(2) references state,
	ac smallint,
	pb smallint,
	voterid text	
);
