select * from(
select product_id,"store1" as "store",store1 price from products
union
select product_id,"store2" as "store",store2 price from products
union
select product_id,"store3" as "store",store3 price from products) t where price is not null