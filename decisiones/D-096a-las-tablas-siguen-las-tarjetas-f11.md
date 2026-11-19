---
tipo: decision
id: D-096a
fecha: 2026-11-19
autor: angel
estado: vigente
tema: interfaz
---
# D-096a · Las tablas siguen las tarjetas f11 y f12 del canvas
- Angel decidió (2026-11-19, al aprobar el diseño): las tablas (casos Ofrecer tablas y Responder una oferta de tablas) se construyen como las dibujan las tarjetas f11 y f12 de la página «08 · Partida», versión 39.
  - «Ofrecer tablas» va abajo a la izquierda junto a «Salir de la partida», con un clic y sin confirmar; solo en partidas de dos jugadores.
  - Quien recibe ve un aviso arriba al centro con «Aceptar tablas» y «Rechazar», que no bloquea el tablero; si juega sin responder, la oferta se retira sola.
  - Quien ofrece ve «Ofreciste tablas» en su renglón y el botón apagado; si se la rechazan o caduca, una franja azul lo dice.
  - Una oferta cada cinco jugadas propias: el botón apagado dice cuántas faltan. Si los dos ofrecen, la segunda cuenta como aceptar.
  - Aceptar cierra la partida con tablas y sale la tablilla «Tablas» de f03.
- porqué: los casos de tablas no tenían prototipo vigente; la partida no tiene menú, así que el botón va junto a la otra acción de la partida.
- descartado: un menú de partida para ofrecer tablas, como decía el caso Ofrecer tablas.
- dónde vive: canvas https://claude.ai/artifact/JMdfC1XAcc8CrT2UE7M5AR, versión 39, página «08 · Partida», sección «6 · Tablas». Construido en la rama `match-closure` (sin commit). Probado en vivo el 2026-11-19: Claude probó ofrecer, rechazar y que la oferta se retire al jugar (partida 6014); Angel probó aceptar las tablas y las franjas de aviso. José no lo ha visto.
