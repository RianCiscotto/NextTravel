from flask import Flask, render_template
from pais import Pais

app = Flask(__name__)

p1 = Pais(
    id=1,
    nome="Brasil",
    bandeira="https://flagcdn.com/w320/br.png",
    capital="Brasília",
    descricao="O maior país da América do Sul, conhecido pela floresta amazônica e o futebol.",
    lingua="Português"
)

p2 = Pais(
    id=2,
    nome="Canadá",
    bandeira="https://flagcdn.com/w320/ca.png",
    capital="Ottawa",
    descricao="Um vasto país norte-americano, famoso por suas paisagens naturais e cidades multiculturais.",
    lingua="Inglês, Francês"
)

p3 = Pais(
    id=3,
    nome="Japão",
    bandeira="https://flagcdn.com/w320/jp.png",
    capital="Tóquio",
    descricao="País insular no leste da Ásia, famoso pela tecnologia e cultura milenar.",
    lingua="Japonês"
)

p4 = Pais(
    id=4,
    nome="Estados Unidos",
    bandeira="https://flagcdn.com/w320/us.png",
    capital="Washington, D.C.",
    descricao="Uma grande nação norte-americana, conhecida por sua diversidade cultural e inovações.",
    lingua="Inglês"
)

p5 = Pais(
    id=5,
    nome="Reino Unido",
    bandeira="https://flagcdn.com/w320/gb.png",
    capital="Londres",
    descricao="Um país europeu com uma rica história, monarquia e influência cultural global.",
    lingua="Inglês"
)

p6 = Pais(
    id=6,
    nome="França",
    bandeira="https://flagcdn.com/w320/fr.png",
    capital="Paris",
    descricao="Um país europeu famoso por sua arte, moda, gastronomia e marcos históricos.",
    lingua="Francês"
)

p7 = Pais(
    id=7,
    nome="Alemanha",
    bandeira="https://flagcdn.com/w320/de.png",
    capital="Berlim",
    descricao="Uma potência econômica europeia, conhecida por sua engenharia, cerveja e história.",
    lingua="Alemão"
)

p8 = Pais(
    id=8,
    nome="Itália",
    bandeira="https://flagcdn.com/w320/it.png",
    capital="Roma",
    descricao="Um país europeu com uma rica herança cultural, culinária e arte.",
    lingua="Italiano"
)

p9 = Pais(
    id=9,
    nome="China",
    bandeira="https://flagcdn.com/w320/cn.png",
    capital="Pequim",
    descricao="O país mais populoso do mundo, com uma história milenar e rápido desenvolvimento.",
    lingua="Mandarim"
)

p10 = Pais(
    id=10,
    nome="Índia",
    bandeira="https://flagcdn.com/w320/in.png",
    capital="Nova Deli",
    descricao="Uma nação vasta e diversa, conhecida por sua cultura vibrante, especiarias e tecnologia.",
    lingua="Hindi, Inglês"
)

p11 = Pais(
    id=11,
    nome="Austrália",
    bandeira="https://flagcdn.com/w320/au.png",
    capital="Camberra",
    descricao="Um país-continente conhecido por sua vida selvagem única, praias e paisagens desérticas.",
    lingua="Inglês"
)

p12 = Pais(
    id=12,
    nome="México",
    bandeira="https://flagcdn.com/w320/mx.png",
    capital="Cidade do México",
    descricao="Um país latino-americano com uma rica cultura pré-colombiana e culinária vibrante.",
    lingua="Espanhol"
)

p13 = Pais(
    id=13,
    nome="Argentina",
    bandeira="https://flagcdn.com/w320/ar.png",
    capital="Buenos Aires",
    descricao="O segundo maior país da América do Sul, famoso pelo tango, carne e paisagens diversas.",
    lingua="Espanhol"
)

p14 = Pais(
    id=14,
    nome="África do Sul",
    bandeira="https://flagcdn.com/w320/za.png",
    capital="Pretória (executiva), Cidade do Cabo (legislativa), Bloemfontein (judicial)",
    descricao="Um país no extremo sul da África, conhecido por sua diversidade cultural e vida selvagem.",
    lingua="Africâner, Inglês, Xhosa, Zulu, entre outras"
)

p15 = Pais(
    id=15,
    nome="Egito",
    bandeira="https://flagcdn.com/w320/eg.png",
    capital="Cairo",
    descricao="Uma nação transcontinental com uma história antiga, famosa pelas pirâmides e o rio Nilo.",
    lingua="Árabe"
)

p16 = Pais(
    id=16,
    nome="Rússia",
    bandeira="https://flagcdn.com/w320/ru.png",
    capital="Moscou",
    descricao="O maior país do mundo em área, com uma rica história e vastas paisagens.",
    lingua="Russo"
)

p17 = Pais(
    id=17,
    nome="Coreia do Sul",
    bandeira="https://flagcdn.com/w320/kr.png",
    capital="Seul",
    descricao="Um país asiático conhecido por sua tecnologia, K-Pop e cultura moderna.",
    lingua="Coreano"
)

p18 = Pais(
    id=18,
    nome="Espanha",
    bandeira="https://flagcdn.com/w320/es.png",
    capital="Madri",
    descricao="Um país europeu vibrante, famoso por sua arquitetura, flamenco e festas.",
    lingua="Espanhol"
)

p19 = Pais(
    id=19,
    nome="Suécia",
    bandeira="https://flagcdn.com/w320/se.png",
    capital="Estocolmo",
    descricao="Um país nórdico conhecido por suas paisagens naturais, design e inovação.",
    lingua="Sueco"
)

p20 = Pais(
    id=20,
    nome="Noruega",
    bandeira="https://flagcdn.com/w320/no.png",
    capital="Oslo",
    descricao="Um país escandinavo famoso por seus fiordes, montanhas e a aurora boreal.",
    lingua="Norueguês"
)

p21 = Pais(
    id=21,
    nome="Nova Zelândia",
    bandeira="https://flagcdn.com/w320/nz.png",
    capital="Wellington",
    descricao="Um país insular no sudoeste do Oceano Pacífico, conhecido por suas paisagens deslumbrantes.",
    lingua="Inglês, Maori"
)

p22 = Pais(
    id=22,
    nome="Suíça",
    bandeira="https://flagcdn.com/w320/ch.png",
    capital="Berna",
    descricao="Um país montanhoso na Europa Central, famoso por seus Alpes, queijos e chocolates.",
    lingua="Alemão, Francês, Italiano"
)


paises = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22]

@app.route("/")
def index():
    return render_template("index.html", paises=paises)

@app.route("/pais/<int:id>/<nome>")
def detalhe(id, nome):
    for pais in paises:
        if pais.id == id and pais.nome.lower() == nome.lower():
            return render_template("pais.html", pais=pais)
    return "País não encontrado", 404
