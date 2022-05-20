-----------------------------------------------------------------------------------------
-- MODELO HR
-----------------------------------------------------------------------------------------

-- Select - From - Where

-- a) Exibir informações dos trabalhos onde o salário mínimo é superior a 10000
select job_title as Trabalho, min_salary as SalarioMin, max_salary as SalarioMax
from jobs 
where min_salary > 10000
-- Outro modo porém os salarios superiores não aparecem
select dp.department_name, jb.job_title, jb.min_salary, lc.city
from job_history jh join jobs jb using (job_id)
                    join departments dp using (department_id) , locations lc
where dp.location_id = lc.location_id and min_salary > 5000
-- b) Mostre o nome e a data de admissão dos empregados que foram admitidos entre 2002 e 2005. 
select first_name, last_name, to_char(hire_date,'yyyy') Contratacao
from employees
where hire_date between '01/01/2002' and '01/01/2005' 

select to_char(hire_date,'yyyy') Contratacao from employees

-- c) Exibir o primeiro nome e a data de admissão dos empregados que são programadores de TI ou Sales Manager.
select e.first_name, j.start_date
from employees e join job_history j using (employee_id)
where j.job_id = 'IT_PROG' or j.job_id = 'SA_MAN'

-- d) Exibir funcionários que foram admitidos após 1º de janeiro de 2008. 
select first_name, hire_date
from employees
where hire_date > '01/01/2008'

-- e) Exibir detalhes do empregado com identificação 150 ou 160
select first_name, employee_id
from employees
where employee_id = 150 or employee_id = 160

select employee_id from employees

-- f) Mostrar o nome, o salário, a comissão e a data de contratação para funcionários com salário inferior a 10000.
select first_name, salary, commission_pct, hire_date
from employees
where salary < 10000

-- g) Indicar título do trabalho, a diferença entre salários máximos e mínimos para empregos com salário máximo na faixa de 10000 a 20000
select job_title, (max_salary - min_salary) Diferenca
from jobs
where max_salary >= 10000 and max_salary <= 20000

-- h) Exibir empregados onde o primeiro nome ou sobrenome começa com S.
select employee_id, first_name, last_name
from employees
where first_name like 'S%' or last_name like 'S%' 

-- i) Exibir empregados que foram admitidos no mês de maio
select employee_id, first_name,hire_date
from employees
where to_char(hire_date,'mm') = '05'

select to_char(hire_date) Contratacao from employees

-- j) Exibir detalhes dos empregados onde a porcentagem de comissão é nula, o salário está no intervalo de 5000 a 10000 e o departamento é 30.
select first_name, employee_id, commission_pct, salary
from employees join departments using (department_id)
where commission_pct is null and department_id = 30 and salary >= 5000 and salary <= 10000

-- k) Exibir nome e o tempo de experiência dos funcionários em anos.
select first_name,last_name, TRUNC((MONTHS_BETWEEN (TO_DATE (end_date, 'dd/mm/yy'), TO_DATE (start_date, 'dd/mm/yy'))/12),1) "Anos"
from job_history join employees using (employee_id)

-- l) Mostrar o primeiro nome dos funcionários que foram admitidos em 2001.
select first_name, to_char(hire_date,'yyyy') Contratacao
from employees
where hire_date like '%01%'

-- m) Exibir o comprimento do primeiro nome para os funcionários onde o sobrenome contém o caractere 'b' após a terceira posição.
select first_name,last_name as Teste, length(first_name)
from employees
where last_name like '___b%'  

-- n) Exibir o primeiro nome em maiúsculas e o endereço de e-mail em minúsculas para os funcionários, onde o primeiro nome é igual ao e-mail.
select upper(first_name), lower(email)
from employees
where first_name = email

-- o) Exibir funcionários que admitidos no ano atual.
select first_name, hire_date
from employees
where hire_date = sysdate

-- p) Selecione todos os ids, nomes e sobrenomes de empregados, que estejam nas faixas de salários de 0 a 2000 e maiores ou iguais a 5000. 
select employee_id, first_name, last_name
from employees
where salary <= 2000 or salary >= 5000

-- Group By

-- a) Exibir quantos funcionários foram admitidos em cada mês do ano atual.
select count(e.employee_id), e.hire_date
from employees e join job_history j using(job_id)
where hire_date like '%22%'
group by e.hire_date

-- b) Exibir ID do gerente e número de funcionários gerenciados por ele.
select d.manager_id as Gerente, count(e.employee_id) Funcionarios
from employees e join departments d using(department_id)
group by d.manager_id

-- c) Exibir ID do funcionário e a data em que ele terminou seu trabalho anterior.
select employee_id , end_date
from employees e join job_history j using(employee_id)

-- d) Mostre o ID do país e o número de cidades que temos no país.
select c.COUNTRY_ID as Pais, count(l.location_id) as TotalCidades
from countries c join locations l on c.country_id = l.country_id -- using (country_id)
group by c.COUNTRY_ID

-- e) Mostrar o salário médio dos funcionários em cada departamento com porcentagem de comissão.
select TRUNC(AVG(salary),2) as MediaSalario, department_name, commission_pct
from employees e join departments d using (department_id)
group by department_name, commission_pct

-- f) Exibir ID do trabalho, número de funcionários, soma do salário e diferença entre o salário mais alto e o salário mais baixo dos funcionários para cada trabalho.
select j.job_id, count(e.employee_id)as qtd_func, sum(e.salary) as Soma_salario, (max(e.salary)-min(e.salary)) as Diferenca_salario
from employees e join job_history j on j.job_id = e.job_id
group by j.job_id
