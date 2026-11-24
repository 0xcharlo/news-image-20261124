# News Image — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/0xcharlo/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/0xcharlo/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image that sums up the world's news of Tuesday 24 November 2026,
entered in the make.fun [`news-image-20261124`](https://make.fun/bounty/news-image-20261124) bounty. Play on make.fun with referral code `7n8phv37`.

## What it shows

- **Lead:** COP31 in Antalya ends with no deal — climate talks collapse
  over fossil fuels, the first summit to fail since Copenhagen in 2009.
- **Grid:** Ukraine sinks a Russian warship off Libya; Odesa left in the
  dark; Nvidia soars as Huang returns; a 6.5 quake near Vanuatu.
- **Also today:** BepiColombo reaches Mercury; EU plans a sports ban in
  new Russia sanctions; 14 nations back the ICJ genocide ruling on the
  Rohingya; Delta outage delays 2,000 flights.

Every headline was checked against Reuters, AP, BBC and ESA reporting
from 23–24 November 2026.

## How it is made

`render_frontpage.py` draws the front page from scratch with Pillow —
masthead, lead story, cracked-globe illustration, four-story grid,
also-today strip and footer. No stock photos or external images are used.

`main.py` is the competition entry point: it copies `news.png` to
`/output/entry.png`.

## Run it

```sh
python3 render_frontpage.py   # writes news.png (1024x1024)
python3 main.py               # writes /output/entry.png
```

## Verification

The rendered page is 1024x1024 pixels and well under the 1 MiB limit.
It was checked at full size and scaled to 300 pixels wide: headlines stay
legible, nothing overlaps, and no text is garbled.
