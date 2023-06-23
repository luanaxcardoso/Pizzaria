create database pizzaria;
use pizzaria; 

CREATE TABLE tb_usuarios(
  id_usuarios int not null auto_increment,
  funcao varchar(100),
  login_usuario varchar(100),
  senha_usuario varchar(100),
  PRIMARY KEY (id_usuarios)
);

create table tb_pizza(
    id_pizza int not null auto_increment,
    sabor varchar (100) not null,
    preco float not null,
    primary key(id_pizza)
);

create table tb_bebidas(
    id_bebidas int not null auto_increment,
    nome varchar(100) not null,
    preco float not null,
    primary key(id_bebidas)
);

create table tb_vendas(
    id_vendas int not null auto_increment,
    id_bebidas int,
    id_pizza int,
    nomeCliente varchar(100) not null,
    totalPagar float not null,
    datavenda datetime,    
    primary key(id_vendas),
    foreign key (id_bebidas) references tb_bebidas(id_bebidas),
    foreign key (id_pizza) references tb_pizza(id_pizza)
);

insert into tb_usuarios (funcao, login_usuario,senha_usuario)
values ("atendente","JoaoRicardo","joao2030"); 

insert into tb_usuarios (funcao, login_usuario,senha_usuario)
values ("gerente","PaulaAlves","paula1415"); 

insert into tb_usuarios (funcao, login_usuario,senha_usuario)
values ("administrativo","FatimaPereira","fatima1518");
 

insert into tb_pizza(sabor,preco)
values ("mussarela","30"); 

insert into tb_pizza(sabor,preco)
values ("marguerita","40"); 

insert into tb_pizza(sabor,preco)
values ("calabresa","35"); 

insert into tb_pizza(sabor,preco)
values ("portuguesa","40"); 

insert into tb_pizza(sabor,preco)
values ("frango com catupiry","60");
 
insert into tb_bebidas(nome,preco)
values ("coca cola","10"); 

insert into tb_bebidas(nome,preco)
values ("fanta uva","12"); 

insert into tb_bebidas(nome,preco)
values ("fanta laranja","14"); 

insert into tb_bebidas(nome,preco)
values ("sprite", "12");

select * from tb_usuarios;
select * from tb_pizza;
select * from tb_bebidas;
select * from tb_vendas;