CREATE TABLE Message(
	id Integer Not null Identity,
	texte varchar(1024) Not null,
	dateMessage dateTime Not null,
	idUtil Integer Not null,
	idSalon Integer Not null,
	Primary key(id),
	Foreign key(idUtil) References Utilisateur(id),
	Foreign key(idSalon) References Salon(id)
)