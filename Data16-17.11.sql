--vytvoření databáze
CREATE DATABASE DATA_ANALYST;

--vytvoření Tabulky Departments
CREATE TABLE Departments (
    Department_ID INT PRIMARY KEY,
    Department_Name VARCHAR(100)
);

--vytvoření Tabulky Employees
CREATE TABLE Employees (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department_ID INT,
    Hire_Date DATE
);
--vytvoření Tabulky Salaries
CREATE TABLE Salaries (
    ID int PRIMARY KEY,
    Employee_ID int,
    Salary int
);

--vložení hodnot do tabulky departments
INSERT INTO Departments (Department_ID, Department_Name)
VALUES 
(101,'Education officer, museum')
,(102,'Editor, film/video')
,(103,'Engineer, production')
,(104,'Doctor, general practice')
,(105,'Psychologist, clinical')
,(106,'Petroleum engineer')
,(107,'TEFL teacher')
,(108,'Engineer, civil (consulting)')
,(109,'Conservation officer, nature')
,(110,'Psychotherapist');

--vložení hodnot do tabulky Employees
INSERT INTO Employees ( ID,   Name,    Department_ID,    Hire_Date)
VALUES 
(1,'Ronald Faulkner',102,'2022-3-31'),
(2,'James Shepard',110,'2021-10-12'),
(3,'Lydia Torres',105,'2022-8-5'),
(4,'Christopher Cruz',103,'2021-7-17'),
(5,'Travis Shaw',101,'2023-11-26'),
(6,'Tracy Mathews',108,'2023-1-12'),
(7,'Nicole Morales',107,'2021-5-16'),
(8,'Elizabeth Hamilton',104,'2020-1-14'),
(9,'Kenneth Long',110,'2020-9-22'),
(10,'Mark Hubbard',109,'2023-4-2'),
(11,'Caitlin Brewer',108,'2021-11-23'),
(12,'Amber Preston',110,'2023-5-10'),
(13,'Jeremy Clark',110,'2019-11-18'),
(14,'Karen Hayes',107,'2019-11-27'),
(15,'Kevin Ware',107,'2021-6-8'),
(16,'Richard Cummings',110,'2022-2-8'),
(17,'Brittany Soto PhD',110,'2021-9-1'),
(18,'Derek Marquez',104,'2021-6-19'),
(19,'Sara Smith PhD',102,'2021-10-27'),
(20,'Andrew Evans',103,'2021-3-5'),
(21,'Donna Holden',102,'2023-11-10'),
(22,'Christopher Fry',103,'2022-11-21'),
(23,'Mark Miller',105,'2024-1-6'),
(24,'Susan Schultz',103,'2024-2-4'),
(25,'Jillian Keith PhD',109,'2024-1-13'),
(26,'Christine Cruz',106,'2020-1-9'),
(27,'Candice Johnson',106,'2020-2-8'),
(28,'Jamie Hardy',101,'2022-4-10'),
(29,'Michael Hall',109,'2020-7-27'),
(30,'Michael Richardson',110,'2024-7-26'),
(31,'Robert Woods',102,'2023-10-5'),
(32,'Robert Jackson',109,'2020-6-27'),
(33,'Robert Atkinson',103,'2020-8-18'),
(34,'Dominique Moore',105,'2022-5-14'),
(35,'John Ramsey',101,'2023-5-24'),
(36,'Philip Myers',110,'2020-7-11'),
(37,'Kimberly Cannon',110,'2024-3-24'),
(38,'Alexis Barnes',107,'2022-3-7'),
(39,'Steven Diaz',105,'2020-11-5'),
(40,'Amy Meadows',104,'2020-3-4'),
(41,'Anthony Proctor',106,'2022-4-8'),
(42,'Donald Becker',109,'2021-8-31'),
(43,'David Gonzalez',110,'2021-4-30'),
(44,'Tyler Ford',107,'2023-12-12'),
(45,'Kevin Serrano',110,'2023-9-17'),
(46,'Kevin Jones',107,'2024-8-13'),
(47,'Nicholas Hamilton',105,'2020-2-8'),
(48,'Michael Hughes DVM',109,'2024-7-27'),
(49,'Christopher Martin',106,'2023-10-10'),
(50,'Alexander Smith',106,'2021-4-8'),
(51,'Karen Davis',108,'2023-7-5'),
(52,'Christine Acosta',107,'2022-4-5'),
(53,'Robin Baker',109,'2023-9-29'),
(54,'Michelle Harmon',109,'2020-11-16'),
(55,'Katelyn Reed',106,'2023-9-22'),
(56,'James Nelson',103,'2021-7-18'),
(57,'David Smith',109,'2023-8-16'),
(58,'Bryan Reed MD',108,'2021-9-4'),
(59,'Timothy Hooper',110,'2021-7-26'),
(60,'Randy Smith',101,'2024-11-5'),
(61,'Maria Martinez',106,'2024-2-1'),
(62,'Kathleen Williams',103,'2024-1-22'),
(63,'Chelsea Henson',102,'2024-6-20'),
(64,'Connie Whitney',109,'2022-2-26'),
(65,'Adam Valenzuela',102,'2020-9-21'),
(66,'John Richmond',101,'2023-5-4'),
(67,'Erica Green',104,'2023-1-6'),
(68,'Heather Silva',103,'2023-6-27'),
(69,'Peter Johnson',109,'2021-4-15'),
(70,'Monica Steele',104,'2022-10-14'),
(71,'Leon Sanchez',106,'2023-7-17'),
(72,'Jacob Kennedy DDS',105,'2022-5-10'),
(73,'Todd Brown',104,'2023-2-3'),
(74,'Jason Christian',109,'2021-10-9'),
(75,'Pam Marshall',106,'2024-5-30'),
(76,'Michael Gibson',110,'2020-7-18'),
(77,'Aaron Ross',105,'2023-6-21'),
(78,'Wendy Calhoun',102,'2024-2-15'),
(79,'David Spencer',103,'2023-5-22'),
(80,'Renee Chavez',110,'2024-7-6'),
(81,'Charles Moody',108,'2022-9-7'),
(82,'Connor Lin',109,'2020-2-23'),
(83,'Donald Martinez',110,'2024-7-24'),
(84,'Danielle Vasquez',104,'2020-7-30'),
(85,'John Nguyen',105,'2023-5-11'),
(86,'Thomas Ellison',108,'2023-10-19'),
(87,'Kayla Diaz',105,'2024-5-24'),
(88,'Caleb Miller',110,'2020-6-21'),
(89,'Ashley Torres',110,'2023-3-19'),
(90,'Shane Lowe',101,'2019-11-28'),
(91,'William Bray',101,'2021-3-29'),
(92,'Henry Mitchell',109,'2020-3-23'),
(93,'Henry Johnson',109,'2022-12-16'),
(94,'Kathleen Johnson',106,'2022-12-27'),
(95,'Jodi Williams MD',102,'2021-11-20'),
(96,'Melanie Murray',106,'2023-9-15'),
(97,'Austin Jackson',101,'2022-4-20'),
(98,'Sean Davis',103,'2022-5-23'),
(99,'Priscilla Woodard',102,'2023-2-19'),
(100,'Ryan Bennett',110,'2022-8-14'),
(101,'Karen Bullock',108,'2023-9-8'),
(102,'Eric Ramirez',109,'2023-12-2'),
(103,'Tina Williamson',102,'2022-1-28'),
(104,'Leah Roberts',109,'2021-7-26'),
(105,'Patricia Salas',110,'2022-7-23'),
(106,'Karen Hull',105,'2023-6-10'),
(107,'Jason Christensen',105,'2022-4-8'),
(108,'Kristin Foley',106,'2022-8-8'),
(109,'Jason Martin',102,'2023-12-4'),
(110,'Christina Jimenez',104,'2022-1-1'),
(111,'Katherine Santos',102,'2023-9-24'),
(112,'John Nguyen',108,'2021-3-7'),
(113,'Barbara Moore',104,'2022-1-14'),
(114,'Pamela Madden',106,'2021-6-10'),
(115,'Henry Rogers',105,'2024-6-4'),
(116,'Margaret Gill',103,'2020-11-10'),
(117,'Michael Kelly',103,'2020-8-29'),
(118,'Jane Johnson',109,'2024-7-13'),
(119,'James Horne',101,'2023-5-10'),
(120,'Mary Scott',106,'2024-4-11'),
(121,'Patrick Collins',102,'2022-1-24'),
(122,'Drew Williams',110,'2024-6-28'),
(123,'Alison Christensen',110,'2020-7-17'),
(124,'Tiffany Dickson',109,'2023-2-28'),
(125,'William Evans',110,'2022-10-25'),
(126,'James Day',107,'2019-11-20'),
(127,'Nicholas Martinez',108,'2023-4-5'),
(128,'Michael Gallegos',103,'2019-12-20'),
(129,'Alexander Taylor',108,'2021-5-25'),
(130,'David Osborn',104,'2022-3-31'),
(131,'Jeanne Clay',110,'2023-9-28'),
(132,'Jacob Fleming',110,'2023-10-25'),
(133,'Patrick Jones',105,'2020-12-5'),
(134,'Joseph Rangel',101,'2022-12-20'),
(135,'Joseph Barker',106,'2024-4-6'),
(136,'Richard Hamilton',104,'2020-1-28'),
(137,'Edward Cole',104,'2024-8-27'),
(138,'Daniel Calhoun',104,'2023-5-3'),
(139,'Emily Newton',103,'2022-7-18'),
(140,'Anita Dixon',106,'2022-1-7'),
(141,'Brady Cochran',105,'2023-6-19'),
(142,'Dylan Mcgee',105,'2020-7-4'),
(143,'Robert Randall',109,'2023-6-7'),
(144,'Patrick Williams',110,'2020-12-19'),
(145,'Abigail Richardson',108,'2021-8-30'),
(146,'Ernest Aguilar',109,'2020-7-25'),
(147,'Kelly Jimenez',101,'2021-11-22'),
(148,'William Wright',106,'2024-11-12'),
(149,'Katherine Brady',105,'2021-2-7'),
(150,'John Maldonado',110,'2023-1-3'),
(151,'Robert Sherman',102,'2021-9-5'),
(152,'Kendra Rivera',101,'2021-3-23'),
(153,'Kristina Harrell',110,'2023-8-5'),
(154,'Paul Huber',101,'2020-11-30'),
(155,'Duane Orr',104,'2023-6-21'),
(156,'Mr. Kyle Mitchell',105,'2021-8-26'),
(157,'Alexander Reilly',101,'2020-11-27'),
(158,'Alex Hardy',103,'2020-7-10'),
(159,'Justin Woods',109,'2021-8-2'),
(160,'Amanda Dickson',102,'2022-10-26'),
(161,'Caitlin Wise',108,'2020-3-29'),
(162,'Angel Mathis',104,'2020-6-8'),
(163,'Kyle Brown',104,'2023-9-25'),
(164,'Carol Taylor',107,'2024-4-12'),
(165,'Corey Griffin',109,'2021-8-4'),
(166,'Hector Todd',104,'2023-11-14'),
(167,'Arthur Barber',107,'2022-10-14'),
(168,'Brandon Cantrell',102,'2020-4-14'),
(169,'Traci Davenport',107,'2020-6-24'),
(170,'Danielle Powell',110,'2023-1-8'),
(171,'Dr. Misty James',104,'2020-8-6'),
(172,'Susan Martin',103,'2024-8-31'),
(173,'Matthew Robinson',106,'2024-3-13'),
(174,'Gregory Thomas',104,'2021-6-11'),
(175,'Laura Lopez',106,'2023-2-5'),
(176,'Wanda Potter',105,'2021-7-29'),
(177,'Robert Ross',103,'2021-2-17'),
(178,'Erin Sullivan',107,'2023-1-19'),
(179,'James Torres',106,'2024-10-6'),
(180,'Joseph Sharp',109,'2024-6-22'),
(181,'Felicia Jarvis',109,'2020-11-14'),
(182,'John Lin',101,'2024-7-5'),
(183,'Mr. Anthony Moss',109,'2021-6-7'),
(184,'Allison Hernandez',108,'2020-11-12'),
(185,'Shawn Sweeney',107,'2024-5-9'),
(186,'William Huber',106,'2023-11-12'),
(187,'Dr. Charles Barber',109,'2023-3-23'),
(188,'Keith Martinez',103,'2022-4-22'),
(189,'Eric Rich',109,'2023-8-25'),
(190,'Anthony Williams',110,'2020-2-2'),
(191,'Stephanie Boyle',102,'2020-4-11'),
(192,'Alexander Williams',101,'2023-3-4'),
(193,'Sean Combs',101,'2024-2-23'),
(194,'William Krause',105,'2022-1-30'),
(195,'Michael Walker',109,'2023-3-28'),
(196,'Jason Rivas',106,'2020-9-12'),
(197,'Jeffrey Lewis',104,'2021-1-16'),
(198,'Heather Stevenson',108,'2023-11-11'),
(199,'Kristen Harris',107,'2020-12-18'),
(200,'Robert Ewing',108,'2020-5-13')

--vložení hodnot do tabulky Salaries
INSERT INTO Salaries (    ID ,    Employee_ID ,    Salary)
Values
(1,1,73790),
(2,2,113404),
(3,3,91443),
(4,4,92269),
(5,5,63017),
(6,6,105409),
(7,7,100881),
(8,8,63157),
(9,9,115362),
(10,10,82716),
(11,11,93569),
(12,12,96625),
(13,13,98518),
(14,14,76915),
(15,15,91126),
(16,16,80229),
(17,17,95214),
(18,18,88982),
(19,19,61138),
(20,20,64647),
(21,21,82802),
(22,22,113248),
(23,23,69635),
(24,24,40368),
(25,25,102923),
(26,26,62730),
(27,27,68455),
(28,28,107415),
(29,29,115639),
(30,30,85262),
(31,31,78492),
(32,32,62523),
(33,33,105487),
(34,34,107875),
(35,35,93623),
(36,36,113173),
(37,37,114202),
(38,38,44343),
(39,39,43406),
(40,40,62541),
(41,41,113993),
(42,42,47501),
(43,43,100256),
(44,44,45071),
(45,45,68414),
(46,46,80624),
(47,47,61388),
(48,48,69159),
(49,49,44474),
(50,50,47405),
(51,51,43761),
(52,52,82505),
(53,53,55597),
(54,54,43206),
(55,55,70512),
(56,56,65269),
(57,57,110302),
(58,58,59472),
(59,59,103991),
(60,60,108117),
(61,61,70489),
(62,62,53828),
(63,63,110360),
(64,64,91112),
(65,65,43453),
(66,66,43720),
(67,67,54352),
(68,68,97134),
(69,69,49505),
(70,70,61656),
(71,71,55437),
(72,72,96263),
(73,73,95302),
(74,74,107626),
(75,75,91808),
(76,76,90511),
(77,77,53124),
(78,78,41326),
(79,79,91497),
(80,80,94202),
(81,81,88585),
(82,82,103890),
(83,83,94995),
(84,84,45510),
(85,85,74102),
(86,86,83319),
(87,87,73886),
(88,88,60302),
(89,89,43923),
(90,90,44215),
(91,91,89305),
(92,92,114479),
(93,93,64874),
(94,94,70777),
(95,95,100722),
(96,96,99933),
(97,97,44486),
(98,98,42815),
(99,99,114285),
(100,100,104695),
(101,101,50485),
(102,102,63587),
(103,103,73824),
(104,104,90225),
(105,105,78297),
(106,106,81733),
(107,107,46666),
(108,108,113888),
(109,109,100057),
(110,110,50981),
(111,111,96249),
(112,112,64327),
(113,113,86917),
(114,114,117563),
(115,115,49605),
(116,116,100678),
(117,117,117282),
(118,118,93582),
(119,119,93325),
(120,120,112248),
(121,121,87570),
(122,122,87922),
(123,123,54470),
(124,124,46815),
(125,125,104200),
(126,126,77715),
(127,127,94093),
(128,128,49147),
(129,129,42268),
(130,130,106481),
(131,131,112540),
(132,132,104247),
(133,133,101205),
(134,134,84747),
(135,135,99683),
(136,136,62071),
(137,137,93670),
(138,138,115533),
(139,139,40314),
(140,140,66523),
(141,141,64368),
(142,142,56049),
(143,143,48402),
(144,144,94640),
(145,145,41076),
(146,146,44475),
(147,147,81228),
(148,148,53574),
(149,149,68768),
(150,150,76112),
(151,151,59476),
(152,152,92577),
(153,153,71896),
(154,154,50117),
(155,155,40211),
(156,156,56739),
(157,157,86084),
(158,158,119443),
(159,159,45344),
(160,160,67025),
(161,161,49686),
(162,162,79008),
(163,163,45019),
(164,164,105106),
(165,165,116728),
(166,166,93351),
(167,167,54346),
(168,168,109869),
(169,169,45989),
(170,170,105767),
(171,171,68666),
(172,172,51379),
(173,173,98802),
(174,174,87975),
(175,175,79127),
(176,176,60569),
(177,177,59976),
(178,178,61599),
(179,179,83136),
(180,180,117267),
(181,181,53072),
(182,182,51736),
(183,183,62392),
(184,184,55790),
(185,185,74382),
(186,186,64120),
(187,187,92876),
(188,188,119075),
(189,189,71227),
(190,190,107494),
(191,191,114040),
(192,192,45939),
(193,193,54369),
(194,194,113386),
(195,195,54991),
(196,196,92580),
(197,197,96262),
(198,198,78751),
(199,199,48803),
(200,200,83824)

--Department name, počet zaměstnanců a průměrný plat zaokrouhlený na 2 desetinná místa 
select 
    A.`Department_Name`
    ,count(B.`Name`) as 'pocet_zamestancu'
    ,ROUND(AVG(C.`Salary`),2) as 'průměrný_plat'
from departments A 
LEFT JOIN employees B ON A.`Department_ID`=B.`Department_ID`
LEFT JOIN salaries C ON B.`Department_ID`=C.`Employee_ID`
group by 
    A.`Department_ID`


--průměrný plat pro oddělení za pomoci "WITH"

With EmployeesSalaries as (
    Select
    A.`Department_ID`, B.Salary
    From employees A JOIN salaries B ON A.ID=B.Employee_ID
)
Select
    C.`Department_Name`
    , SUM( D.Salary) as 'průměrný plat'
From departments C JOIN EmployeesSalaries D on C.`Department_ID`= D.`Department_ID`
Group by 
    C.`Department_Name`
Order by SUM( D.Salary) DESC


--oddělení, které má platy vyšší než 2M, tak vypsat jejich zaměstnance a platy, a jejich oddělení
-- a deklarování proměnné

Declare @TIMESTAMP='2024-01-01'
With EmployeesSalaries as (
    Select
    A.`Department_ID`, Sum(B.Salary) As 'suma platů'
    From employees A JOIN salaries B ON A.ID=B.Employee_ID
    Group by  A.`Department_ID`
    HAVING Sum(B.Salary)>2000000
    order by Sum(B.Salary) DESC
)
Select
    D.`Department_Name`,C.`Name`, E.`Salary`
From employees C 
JOIN departments D ON C.`Department_ID`=D.`Department_ID`
JOIN salaries E ON C.`ID`=E.`Employee_ID`
Where C.Department_ID in (Select `Department_ID` from `EmployeesSalaries`) and TIMESTAMP>@timestamp
Order by E.`Salary` DESC


-- více podmínek dle klasického AND a dle příkaz NOT IN
Select *
From Departments
Where Department_ID<> 101 and  Department_ID<>103 and  Department_ID<>106

Select *
From Departments
Where Department_ID NOT IN (101,103,106)


-- oddělení a jejich celkové platy platy, zobrazení oddělení jen nad 2.000.000
With EmployeesSalaries as (
    Select
    A.`Department_ID`, Sum(B.Salary) As 'suma platů'
    From employees A JOIN salaries B ON A.ID=B.Employee_ID
    Group by  A.`Department_ID`
    HAVING Sum(B.Salary)>2000000
    order by Sum(B.Salary) DESC
)
Select
   C.`Department_ID`,C.`Name`
From employees C 
Where C.Department_ID not in (Select `Department_ID` from `EmployeesSalaries`)

--Suma > 1000000 a zároveň počet zaměstanců na daném oddělení < 20
With EmployeesSalaries as (
    Select
    A.`Department_ID`, Sum(B.Salary) As 'suma platů'
    From employees A JOIN salaries B ON A.ID=B.Employee_ID
    Group by  A.`Department_ID`
    HAVING Sum(B.Salary)>1000000
),
PrumPocet as (
    Select
        F.department_ID,
        COUNT(F.Name)
    From employees F
    Group by F.department_ID
    Having COunt(F.name)<20
)
Select
    D.`Department_Name`,C.`Name`, E.`Salary`
From employees C 
JOIN departments D ON C.`Department_ID`=D.`Department_ID`
JOIN salaries E ON C.`ID`=E.`Employee_ID`
Where C.Department_ID in (Select `Department_ID` from `EmployeesSalaries`) and D.`Department_ID` in (Select department_ID from PrumPocet )

