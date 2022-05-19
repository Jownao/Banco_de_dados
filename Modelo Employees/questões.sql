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
