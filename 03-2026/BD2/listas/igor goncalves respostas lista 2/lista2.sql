-- Exibir o título do filme e o nome do respectivo diretor.
SELECT f.titulo,
    d.nome_diretor
FROM filmes f
    INNER JOIN diretores d ON d.cod_diretor = f.cod_diretor;


-- Exibir o título do filme e o nome do respectivo gênero.
SELECT f.titulo,
    g.nome_genero
FROM filmes f
    INNER JOIN generos g ON g.cod_genero = f.cod_genero;


-- Exibir o título do filme, o nome do diretor e o nome do gênero.
SELECT f.titulo,
    d.nome_diretor,
    g.nome_genero
FROM filmes f
    INNER JOIN diretores d ON d.cod_diretor = f.cod_diretor
    INNER JOIN generos g ON g.cod_genero = f.cod_genero;


-- Exibir o título do filme e o nome dos respectivos atores.
SELECT f.titulo,
    a.nome_ator
FROM filmes f
    INNER JOIN elenco e ON e.cod_filme = f.cod_filme
    INNER JOIN atores a ON a.cod_ator = e.cod_ator;


-- Exibir o título do filme, o nome do ator e o nome do diretor.
SELECT f.titulo,
    a.nome_ator,
    d.nome_diretor
FROM filmes f
    INNER JOIN elenco e ON e.cod_filme = f.cod_filme
    INNER JOIN atores a ON a.cod_ator = e.cod_ator
    INNER JOIN diretores d ON d.cod_diretor = f.cod_diretor;


-- Exibir o título do filme, o nome do diretor e o ano de lançamento apenas dos filmes lançados após 2010.
SELECT f.titulo,
    d.nome_diretor,
    f.ano_lancamento
FROM filmes f
    INNER JOIN diretores d ON d.cod_diretor = f.cod_diretor
WHERE CAST(NULLIF(f.ano_lancamento, '') AS UNSIGNED) > 2010;


-- Exibir o título do filme, o nome do gênero e a duração apenas dos filmes com duração maior que 120 minutos.
SELECT f.titulo,
    g.nome_genero,
    f.duracao
FROM filmes f
    INNER JOIN generos g ON g.cod_genero = f.cod_genero
WHERE f.duracao > 120;


-- Exibir o título do filme e o nome do ator apenas dos filmes cujo títul  contenha a palavra "amor".
SELECT f.titulo,
    a.nome_ator
FROM filmes f
    INNER JOIN elenco e ON e.cod_filme = f.cod_filme
    INNER JOIN atores a ON a.cod_ator = e.cod_ator
WHERE f.titulo LIKE '%amor%';


-- Exibir o título do filme, o nome do ator e a duração apenas para atores cujo nome contenha "John" em qualquer posição, quando a duração não for nula, ordenando da menor duração para a maior.
SELECT f.titulo,
    a.nome_ator,
    f.duracao
FROM filmes f
    INNER JOIN elenco e ON e.cod_filme = f.cod_filme
    INNER JOIN atores a ON a.cod_ator = e.cod_ator
WHERE a.nome_ator LIKE '%John%'
    AND f.duracao IS NOT NULL
ORDER BY f.duracao ASC;


-- Exibir, sem repetição, o nome dos atores que participaram de filmes cujo título contenha "Harry Potter".
SELECT DISTINCT a.nome_ator
FROM atores a
    INNER JOIN elenco e ON e.cod_ator = a.cod_ator
    INNER JOIN filmes f ON f.cod_filme = e.cod_filme
WHERE f.titulo LIKE '%Harry Potter%';


-- Exibir, sem repetição, o nome dos diretores que dirigiram filmes do gênero "Comédia".
SELECT DISTINCT d.nome_diretor
FROM diretores d
    INNER JOIN filmes f ON f.cod_diretor = d.cod_diretor
    INNER JOIN generos g ON g.cod_genero = f.cod_genero
WHERE g.nome_genero = 'Com?dia';


-- Exibir todos os filmes e seus respectivos diretores, incluindo também os filmes que não possuem diretor.
SELECT f.titulo,
    d.nome_diretor
FROM filmes f
    LEFT JOIN diretores d ON d.cod_diretor = f.cod_diretor;


-- Exibir todos os diretores e seus respectivos filmes, incluindo também os diretores que não possuem filme.
SELECT d.nome_diretor,
    f.titulo
FROM diretores d
    LEFT JOIN filmes f ON f.cod_diretor = d.cod_diretor;


-- Exibir todos os filmes e seus respectivos gêneros, incluindo também os casos em que não exista associação.
SELECT f.titulo,
    g.nome_genero
FROM filmes f
    LEFT JOIN generos g ON g.cod_genero = f.cod_genero;


-- Exibir todos os gêneros e seus respectivos filmes, incluindo também os gêneros que não possuem filmes.
SELECT g.nome_genero,
    f.titulo
FROM generos g
    LEFT JOIN filmes f ON f.cod_genero = g.cod_genero;


-- Exibir a lista de filmes que não possuem nenhum diretor cadastrado.
SELECT f.titulo
FROM filmes f
    LEFT JOIN diretores d ON d.cod_diretor = f.cod_diretor
WHERE d.cod_diretor IS NULL;


-- Exibir a lista de diretores que não possuem nenhum filme.
SELECT d.nome_diretor
FROM diretores d
    LEFT JOIN filmes f ON f.cod_diretor = d.cod_diretor
WHERE f.cod_filme IS NULL;


-- Exibir a lista de filmes que não possuem nenhum ator no elenco.
SELECT f.titulo
FROM filmes f
    LEFT JOIN elenco e ON e.cod_filme = f.cod_filme
WHERE e.cod_filme IS NULL;


-- Exibir a lista de atores que nunca atuaram em filmes.
SELECT a.nome_ator
FROM atores a
    LEFT JOIN elenco e ON e.cod_ator = a.cod_ator
WHERE e.cod_ator IS NULL;


-- Exibir os nomes dos gêneros que não possuem nenhum filme cadastrado.
SELECT g.nome_genero
FROM generos g
    LEFT JOIN filmes f ON f.cod_genero = g.cod_genero
WHERE f.cod_filme IS NULL;