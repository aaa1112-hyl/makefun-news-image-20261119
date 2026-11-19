# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/aaa1112-hyl/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/aaa1112-hyl/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A front-page-style image summing up Thursday 19 November 2026's world news in one 1024×1024 picture. Lead story: Trump, Xi and Putin hold the first three-way summit of the United States, China and Russia on the sidelines of APEC in Shenzhen — Ukraine, Iran and nuclear arms control on the agenda. Also covered: the International Court of Justice rules on Gambia's genocide accusation against Myanmar over the Rohingya; Anthropic prices its Nasdaq debut at $83 a share, above its $70–$78 range, in a record AI listing; and an "Also today" strip — Ukraine hits the Crimea bridge for a third time in a week, Iran fires at U.S. bases in the Gulf while the U.S. hits Qeshm Island, COP31 ministers meet in Antalya to unblock climate talks, Bangladesh unrest as Yunus's ancestral home is set on fire, a Van Gogh sells for $190.4M (a record for the artist), and the IAEA says North Korea expanded uranium enrichment.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to `/output/entry.png`. No network, deterministic — both runs write the same bytes. `generate_image.py` is the dev-time generator (Pillow + DejaVu fonts) that drew `entry.png` from the headlines above.

Sources checked 2026-11-19: One Turn daily brief, Horizon daily brief, FeedCast daily brief, Open Chronicle global brief.

---

<sub>Entered on [make.fun](https://make.fun/?ref=fhvxzr4c&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
