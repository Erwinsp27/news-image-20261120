# THE WORLD — 20 November 2026

A newspaper front page summing up the world's news of Friday, 20 November
2026. The masthead reads THE WORLD, with the dateline Friday, 20 November
2026. The lead illustration shows three leaders shaking hands at a summit
table in Shenzhen, above five smaller illustrated stories.

## The six stories

1. **Lead:** Trump, Xi and Putin meet in Shenzhen — the first three-way
   summit, with a joint peace declaration but no Ukraine breakthrough.
2. Kyiv hit by the biggest missile barrage of the year — 110 missiles,
   bridges damaged.
3. World court: Myanmar guilty of Rohingya genocide.
4. Houthi missile damages Riyadh tower.
5. Markets plunge, Nikkei down 4.8 percent as the AI rally falters.
6. COP31 drops the fossil-fuel phase-out.

## How to run

```sh
python3 main.py
```

The program writes `entry.png` to the output directory: the
`MAKEFUN_OUTPUT_DIR` environment variable when set, otherwise `/output`.
It takes no arguments, uses no network, and needs nothing but the Python
3.13 standard library. The output directory is created if it does not
already exist.

To try it in a scratch folder:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/news-out python3 main.py
```

## Deterministic output

The output is a byte-for-byte copy of the bundled `news.jpg`, so running
the program twice produces identical output. The image is 1024 by 1024
pixels, well under the 1 MiB limit.

## License

MIT — see `LICENSE`.
