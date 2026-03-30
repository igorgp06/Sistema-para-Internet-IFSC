Exibir todos os registros da tabela filmes.

~~~sql
SELECT * FROM filmes;
~~~

Exibir apenas o título e o ano de lançamento de todos os filmes.

~~~sql
SELECT titulo, ano_lancamento FROM filmes;
~~~

Exibir os filmes lançados após 2010.

~~~sql
SELECT *
FROM filmes
WHERE NULLIF(ano_lancamento, '') IS NOT NULL
	AND CAST(ano_lancamento AS UNSIGNED) > 2010;
~~~

Exibir os filmes lançados entre 2005 e 2010.

~~~sql
SELECT *
FROM filmes
WHERE NULLIF(ano_lancamento, '') IS NOT NULL
	AND CAST(ano_lancamento AS UNSIGNED) BETWEEN 2005 AND 2010;
~~~

Exibir os filmes com duração entre 60 e 80 minutos.

~~~sql
SELECT * FROM filmes WHERE duracao BETWEEN 60 AND 80;
~~~

Exibir os filmes ordenados por ano de lançamento do mais antigo para o mais novo.

~~~sql
SELECT *
FROM filmes
WHERE NULLIF(ano_lancamento, '') IS NOT NULL
ORDER BY CAST(ano_lancamento AS UNSIGNED) ASC;
~~~

Exibir os filmes cujo título contenha a palavra "amor".

~~~sql
SELECT * FROM filmes WHERE titulo LIKE '%amor%';
~~~

Exibir os filmes cujo título contenha a palavra "rei" em qualquer posição.

~~~sql
SELECT * FROM filmes WHERE titulo LIKE '%rei%';
~~~

Exibir os filmes em que o título seja igual ao título original.

~~~sql
SELECT * FROM filmes WHERE titulo = titulo_original;
~~~

Exibir a duração do filme mais longo.

~~~sql
SELECT MAX(duracao) AS duracao_mais_longa FROM filmes;
~~~

Exibir os 3 filmes com maior duração.

~~~sql
SELECT * FROM filmes ORDER BY duracao DESC LIMIT 3;
~~~

Exibir o 3º, 4º e 5º filmes com maior duração.

~~~sql
SELECT * FROM filmes ORDER BY duracao DESC LIMIT 3 OFFSET 2;
~~~

Exibir os filmes que possuem ano de lançamento preenchido.

~~~sql
SELECT *
FROM filmes
WHERE NULLIF(ano_lancamento, '') IS NOT NULL;
~~~
 
Exibir os filmes que possuem duração preenchida, ordenando da menor para a maior duração.

~~~sql
SELECT *
FROM filmes
WHERE duracao IS NOT NULL
ORDER BY duracao ASC;
~~~

Exibir os filmes cuja duração seja maior que a média de duração de todos os filmes.
~~~sql
SELECT * FROM filmes WHERE duracao > (SELECT AVG(duracao) FROM filmes);
~~~

Exibir os filmes com duração entre 90 e 120 minutos, ordenado do maior para o menor.

~~~sql
SELECT * FROM filmes WHERE duracao BETWEEN 90 AND 120 ORDER BY duracao DESC;
~~~

Exibir os 10 filmes mais recentes que possuem duração informada.

~~~sql
SELECT *
FROM filmes
WHERE duracao IS NOT NULL
	AND NULLIF(ano_lancamento, '') IS NOT NULL
ORDER BY CAST(ano_lancamento AS UNSIGNED) DESC, duracao DESC
LIMIT 10;
~~~

Exibir o título do filme, o nome do ator e a duração apenas para atores cujo
nome contenha "John" em qualquer posição, quando a duração não for nula, 
ordenando da menor duração para a maior

~~~sql
SELECT f.titulo, a.nome_ator, f.duracao
FROM filmes f
JOIN elenco e ON e.cod_filme = f.cod_filme
JOIN atores a ON a.cod_ator = e.cod_ator
WHERE a.nome_ator LIKE '%John%'
	AND f.duracao IS NOT NULL
ORDER BY f.duracao ASC;
~~~

Exibir, sem repetição, o nome dos atores que participaram de filmes cujo título contém "Harry Potter"

~~~sql
SELECT DISTINCT a.nome_ator
FROM atores a
JOIN elenco e ON e.cod_ator = a.cod_ator
JOIN filmes f ON f.cod_filme = e.cod_filme
WHERE f.titulo LIKE '%Harry Potter%';
~~~

Exibir, sem repetição, o nome dos atores que participaram de filmes cujo
título contenha a palavra "Amor" e cujo título original contenha a palavra
"Love".

~~~sql
SELECT DISTINCT a.nome_ator
FROM atores a
JOIN elenco e ON e.cod_ator = a.cod_ator
JOIN filmes f ON f.cod_filme = e.cod_filme
WHERE f.titulo LIKE '%Amor%' AND f.titulo_original LIKE '%Love%';
~~~
