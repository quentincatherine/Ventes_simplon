-- Chiffres d'affaire total
SELECT SUM(c3*c4) FROM ventes;


-- Ventes par produits
SELECT c2, COUNT (*) FROM ventes
WHERE c2 != 'produit'
GROUP BY c2;

-- Ventes par region 
SELECT SUM(c3*c4) FROM ventes
WHERE c5 != 'region'
GROUP BY c5 ;