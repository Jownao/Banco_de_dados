-- Exercicio 08

-- 1 Questão
select distinct a.nom_alu, a.mat_alu, a.mgp, a.dat_nasc
from alunos a join cursos c on a.cod_curso = c.cod_curso
              join matriculas m on a.mat_alu = m.mat_alu
where a.cod_curso = 26 and ano = 2011 and semestre = 3
order by 3 desc

-- 2 Questão
select a.mat_alu, a.nom_alu, a.mgp, h.faltas
from alunos a join historicos h on a.mat_alu = h.mat_alu
where h.cod_disc = 3817 and h.ano = 2008 and h.semestre = 1

-- 3 Questão

select cod_disc as CoDisciplina, nom_disc as nomeDisc, periodo
from disciplinas join matrizes using (cod_disc)
where cod_curso = 52

 

-- 4 Questão / Formato da data na database está "yy" impossibilitando a subtração de 2011 - yyyy

select TRUNC(AVG(MONTHS_BETWEEN 
        (TO_DATE ('01-01-2011', 'dd/mm/RRRR'), 
         TO_DATE (dat_nasc    , 'dd/mm/RRRR') ) /12),2) "Idade Média"
from alunos join matriculas using (mat_alu)
where cod_disc = 5472

-- 5 Questão

select distinct a.mat_alu, a.nom_alu, c.nom_curso, p.nom_prof
from cursos c join alunos a using (cod_curso)
              join professores p using (idt_prof) , historicos h
where situacao = 'AP' and h.mat_alu = a.mat_alu
order by 3,2



-- 6 Questão

select distinct c.nom_curso, d.nom_disc, TRUNC(AVG(h.media),2)
from matrizes m join cursos c on m.cod_curso = c.cod_curso
                join disciplinas d on m.cod_disc = d.cod_disc, historicos h
where d.cod_disc = h.cod_disc and c.cod_curso = 13 and ano = 2007 and semestre = 3
group by c.nom_curso, d.nom_disc




