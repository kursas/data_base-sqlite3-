# --1.Sukurkite duomenų bazę pagal tokią diagramą:
# -- CREATE TABLE `customer` (
# --   `id` integer PRIMARY KEY,
# --   `f_name` string,
# --   `l_name` string,
# --   `email` string
# -- );
#
# -- CREATE TABLE `status` (
# --   `id` integer PRIMARY KEY,
# --   `name` string
# -- );
#
# -- CREATE TABLE `product` (
# --   `id` integer PRIMARY KEY,
# --   `name` string,
# --   `price` float
# -- );
# -- CREATE TABLE `order_` (
# --   `id` integer PRIMARY KEY,
# --   `customer_id` integer,
# --   `date_` string,
# --   `status_id` integer,
# --    FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
# --    FOREIGN KEY (`status_id`) REFERENCES `status` (`id`)
# -- );
# -- CREATE TABLE `product_order` (
# --   `order_id` integer PRIMARY KEY,
# --   `product_id` integer,
# --   `quantity` integer,
# --    FOREIGN KEY (`order_id`) REFERENCES `order_` (`id`),
# --    FOREIGN KEY (`product_id`) REFERENCES `product` (`id`)
# -- );
# --Užpildykite duomenimis - bent 3 klientai, bent 5 užsakymai, kiekviename jų po 1-3 pozicijas,
# --keletas produktų, keletas užsakymo statusų (pvz, patvirtintas, vykdomas, įvykdytas, atmestas).
# --INSERT INTO "main"."customer" ("id", "f_name", "l_name", "email") VALUES ('1', 'Jonas', 'Jonaitis', 'jj@epastas.lt');
# --INSERT INTO "main"."customer" ("id", "f_name", "l_name", "email") VALUES ('2', 'Petras', 'Petraitis', 'pp@gmail.com');
# --INSERT INTO "main"."customer" ("id", "f_name", "l_name", "email") VALUES ('3', 'Antanas', 'Antanaitis', 'aa@mail.com');
#
# --INSERT INTO "main"."product" ("id", "name", "price") VALUES ('1', 'smelis', '15.0');
# --INSERT INTO "main"."product" ("id", "name", "price") VALUES ('2', 'zvyras', '20.0');
# --INSERT INTO "main"."product" ("id", "name", "price") VALUES ('3', 'juodzemis','40.0');
# --INSERT INTO "main"."product" ("id", "name", "price") VALUES ('4', 'trasos', '80.0');
#
# --INSERT INTO "main"."status" ("id", "Name") VALUES ('1', 'patvirtinta');
# --INSERT INTO "main"."status" ("id", "Name") VALUES ('2', 'pristatoma');
# --INSERT INTO "main"."status" ("id", "Name") VALUES ('3', 'atlikta');
#
# --INSERT INTO "main"."order_" ("id", "date_", "customer_id", "status_id") VALUES ('1', '2021-01-20 12:00:00', '1', '1');
# --INSERT INTO "main"."order_" ("id", "date_", "customer_id", "status_id") VALUES ('2', '2020-06-22 14:00:00', '1', '2');
# --INSERT INTO "main"."order_" ("id", "date_", "customer_id", "status_id") VALUES ('3', '2022-12-20 18:00:00', '1', '1');
# --INSERT INTO "main"."order_" ("id", "date_", "customer_id", "status_id") VALUES ('4', '2019-08-28 15:00:00', '1', '2');
#
#
# --INSERT INTO "main"."product_order" ("order_id", "product_id", "quantity") VALUES ('2', '1', '3');
# --INSERT INTO "main"."product_order" ("order_id", "product_id", "quantity") VALUES ('3', '2', '4');
# --INSERT INTO "main"."product_order" ("order_id", "product_id", "quantity") VALUES ('4', '3', '8');
#
# --1uzklausa:kad rezultate matytųsi užsakymo id, užsakovo pavardė, data, bendra užsakymo suma:
# -- SELECT 	order_.id as "order id",
# -- 		order_.date_ as "date",
# -- 		customer.l_name as "customer",
# --         sum(product_order.quantity * product.price) as "price"
# -- FROM product_order
# -- JOIN order_ on order_.id = product_order.order_id
# -- JOIN product on product.id = product_order.product_id
# -- JOIN customer on customer.id = order_.customer_id
# -- GROUP by order_id
#
# --2uzklausa:kad rezultate matytųsi užsakymo id, pozicijos su kiekiais, kainomis ir bendra pozicijos suma:
# -- SELECT
# -- 	order_.id,
# -- 	product.name,
# -- 	product_order.quantity,
# -- 	product.price,
# -- 	product_order.quantity * product.price as "total"
# -- FROM order_
# -- JOIN product_order ON order_.id = product_order.order_id
# -- JOIN product ON product.id = product_order.product_id
#
# --3uzklausa:prieš tai buvusios užklausos pagrindu sukurkite užklausą, kurioje matytųsi, kiek ir kokio produkto buvo užsakyta:
# -- SELECT
# -- 	order_.id,
# -- 	product.name,
# -- 	sum(product_order.quantity) as "quantity",
# -- 	product.price,
# -- 	sum(product_order.quantity) * product.price as "total"
# -- FROM order_
# -- JOIN product_order ON order_.id = product_order.order_id
# -- JOIN product ON product.id = product_order.product_id
# -- group by product_order.product_id
#
