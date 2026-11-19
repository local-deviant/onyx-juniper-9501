# news-image-20261119 v3 — Results

## The page

"The World in One Day" — Thursday 19 November 2026. Built from zero,
following the v3 design brief. No code read from v1 or v2.

- **40 stories, 7 regions, 12 drawn illustrations**
- **entry.png: 1024x1024 RGB, 203,306 bytes** (target 200-300KB)
- sha256: `df4ae0d811aee5611a67fd63311dec392c62d63e2b298e6c799e009660320de6`
- Deterministic: 3 renders byte-identical. `main.py` (stdlib) copies
  entry.png byte-identically to `MAKEFUN_OUTPUT_DIR`.

## Why v3 exists

v2 (readability-first, 243KB, all winner features) ranked 4,905 — WORSE
than v1 (2,943). Suspected cause: the lead headline "XI HUGS TRUMP IN
SHENZHEN" read as hype and was punished under the judge's "faithful, no
hype" criterion. v3 is factual and sober throughout: no hype words in any
headline ("hugs", "stuns", "shocks", "sinks" banned in the lead). The
page title follows the winning concept ("The World in One Day", ranks
1/4/6/9). Execution was polished to match ipot (rank 7, same 40/7/12
structure as our v2): clear hierarchy, generous spacing, measured type.

## Lead and mediums

- **Lead:** "TRUMP MEETS XI IN SHENZHEN" — first three-way summit with
  Putin opens at Kylin Villa; nuclear arms, trade, Ukraine and Iran on
  the agenda. Proof tag: DATE-CHECKED, Reuters / AFP / AP (hand-drawn
  check mark, no glyph).
- **Gulf:** "U.S. JETS HIT IRGC SITE" — Iran answers with drones at U.S.
  bases in Bahrain and Kuwait; three carrier groups in the Gulf.
- **Markets:** "BITCOIN FALLS TO $63,048" — down 2.9% in a day, 14.8%
  in a week; fear index at 10 as ETFs shed $240m.
- **Business:** "ANTHROPIC DEBUTS AT $81 BILLION" — priced at $83, the
  largest debut on record; shares start trading on Nasdaq under ANT.
- **Americas:** "PELTOLA TAKES ALASKA" — Democrat unseats Sullivan;
  Senate goes 56-44, the largest majority since 2009.

## Winner features (all present)

UTC timeline strip (4 stops: 00:00 BTC $63,048; 02:37 Anthropic prices
IPO at $83; 05:16 Trump-Putin talks end; 06:30 three-way summit meets),
DAY IN NUMBERS strip (BTC $63,048 / ANT $83 / GTA 99 / SENATE 56-44 /
AKVAN 110 KM/H / EU €45BN), proof tags, Gulf map, count bar
(40 stories · 7 regions · 12 drawn), dotted world map strip, crypto and
hot topics prominent (GTA VI 99, Voyager-free but crypto-led).

## The 40 stories (all 19 November 2026, researched independently)

Lead 1 + mediums 4 + art briefs 5 (Akvan, Ebola 11,500, Dow -561,
GTA VI 99, ICJ Rohingya) + region briefs 30:
ASIA 6 (Bangladesh, Russian bombers in Vietnam, Taiwan, S. Korea NK
talks, Indonesia fires, N. Korea uranium), EUROPE 5 (EU €45bn Ukraine
loan, COP31 Antalya, Crimea bridge, Van Gogh $190.4m, EU-Indonesia
trade), MIDDLE EAST 4 (Gaza line, Saudi PIF tower, Yemen missile, NSA
outage), AMERICAS 5 (Supreme Court TPS, Panama arrest, U.S.-Philippines
$2bn, House 254-170, Fed December hike), AFRICA 4 (Ethiopia-Eritrea,
Kenya milk, Somalia, Senegal boat), OCEANIA 3 (Fiji disaster, Cyclone
Xavier, Albanese APEC photo), GLOBAL 3 (Pew Islam 2035, 589m children
in conflict, drug-resistant infections 4.7m).

Sources checked via web search 19 Nov 2026: Reuters, Yonhap,
BusinessWorld, CNN, BitBeacon/Finnhub, BusinessWorld/TechCrunch,
AP/Reuters (Peltola), IMD, WHO, Le Monde, 10things.news, Horizon.

## 300px readability (2 render-and-fix rounds)

- Round 1: 13 region briefs over-wide (would wrap to 2 lines and
  overflow the grid); lead dek/proof crossed the rule line; cyclone
  headline wrapped; BTC chart labels overlapped ("$63,048" / "-14.8%
  WK"); IPO bar labels overlapped; skyline flags read as one striped
  flag; world map dots too sparse.
- Round 2: all briefs shortened to fit one line (0 over-wide);
  vertical layout re-budgeted; flags split onto three poles; BTC price
  moved to top of chart; IPO values above bars, names below, centred;
  map dots denser. Re-viewed at 300px AND 1024px: masthead, lead
  headline, all 4 medium headlines, timeline, day-in-numbers and
  region headers readable at 300px; brief grid is neat texture at
  300px and fully readable at full size. No overlap, no clipped text,
  no tofu glyphs (checkmark is hand-drawn; €/–/· verified rendering).

## Skills used (all free, offline)

prompt-to-design (typography + house fonts), genart (determinism +
render-look-fix loop), data-visualization (BTC line chart, IPO bars,
Senate bars: one accent, no chart junk), morning-paper-edition
(compose → budget → visual QA), morning-paper-writing (Strunk: cut
needless words, one-line briefs).
