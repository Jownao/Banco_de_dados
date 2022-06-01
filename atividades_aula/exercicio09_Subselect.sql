-- Exercicio 09 - Subselects


-- Cláusura where - listar os alunos com maior MGP para cada curso
select nom_alu, nom_curso, mgp
from alunos join cursos using (cod_curso)
where (cod_curso,mgp) in (select cod_curso , max(mgp) 
                            from alunos join cursos using (cod_curso)
                            group by cod_curso)

--Cláusura where - listar os alunos que possuem MGP maior que média geral do seu curso ordenar por curso e depois nome do aluno
select nom_alu, nom_curso, mgp
from alunos join cursos using (cod_curso)
where (mgp) >   (select avg(mgp)
                    from alunos)
order by 2,1 asc

--Cláusura where - listar o nome do aluno e o nome do curso para os alunos com maior e menor quantidade de créditos cursados por curso
select  a.nom_alu, c.nom_curso, a.tot_cred
from alunos a join cursos c using(cod_curso)
where (cod_curso,a.tot_cred) in (select cod_curso,min(tot_cred)
                                from alunos 
                                where tot_cred > 0
                                group by cod_curso)
or (cod_curso,a.tot_cred) in (select cod_curso,max(tot_cred)
                                from alunos 
                                group by cod_curso)

--Cláusura from - listar o nome do aluno e o nome da disciplina dos alunos que já perderam a mesma disciplina mais de uma vez
select nom_disc, nom_alu 
from (select *
      from alunos a join historicos h using(mat_alu) 
      where h.situacao in ('RM','RF')) d 
      join disciplinas d using (cod_disc)
group by nom_disc, nom_alu
having count(nom_disc) > 1

--Cláusura from - além de seguir os critérios do item 4, liste somente os casos em que a média do aluno foi inferior a 4,0 na disciplina e o número de faltas superior a 18
select nom_disc, nom_alu
from (select * 
      from alunos a join historicos h using(mat_alu)
      where h.situacao in ('RM','RF')) d
      join disciplinas d using (cod_disc)
where mgp < 4.0 or faltas > 18
group by nom_disc, nom_alu
having count(nom_disc) > 1

--Cláusura from - listar os 5 alunos com maior média na disciplina 282
select nom_alu 
  from (select nom_alu
         from alunos join historicos using(mat_alu)
         where cod_disc = 282
         order by media desc) 
where rownum <= 5
