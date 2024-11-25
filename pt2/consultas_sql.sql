CREATE DATABASE vendas_2023;
USE vendas_2023;

CREATE TABLE vendas (
    ID int PRIMARY KEY,
    Data DATE NOT NULL,
    Produto VARCHAR(255) NOT NULL,
    Categoria VARCHAR(255) NOT NULL,
    Quantidade INT NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL
);

-- Tentei fazer com o BULK INSERT e manual e não consegui, tive que apelar, rs
INSERT INTO vendas(ID, Data, Produto, Categoria, Quantidade, Preco) VALUES 
(1, '2023-04-13', 'Produto B', 'Categoria 1', 14.0, 37.08),
(2, '2023-12-15', 'Produto B', 'Categoria 1', 7.0, 35.64),
(3, '2023-09-28', 'Produto B', 'Categoria 2', 9.0, 13.32),
(4, '2023-04-17', 'Produto A', 'Categoria 3', 15.0, 64.86),
(5, '2023-03-13', 'Produto B', 'Categoria 1', 15.0, 55.24),
(6, '2023-07-08', 'Produto A', 'Categoria 2', 9.74, 14.63),
(7, '2023-01-21', 'Produto B', 'Categoria 1', 13.0, 35.08),
(8, '2023-04-13', 'Produto D', 'Categoria 1', 19.0, 91.74),
(9, '2023-05-02', 'Produto D', 'Categoria 1', 7.0, 31.56),
(10, '2023-08-03', 'Produto C', 'Categoria 1', 17.0, 23.04),
(11,'2023-11-27','Produto D','Categoria 3',4.0,51.64019999999999),
(12,'2023-03-29','Produto C','Categoria 1',5.0,98.71),
(13,'2023-04-10','Produto D','Categoria 1',7.0,31.78),
(14,'2023-12-26','Produto A','Categoria 1',13.0,70.49),
(15,'2023-06-01','Produto D','Categoria 3',15.0,78.55),
(16,'2023-05-11','Produto C','Categoria 1',11.0,31.39),
(17,'2023-05-30','Produto C','Categoria 1',4.0,75.54),
(18,'2023-11-05','Produto B','Categoria 3',13.0,43.1),
(19,'2023-09-15','Produto A','Categoria 3',7.0,66.91),
(20,'2023-12-10','Produto D','Categoria 3',19.0,67.02),
(21,'2023-10-21','Produto B','Categoria 1',2.0,58.22),
(22,'2023-07-11','Produto D','Categoria 3',10.0,18.13),
(23,'2023-10-04','Produto D','Categoria 3',13.0,85.18),
(24,'2023-06-10','Produto B','Categoria 1',6.0,38.87),
(25,'2023-11-10','Produto B','Categoria 3',12.0,26.79),
(26,'2023-01-22','Produto B','Categoria 1',12.0,13.67),
(27,'2023-09-10','Produto B','Categoria 2',11.0,63.18),
(28,'2023-08-24','Produto B','Categoria 3',7.0,70.98),
(29,'2023-12-11','Produto D','Categoria 2',1.0,11.49),
(30,'2023-02-18','Produto B','Categoria 1',1.0,56.09),
(31,'2023-02-28','Produto A','Categoria 3',13.0,30.38),
(32,'2023-06-19','Produto C','Categoria 1',9.0,68.07),
(33,'2023-07-07','Produto B','Categoria 2',3.0,25.69),
(34,'2023-09-28','Produto B','Categoria 1',7.0,72.18),
(35,'2023-07-09','Produto D','Categoria 3',6.0,44.81),
(36,'2023-06-24','Produto B','Categoria 3',8.0,94.31),
(37,'2023-02-20','Produto B','Categoria 2',9.0,22.38),
(38,'2023-12-30','Produto B','Categoria 1',5.0,40.7),
(39,'2023-02-24','Produto D','Categoria 3',1.0,20.21),
(40,'2023-09-01','Produto B','Categoria 2',19.0,93.22),
(41,'2023-11-16','Produto C','Categoria 3',10.0,88.96),
(42,'2023-05-11','Produto D','Categoria 3',12.0,33.21),
(43,'2023-11-03','Produto C','Categoria 1',15.0,69.4),
(44,'2023-05-15','Produto D','Categoria 3',9.0,83.55),
(45,'2023-01-21','Produto B','Categoria 1',17.0,59.97),
(46,'2023-11-25','Produto C','Categoria 3',17.0,57.67),
(47,'2023-06-16','Produto D','Categoria 2',12.0,31.77),
(48,'2023-10-01','Produto A','Categoria 3',7.0,18.38),
(49,'2023-03-30','Produto B','Categoria 1',2.0,90.75),
(50,'2023-11-12','Produto D','Categoria 1',3.0,91.04)


--=-=-=-=-=-=-= CONSULTAS -=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=

SELECT*
  FROM [vendas_2023].[dbo].[vendas]

-- Consulta 1: Listar o nome do produto, categoria e a soma total de vendas para cada produto, em ordem decrescente
SELECT 
    Produto,
    Categoria,
    SUM(Quantidade * Preco) AS Total_Vendas
FROM 
    vendas
GROUP BY 
    Produto, Categoria
ORDER BY 
    Total_Vendas DESC;


-- Consulta 2: Identificar os produtos que venderam menos no mês de junho de 2024
SELECT TOP 10
    Produto,
    Categoria,
    SUM(Quantidade) AS Total_Quantidade_Vendida
FROM 
    vendas
WHERE 
    YEAR(Data) = 2023 AND MONTH(Data) = 6
GROUP BY 
    Produto, Categoria
ORDER BY 
    Total_Quantidade_Vendida ASC;

