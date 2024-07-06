# Write your MySQL query statement below
select name,unique_id from employees left join EmployeeUNI on employees.id=EmployeeUNI.id
