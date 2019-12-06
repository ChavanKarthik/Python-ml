SELECT 
    e.item_id,
    e.no_of_times_redeemed_item,
    d.coupon_id,
    d.no_of_times_redeemed,
    d.no_of_times_given,
    d.brand,
    d.brand_type,
    d.category
FROM
    (SELECT 
        c.item_id, COUNT(*) AS 'no_of_times_redeemed_item'
    FROM
        (SELECT 
        coupon_id,
            SUM(redemption_status) AS 'no_of_times_redeemed_coupon',
            COUNT(*) AS 'no_of_times_given'
    FROM
        train
    GROUP BY coupon_id
    HAVING no_of_times_redeemed_coupon > 0) AS a
    JOIN coupon_item_mapping b ON a.coupon_id = b.coupon_id
    JOIN item_data c ON b.item_id = c.item_id
    GROUP BY c.item_id) AS e
        JOIN
    (SELECT 
        a.coupon_id,
            a.no_of_times_redeemed,
            a.no_of_times_given,
            c.item_id,
            c.brand,
            c.brand_type,
            c.category
    FROM
        (SELECT 
        coupon_id,
            SUM(redemption_status) AS 'no_of_times_redeemed',
            COUNT(*) AS 'no_of_times_given'
    FROM
        train
    GROUP BY coupon_id
    HAVING no_of_times_redeemed > 0) AS a
    JOIN coupon_item_mapping b ON a.coupon_id = b.coupon_id
    JOIN item_data c ON b.item_id = c.item_id) AS d ON d.item_id = e.item_id;

