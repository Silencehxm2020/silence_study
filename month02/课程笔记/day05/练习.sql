作业： 1. 创建一个数据库 books 使用utf8编码
      2. 在books中创建数据表 book   字段的类型和约束条件自己拟定

          id  书名  作者  出版社  价格  备注

      3. 向book插入若干数据

         作者： 老舍  鲁迅  。。。
         价格： 30 -- 120
         出版社 ： 中国文学  机械工业   中国教育 。。。。

      4. mysql语句和数据类型

create database books character set utf8;

create table book(id int primary key auto_increment,
book_name varchar(50),
author varchar(20),
publication varchar(100),
price decimal(5,2),
remark text
);
-- 练习2: 使用book表完成
-- 1. 将呐喊的价格改为45
update book set price = 45 where title='呐喊';

-- 2. 增加一个字段,出版日期,类型为date,放在price的后面
alter table book add publication_time date after price;
alter table book add publication_time date after price;

-- 3. 修改所有老舍的作品,出版日期为2016-10-1
update book set publication_time="2016-10-1" where author="老舍";
update book set publication_time="2016-10-1" where author ="老舍";
-- 4. 修改所有中国文学出版社的图书,出版日期为2018-1-1,但是老舍的不要改
update book set publication_time="2018-1-1"
where publication="中国文学出版社" and  author != '老舍';
update book set publication_time="2018-1-1" where publication="中国文学出版社" and author !="老舍";

-- 5. 修改价格字段数据类型为 decimal(5,2)
alter table book modify price decimal(5,2);
alter table book modify price decimal(4,2);

-- 6. 查找鲁迅写的,2017-1-1以后出版的图书
select * from book where author="鲁迅" and publication_time > "2017-01-01";
select * from book where author="鲁迅" and publication_time >"2017-01-01";
-- 7. 删除所有价格在65元以上的图书
delete from book where price > 65;

练习3:
stu数据库下创建一个表 sanguo

id  name   gender  country   attack(攻击力)   defense(防御力)



insert into sanguo
values (1, '曹操', '男', '魏', 256, 63),
       (2, '张辽', '男', '魏', 328, 69),
       (3, '甄姬', '女', '魏', 168, 34),
       (4, '夏侯渊', '男', '魏', 366, 83),
       (5, '刘备', '男', '蜀', 220, 59),
       (6, '诸葛亮', '男', '蜀', 170, 54),
       (7, '赵云', '男', '蜀', 377, 66),
       (8, '张飞', '男', '蜀', 370, 80),
       (9, '孙尚香', '女', '蜀', 249, 62),
       (10, '大乔', '女', '吴', 190, 44),
       (11, '小乔', '女', '吴', 188, 39),
       (12, '周瑜', '男', '吴', 303, 60),
       (13, '吕蒙', '男', '吴', 330, 71);
create table sanguo (id int primary key auto_increment,name varchar(20),
gender char,country char,attack int,defense int);

1. 查找所有蜀国人的信息,按照攻击力排名
select * from sanguo where country="蜀" order by attack;
2. 将赵云攻击力设置为360,防御力设置为70
update sanguo set attack=360,defense=70 where name ="赵云";
3. 吴国英雄攻击力超过300的改为300 ,最多改两个
update sanguo set attack=300 where country="吴" and attack > 300 limit 2;
4. 查找攻击力超过200的魏国英雄的名字,和攻击力 并且显示为 姓名  攻击力
select attack as "攻击力",name as "姓名" from sanguo where country="魏" and attack >200;
5. 所有英雄攻击力按照降序排序,如果攻击力相同则按照防御力降序排序
select * from sanguo order by attack,defense;
6. 查找名字为3个字的英雄
select * from sanguo where name like "___";
7. 找到比魏国攻击力最高的英雄的攻击力还要高的蜀国英雄
select * from sanguo where country="蜀国" and attack > (select attack from sanguo where
country="魏国" order by attack desc limit 1);
8. 找到魏国防御排名前2的英雄
select * from sanguo where country="魏" order by defense desc limit 2;
9. 查找所有女性角色,同时查找所有男性角色英雄中攻击力少于250的
select * from sanguo where gender="女" union select * from sanguo where gender ="男" and attack>250;