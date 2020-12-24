CREATE TABLE Salon(
	id Integer Not null Identity,
	nomSalon varchar(255) Not null,
	idUtil Integer Not null,
	Primary key(id),
	Foreign key(idUtil) References Utilisateur(id)
)