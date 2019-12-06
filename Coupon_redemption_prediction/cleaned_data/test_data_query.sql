select tr.id, a.percent_redeemed_on_coupin_id, 
b.percent_redeemed_on_customer_id, c.avg_transaction, c.frequency_of_visit, c.age_on_service, 
d.age_range, d.is_married, d.rented, d.family_size, d.income_bracket_categorized, '123' as 'redemption_status'

from 

(select id, campaign_id, coupon_id, customer_id from test) as tr left join 

(SELECT coupon_id, SUM(redemption_status)/COUNT(*)*1000 as 'percent_redeemed_on_coupin_id'
FROM local_host.train GROUP BY coupon_id) as a on tr.coupon_id = a.coupon_id left join

(SELECT customer_id, (SUM(redemption_status)/COUNT(*)*1000) as 'percent_redeemed_on_customer_id'
FROM local_host.train GROUP BY customer_id) as b on tr.customer_id=b.customer_id left join 

(SELECT customer_id, SUM(quantity * selling_price)/COUNT(*) AS 'avg_transaction', count(*) as 'frequency_of_visit',
DATEDIFF(MAX(date), MIN(date)) as 'age_on_service' 
FROM local_host.customer_transaction_data2 GROUP BY customer_id) as c on tr.customer_id=c.customer_id left join 

(select customer_id, age_range, case when marital_status = 'single' then 0 else 1 end as 'is_married', rented, family_size, 
no_of_children, case when income_bracket = 1 then 'one' 
when income_bracket = 2 then 'two' 
when income_bracket = 3 then 'three'
when income_bracket = 4 then 'four'
when income_bracket = 5 then 'five'
when income_bracket = 6 then 'six'
when income_bracket = 7 then 'seven'
when income_bracket = 8 then 'eight'
when income_bracket = 9 then 'nine'
when income_bracket = 10 then 'ten'
when income_bracket = 11 then 'eleven'
when income_bracket = 12 then 'twelve' 
else 'income_bracket_unknown' end as 'income_bracket_categorized' from customer_demographics) as d on tr.customer_id=d.customer_id;
