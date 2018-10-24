/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
/*			       Company	database			*/
/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */


INSERT INTO Department VALUES (1, 'SALES', '00110', STR_TO_DATE('02/01/2012', '%d/%m/%Y'));
INSERT INTO Department VALUES (2, 'ACCOUNTING', '00120', STR_TO_DATE('30/10/2010', '%d/%m/%Y'));
INSERT INTO Department VALUES (3, 'GAMES', '00150', STR_TO_DATE('01/03/2008', '%d/%m/%Y'));
INSERT INTO Department VALUES (4, 'HUMAN RESOURCES', '00200', STR_TO_DATE('02/01/2013', '%d/%m/%Y'));
INSERT INTO Department VALUES (5, 'SPORTS', '00250', STR_TO_DATE('10/05/2010', '%d/%m/%Y'));


INSERT INTO DeptLocation VALUES (1, '1 gipps road, Wollongong, NSW 2500');
INSERT INTO DeptLocation VALUES (1, '10 Jones Street, Sydney, NSW 2000');
INSERT INTO DeptLocation VALUES (1, '25 Gore Street, Melbourne, VIC 3065');
INSERT INTO DeptLocation VALUES (2, '108 George Street, Sydney, NSW 2000');
INSERT INTO DeptLocation VALUES (3, '183 Pier Street, Sydney, NSW 2000');
INSERT INTO DeptLocation VALUES (3, '64 Smith Street, Wollongong, NSW 2500');
INSERT INTO DeptLocation VALUES (4, '4 Elizabeth Street, Sydney, NSW 2000');
INSERT INTO DeptLocation VALUES (5, '77 Kenny Street, Wollongong, NSW 2500');
INSERT INTO DeptLocation VALUES (5, '263 Box road, Sydney, NSW 2170');


INSERT INTO Employee VALUES ('00100', 'Albert', STR_TO_DATE('13/10/1965', '%d/%m/%Y'), '12 Robert street, Woonona, NSW 2517', 'M', 186.5, NULL, NULL);
INSERT INTO Employee VALUES ('00110', 'Alvin', STR_TO_DATE('13/10/1977', '%d/%m/%Y'), '56 Marlo road, Wollongong, NSW 2500', 'M', 156.4, '00100', 1);
INSERT INTO Employee VALUES ('00120', 'Alice', STR_TO_DATE('17/06/1973', '%d/%m/%Y'), '43 Collaery road, Russell Vale, NSW 2517', 'F', 156.5, '00100', 2);
INSERT INTO Employee VALUES ('00150', 'Bob', STR_TO_DATE('02/07/1960', '%d/%m/%Y'), '23 Kendall street, Wollongong, NSW 2500', 'M', 166.4, '00100', 3);
INSERT INTO Employee VALUES ('00200', 'Carl', STR_TO_DATE('02/02/1967', '%d/%m/%Y'), '44 Mount Keira road, West Wollongong, NSW 2500', 'M', 156.3, '00100', 4);
INSERT INTO Employee VALUES ('00250', 'Douglass', STR_TO_DATE('14/04/1983', '%d/%m/%Y'), '78 Uralba street, West Wollongong, NSW 2500', 'M', 156.4, '00100', 5);
INSERT INTO Employee VALUES ('00101', 'Peter', STR_TO_DATE('13/11/1976', '%d/%m/%Y'), '77 Gipps road, Wollongong, NSW 2500', 'M', 85.2, '00110', 1);
INSERT INTO Employee VALUES ('00103', 'Ami', STR_TO_DATE('12/09/1985', '%d/%m/%Y'), '51 Mackie street, Coniston, NSW 2500', 'F', 78.2, '00110', 1);
INSERT INTO Employee VALUES ('00107', 'Wendy', STR_TO_DATE('12/09/1988', '%d/%m/%Y'), '41 Wall street, Wollongong, NSW 2500', 'F', 68.2, '00110', 1);
INSERT INTO Employee VALUES ('00109', 'Michael', STR_TO_DATE('12/09/1990', '%d/%m/%Y'), '112 Smith road, Wollongong, NSW 2500', 'M', 58.2, '00110', 1);
INSERT INTO Employee VALUES ('00125', 'Angela', STR_TO_DATE('20/11/1990', '%d/%m/%Y'), '23 Gibsons road, Figtree, NSW 2525', 'F', 56.4, '00120', 2);
INSERT INTO Employee VALUES ('00105', 'Robert', STR_TO_DATE('15/01/1986', '%d/%m/%Y'), '66 Risely road, Figtree, NSW 2525', 'M', 66.2, '00150', 3);
INSERT INTO Employee VALUES ('00136', 'Aban', STR_TO_DATE('15/01/1990', '%d/%m/%Y'), '187 Princes Highway, Wollongong, NSW 2500', 'M', 55.3, '00200', 4);
INSERT INTO Employee VALUES ('00187', 'Eadger', STR_TO_DATE('07/04/1986', '%d/%m/%Y'), '73 Ocean street, Wollongong, NSW 2500', 'M', 76.5, '00250', 5);


INSERT INTO Project VALUES (1001, 'Computation', 'Microsoft', 1, 25000);
INSERT INTO Project VALUES (1002, 'Study methods', 'Education committee', 3, 15000);
INSERT INTO Project VALUES (1003, 'Racing car', 'Cloud Pty Ltd', 3, 225000);
INSERT INTO Project VALUES (1004, 'Football', 'Football club', 5, 35000);
INSERT INTO Project VALUES (1005, 'Swimming', 'Education committee', 5, 125000);


INSERT INTO WorksOn VALUES ('00110', 1001, 10);
INSERT INTO WorksOn VALUES ('00101', 1001, 20);
INSERT INTO WorksOn VALUES ('00150', 1002, 10);
INSERT INTO WorksOn VALUES ('00105', 1002, 10);
INSERT INTO WorksOn VALUES ('00105', 1003, 20);
INSERT INTO WorksOn VALUES ('00105', 1004, 20);
INSERT INTO WorksOn VALUES ('00250', 1004, 15);
INSERT INTO WorksOn VALUES ('00187', 1004, 25);
INSERT INTO WorksOn VALUES ('00105', 1005, 15);


INSERT INTO Dependent VALUES ('00100', 'Judy', 'F', STR_TO_DATE('11/03/1966', '%d/%m/%Y'), 'SPOUSE');
INSERT INTO Dependent VALUES ('00100', 'Bolt', 'M', STR_TO_DATE('05/03/1986', '%d/%m/%Y'), 'SON');
INSERT INTO Dependent VALUES ('00100', 'Edee', 'F', STR_TO_DATE('11/03/1989', '%d/%m/%Y'), 'DAUGHTER');
INSERT INTO Dependent VALUES ('00120', 'Blues', 'M', STR_TO_DATE('11/03/1975', '%d/%m/%Y'), 'SPOUSE');
INSERT INTO Dependent VALUES ('00120', 'Kadi', 'F', STR_TO_DATE('05/03/2001', '%d/%m/%Y'), 'DAUGHTER');
INSERT INTO Dependent VALUES ('00120', 'Edee', 'F', STR_TO_DATE('15/05/2003', '%d/%m/%Y'), 'DAUGHTER');
INSERT INTO Dependent VALUES ('00187', 'Angela', 'F', STR_TO_DATE('15/05/2003', '%d/%m/%Y'), 'SPOUSE');


ALTER TABLE Department ADD CONSTRAINT Department_FK FOREIGN KEY (Manager)
	REFERENCES Employee (ENumber);

/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
