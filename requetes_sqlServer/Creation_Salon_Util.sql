Create table Salon_Util(
	idUtil Integer Not null,
	idSalon Integer Not null,
	Primary key (idUtil,idSalon),
	Foreign key(idUtil) References Utilisateur(id),
	Foreign key (idSalon) References Salon(id)
)