<div align="center">

# 🌒 NiZaMinius

<p align="center">
  <img src="https://count.getloli.com/@my-little-niza?theme=booru-lewd&padding=6&offset=2&align=center&scale=1.2&pixelated=1&darkmode=0&prefix=2379" alt="Profile visitor counter" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=A020F0&center=true&vCenter=true&width=600&lines=Code+as+art;Writing+darkness+line+by+line;Breathing+atmosphere+into+creations" alt="Typing SVG" />
</p>

</div>

<img src="https://github.com/andreasbm/readme/blob/master/assets/lines/cloudy.png" width="100%" alt="Cloudy divider" />

## About Me

Software developer focused on Rust and developer tooling. I build CLI/TUI applications and reusable libraries, with an emphasis on flexibility, safety, and performance. I'm particularly interested in systems programming, low-level concepts, software architecture, and improving existing solutions.

I also build integrations for local and hosted language models, including retrieval-augmented generation (RAG), tool calling, and database-backed multi-layer memory systems.

<p>
  <a href="https://discord.gg/bvUwqJSmFY"><img src="https://img.shields.io/badge/Discord-Community-5865F2?style=flat-square&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://t.me/NiZaMinius"><img src="https://img.shields.io/badge/Telegram-Contact-26A5E4?style=flat-square&logo=telegram&logoColor=white" alt="Telegram" /></a>
</p>

## Interests

- Systems programming and low-level software
- Software architecture and system design
- Performance optimization and improving existing solutions

<img src="https://github.com/andreasbm/readme/blob/master/assets/lines/cloudy.png" width="100%" alt="Cloudy divider" />

## Projects

<details>
<summary><b>tree2dir</b> — Turn text-based directory trees into real files and directories</summary>

[![Crates.io](https://img.shields.io/crates/v/tree2dir?style=flat-square&logo=rust&logoColor=white)](https://crates.io/crates/tree2dir)
[![Downloads](https://img.shields.io/crates/d/tree2dir?style=flat-square)](https://crates.io/crates/tree2dir)
[![Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github)](https://github.com/NiZaMinius/tree2dir)

A flexible Rust CLI/TUI utility that converts a text representation of a directory tree into actual files and directories.

**Highlights**
- Interactive TUI, Unix pipes, and file-based input.
- Handles box-drawing characters, spaces, tabs, and raw `tree` output with Unicode-aware indentation parsing.
- Detects directories from their structure instead of requiring every directory to be marked manually.
- Includes path-traversal protection, safe handling of existing files, and a `--dry-run` mode.
- Distributed as a self-contained binary.

**Stack:** Rust, Ratatui, Crossterm.

</details>

<details>
<summary><b>GameMaker-Save</b> — Encrypted save system for GameMaker Studio 2</summary>

[![Crates.io](https://img.shields.io/crates/v/gm-save-core?style=flat-square&logo=rust&logoColor=white)](https://crates.io/crates/gm-save-core)
[![Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github)](https://github.com/NiZaMinius/GameMaker-Save)

A cross-platform save system for GameMaker Studio 2, built around a Rust core and exposed to GameMaker through a C ABI layer.

**Highlights**
- XChaCha20-Poly1305 authenticated encryption.
- PBKDF2-HMAC-SHA256 key derivation and fallback-key rotation.
- Atomic writes to help protect existing save slots from interrupted writes.
- Independent save slots, metadata access, backups, and import/export operations.
- Builds for Windows, Linux, and macOS.

**Stack:** Rust, C ABI / FFI, XChaCha20-Poly1305, PBKDF2-HMAC-SHA256, GameMaker.

</details>

<details>
<summary><b>Entropix</b> — Real-time activity and chaos tracking for Discord</summary>

[![Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github)](https://github.com/Devoid-Kun/Entropix)

A collaborative Rust Discord bot that estimates channel activity using a heuristic chaos index based on message velocity, capitalization, and punctuation density. When activity crosses configured thresholds, the bot can rename the monitored channel and produce daily activity summaries.

**My contribution:** Implemented the core application logic and database layer, and handled a substantial part of the bug fixing. The project architecture and file structure were developed together with [Devoid-Kun](https://github.com/Devoid-Kun). The mathematical model and documentation were contributed by Devoid-Kun.

**Stack:** Rust, Serenity, Poise, Tokio, SQLx, SQLite.

</details>

<img src="https://github.com/andreasbm/readme/blob/master/assets/lines/cloudy.png" width="100%" alt="Cloudy divider" />

## Tech Stack

<details>
<summary><b>Languages, Libraries & Tools</b></summary>

<table align="center">
  <tr>
    <td width="175"><b>Languages</b></td>
    <td>
      <a href="https://www.rust-lang.org/"><img src="https://img.shields.io/badge/Rust-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Rust" /></a>
      <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-302642?style=flat-square&logo=python&logoColor=C4B5FD" alt="Python" /></a>
      <a href="https://www.typescriptlang.org/docs/"><img src="https://img.shields.io/badge/TypeScript-302642?style=flat-square&logo=typescript&logoColor=C4B5FD" alt="TypeScript" /></a>
      <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"><img src="https://img.shields.io/badge/JavaScript-302642?style=flat-square&logo=javascript&logoColor=C4B5FD" alt="JavaScript" /></a>
      <br/>
      <sub>Rust is my primary language.</sub>
    </td>
  </tr>
  <tr>
    <td><b>CLI & TUI</b></td>
    <td>
      <a href="https://ratatui.rs/"><img src="https://img.shields.io/badge/Ratatui-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Ratatui" /></a>
      <a href="https://docs.rs/crossterm/latest/crossterm/"><img src="https://img.shields.io/badge/Crossterm-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Crossterm" /></a>
      <a href="https://docs.rs/clap/latest/clap/"><img src="https://img.shields.io/badge/Clap-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Clap" /></a>
      <a href="https://docs.rs/arboard/latest/arboard/"><img src="https://img.shields.io/badge/Arboard-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Arboard" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Async & Discord</b></td>
    <td>
      <a href="https://tokio.rs/"><img src="https://img.shields.io/badge/Tokio-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Tokio" /></a>
      <a href="https://docs.rs/serenity/latest/serenity/"><img src="https://img.shields.io/badge/Serenity-302642?style=flat-square&logo=discord&logoColor=C4B5FD" alt="Serenity" /></a>
      <a href="https://docs.rs/poise/latest/poise/"><img src="https://img.shields.io/badge/Poise-302642?style=flat-square&logo=discord&logoColor=C4B5FD" alt="Poise" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Python Libraries</b></td>
    <td>
      <a href="https://discordpy.readthedocs.io/en/stable/"><img src="https://img.shields.io/badge/discord.py-302642?style=flat-square&logo=discord&logoColor=C4B5FD" alt="discord.py" /></a>
      <a href="https://docs.aiohttp.org/en/stable/"><img src="https://img.shields.io/badge/aiohttp-302642?style=flat-square&logo=python&logoColor=C4B5FD" alt="aiohttp" /></a>
      <a href="https://magicstack.github.io/asyncpg/current/"><img src="https://img.shields.io/badge/asyncpg-302642?style=flat-square&logo=postgresql&logoColor=C4B5FD" alt="asyncpg" /></a>
      <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-302642?style=flat-square&logo=flask&logoColor=C4B5FD" alt="Flask" /></a>
      <a href="https://saurabh-kumar.com/python-dotenv/"><img src="https://img.shields.io/badge/python-dotenv-302642?style=flat-square&logo=python&logoColor=C4B5FD" alt="python-dotenv" /></a>
      <a href="https://pytba.readthedocs.io/en/latest/"><img src="https://img.shields.io/badge/pyTelegramBotAPI-302642?style=flat-square&logo=telegram&logoColor=C4B5FD" alt="pyTelegramBotAPI" /></a>
      <a href="https://docs.python-telegram-bot.org/en/stable/"><img src="https://img.shields.io/badge/python-telegram-bot-302642?style=flat-square&logo=telegram&logoColor=C4B5FD" alt="python-telegram-bot" /></a>
      <a href="https://requests.readthedocs.io/en/latest/"><img src="https://img.shields.io/badge/Requests-302642?style=flat-square&logo=python&logoColor=C4B5FD" alt="Requests" /></a>
      <a href="https://github.com/Mimino666/langdetect"><img src="https://img.shields.io/badge/langdetect-302642?style=flat-square&logo=python&logoColor=C4B5FD" alt="langdetect" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Data & Serialization</b></td>
    <td>
      <a href="https://docs.rs/sqlx/latest/sqlx/"><img src="https://img.shields.io/badge/SQLx-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="SQLx" /></a>
      <a href="https://serde.rs/"><img src="https://img.shields.io/badge/Serde-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Serde" /></a>
      <a href="https://docs.rs/serde_json/latest/serde_json/"><img src="https://img.shields.io/badge/serde_json-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="serde_json" /></a>
      <a href="https://docs.rs/chrono/latest/chrono/"><img src="https://img.shields.io/badge/Chrono-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Chrono" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Errors & Logging</b></td>
    <td>
      <a href="https://docs.rs/anyhow/latest/anyhow/"><img src="https://img.shields.io/badge/Anyhow-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Anyhow" /></a>
      <a href="https://docs.rs/thiserror/latest/thiserror/"><img src="https://img.shields.io/badge/Thiserror-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Thiserror" /></a>
      <a href="https://docs.rs/tracing/latest/tracing/"><img src="https://img.shields.io/badge/Tracing-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Tracing" /></a>
      <a href="https://docs.rs/dotenvy/latest/dotenvy/"><img src="https://img.shields.io/badge/Dotenvy-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Dotenvy" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Databases & Backend</b></td>
    <td>
      <a href="https://sqlite.org/docs.html"><img src="https://img.shields.io/badge/SQLite-302642?style=flat-square&logo=sqlite&logoColor=C4B5FD" alt="SQLite" /></a>
      <a href="https://www.postgresql.org/docs/"><img src="https://img.shields.io/badge/PostgreSQL-302642?style=flat-square&logo=postgresql&logoColor=C4B5FD" alt="PostgreSQL" /></a>
      <a href="https://supabase.com/docs"><img src="https://img.shields.io/badge/Supabase-302642?style=flat-square&logo=supabase&logoColor=C4B5FD" alt="Supabase" /></a>
      <br/>
      <a href="https://github.com/pgvector/pgvector"><img src="https://img.shields.io/badge/pgvector-302642?style=flat-square&logo=postgresql&logoColor=C4B5FD" alt="pgvector" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Machine Learning</b></td>
    <td>
      <a href="https://burn.dev/book/"><img src="https://img.shields.io/badge/Burn-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Burn" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Cryptography</b></td>
    <td>
      <a href="https://docs.rs/chacha20poly1305/latest/chacha20poly1305/"><img src="https://img.shields.io/badge/XChaCha20-Poly1305-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="XChaCha20-Poly1305" /></a>
      <a href="https://docs.rs/pbkdf2/latest/pbkdf2/"><img src="https://img.shields.io/badge/PBKDF2-HMAC-SHA256-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="PBKDF2-HMAC-SHA256" /></a>
      <a href="https://docs.rs/sha2/latest/sha2/"><img src="https://img.shields.io/badge/SHA-2-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="SHA-2" /></a>
      <a href="https://docs.rs/zeroize/latest/zeroize/"><img src="https://img.shields.io/badge/Zeroize-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Zeroize" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Interoperability & APIs</b></td>
    <td>
      <img src="https://img.shields.io/badge/C%20ABI%20%2F%20FFI-302642?style=flat-square&logo=c&logoColor=C4B5FD" alt="C ABI / FFI" />
      <a href="https://discord.com/developers/docs/intro"><img src="https://img.shields.io/badge/Discord%20API-302642?style=flat-square&logo=discord&logoColor=C4B5FD" alt="Discord API" /></a>
      <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP"><img src="https://img.shields.io/badge/REST%20APIs-302642?style=flat-square" alt="REST APIs" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Frontend · Previous experience</b></td>
    <td>
      <a href="https://react.dev/"><img src="https://img.shields.io/badge/React-302642?style=flat-square&logo=react&logoColor=C4B5FD" alt="React" /></a>
      <a href="https://svelte.dev/docs"><img src="https://img.shields.io/badge/Svelte-302642?style=flat-square&logo=svelte&logoColor=C4B5FD" alt="Svelte" /></a>
      <a href="https://vite.dev/guide/"><img src="https://img.shields.io/badge/Vite-302642?style=flat-square&logo=vite&logoColor=C4B5FD" alt="Vite" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Testing</b></td>
    <td>
      <a href="https://docs.rs/assert_cmd/latest/assert_cmd/"><img src="https://img.shields.io/badge/assert_cmd-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="assert_cmd" /></a>
      <a href="https://docs.rs/predicates/latest/predicates/"><img src="https://img.shields.io/badge/predicates-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="predicates" /></a>
      <a href="https://docs.rs/tempfile/latest/tempfile/"><img src="https://img.shields.io/badge/tempfile-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="tempfile" /></a>
      <a href="https://docs.rs/serial_test/latest/serial_test/"><img src="https://img.shields.io/badge/serial_test-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="serial_test" /></a>
    </td>
  </tr>
</table>

</details>

<img src="https://github.com/andreasbm/readme/blob/master/assets/lines/cloudy.png" width="100%" alt="Cloudy divider" />

## Coding Statistics

<details>
<summary><b>⌛ Coding Statistics</b></summary>

<p align="center">
  <!-- Generated by the WakaTime stats workflow. -->
  <img src="./assets/wakatime-overview.svg" alt="WakaTime all-time coding time and recent development environment" />
</p>

### Languages by coding time · All time

<p align="center">
  <img src="./assets/wakatime-languages.svg" alt="WakaTime language distribution by coding time" />
</p>

### Languages in repositories · GitHub

<p align="center">
  <img src="./languages.svg" alt="GitHub language distribution across accessible repositories" />
</p>

### Code changes by quarter · GitHub

<!--START_SECTION:github-loc-->
**Timeline**

![Lines of Code chart](https://raw.githubusercontent.com/NiZaMinius/NiZaMinius/main/assets/bar_graph.png)


<!--END_SECTION:github-loc-->

</details>

## GitHub Activity

<div align="center">

<img src="./overview.svg" height="195" alt="GitHub profile statistics" />

<img src="https://streak-stats.demolab.com/?user=NiZaMinius&theme=dark&background=00000000&ring=A78BFA&fire=C4B5FD&currStreakLabel=A78BFA&sideLabels=C9C1D9&dates=827A94&hide_border=true" alt="GitHub contribution streak" />

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/NiZaMinius/NiZaMinius/output/github-snake-dark.svg" alt="GitHub contribution snake" />
</p>

<img src="https://github.com/andreasbm/readme/blob/master/assets/lines/cloudy.png" width="100%" alt="Cloudy divider" />

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=702963&height=100&section=footer" alt="Purple wave footer" />
</div>
