CREATE TABLE Message(
	id Integer Not null Identity Primary key,
	texte varchar(1024) Not null,
	dateMessage dateTime Not null
)
