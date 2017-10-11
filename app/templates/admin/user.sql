/*user*/
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Mouse','1231','1231@123.com','13888888881','Mouse','head1.png','d32a72bdac524478b7e4f6dfc8394fc0',now());
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Bull','1232','1232@123.com','13888888882','Bull','head2.png','d32a72bdac524478b7e4f6dfc8394fc1',now());
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Tiger','1233','1233@123.com','13888888883','Tiger','head3.png','d32a72bdac524478b7e4f6dfc8394fc2',now());
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Rabbit','1234','1234@123.com','13888888884','Rabbit','head4.png','d32a72bdac524478b7e4f6dfc8394fc3',now());
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Dragon','1235','1235@123.com','13888888885','Dragon','head5.png','d32a72bdac524478b7e4f6dfc8394fc4',now());
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Snake','1236','1236@123.com','13888888886','Snake','head6.png','d32a72bdac524478b7e4f6dfc8394fc5',now());
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Horse','1237','1237@123.com','13888888887','Horse','head7.png','d32a72bdac524478b7e4f6dfc8394fc6',now());
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Sheep','1238','1238@123.com','13888888888','Sheep','head8.png','d32a72bdac524478b7e4f6dfc8394fc7',now());
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Monkey','1239','1239@123.com','13888888889','Monkey','head9.png','d32a72bdac524478b7e4f6dfc8394fc8',now());
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Chicken','1240','1240@123.com','13888888891','Chicken','head10.png','d32a72bdac524478b7e4f6dfc8394fc9',now());
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Dog','1241','1241@123.com','13888888892','Dog','head11.png','d32a72bdac524478b7e4f6dfc8394fd0',now());
insert into user(name,pwd,email,phone,info,face,uuid,addtime) values('Pig','1242','1242@123.com','13888888893','Pig','head12.png','d32a72bdac524478b7e4f6dfc8394fd1',now());


ALTER TABLE user auto_increment=1;
/*comment*/
insert into comment(movie_id,user_id,content,addtime) values(3,25,"Good!",now());
insert into comment(movie_id,user_id,content,addtime) values(3,26,"Very nice!",now());
insert into comment(movie_id,user_id,content,addtime) values(3,27,"What a classic movie!",now());
insert into comment(movie_id,user_id,content,addtime) values(3,28,"HHAHAHAHA",now());
insert into comment(movie_id,user_id,content,addtime) values(4,29,"This is just some bullshit man",now());
insert into comment(movie_id,user_id,content,addtime) values(4,30,"Boring, the director of this movie sucks",now());
insert into comment(movie_id,user_id,content,addtime) values(4,31,"This movie makes me sleepy...",now());
insert into comment(movie_id,user_id,content,addtime) values(4,32,"I have know idea what this movie is talking about...",now());

/*collection*/
insert into moviecol(movie_id,user_id,addtime) values(3,28,now());
insert into moviecol(movie_id,user_id,addtime) values(3,29,now());
insert into moviecol(movie_id,user_id,addtime) values(3,31,now());
insert into moviecol(movie_id,user_id,addtime) values(3,32,now());
insert into moviecol(movie_id,user_id,addtime) values(4,33,now());
insert into moviecol(movie_id,user_id,addtime) values(4,34,now());
insert into moviecol(movie_id,user_id,addtime) values(4,35,now());
insert into moviecol(movie_id,user_id,addtime) values(4,25,now());

ALTER TABLE moviecol auto_increment=1;

/*User login operation log*/
insert into userlog(user_id, ip, addtime) values(25, "192.168.4.1", now());
insert into userlog(user_id, ip, addtime) values(26, "192.168.4.2", now());
insert into userlog(user_id, ip, addtime) values(27, "192.168.4.3", now());
insert into userlog(user_id, ip, addtime) values(28, "192.168.4.4", now());
insert into userlog(user_id, ip, addtime) values(29, "192.168.4.5", now());
insert into userlog(user_id, ip, addtime) values(30, "192.168.4.6", now());
insert into userlog(user_id, ip, addtime) values(31, "192.168.4.7", now());
insert into userlog(user_id, ip, addtime) values(32, "192.168.4.8", now());
insert into userlog(user_id, ip, addtime) values(33, "192.168.4.9", now());

