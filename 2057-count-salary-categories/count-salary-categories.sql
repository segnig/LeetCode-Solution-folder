# Write your MySQL query statement below
Select "Low Salary" as category, count(account_id) accounts_count
from accounts
Where income < 20000

union 

Select "Average Salary" as category, count(account_id) accounts_count
from Accounts
Where income >= 20000 and income <= 50000

union 

Select "High Salary" as category, count(account_id) acounts_count
from Accounts
where income > 50000;
