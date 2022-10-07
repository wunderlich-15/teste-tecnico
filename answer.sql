-- 1. Escreva uma query que retorne o nome de cada curso com a somatória de todas as
--compras associadas;
select compras.id_course, cursos.name, sum(compras.mensalidade) from compras inner join cursos where compras.id_course = cursos.id group by cursos.id

-- 2. Escreva uma query que retorne todas as compras que tiveram um valor acima de 110
-- reais;
select * from compras where mensalidade > 110

-- 3. Escreva uma query que retorne todas as informações dos cursos que não aparecem na
-- tabela compras
select * from cursos where cursos.id not in (select id_course from compras)