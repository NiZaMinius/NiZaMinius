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
    <td width="175"><b>⌨️ Languages</b></td>
    <td>
      <img src="https://skillicons.dev/icons?i=rust,python,ts,js&theme=dark&perline=4" height="42" alt="Rust, Python, TypeScript, JavaScript" />
      <br/>
      <sub>Rust is my primary language.</sub>
    </td>
  </tr>
  <tr>
    <td><b>CLI & TUI</b></td>
    <td>
      <img src="https://img.shields.io/badge/Ratatui-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Ratatui" />
      <img src="https://img.shields.io/badge/Crossterm-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Crossterm" />
      <img src="https://img.shields.io/badge/Clap-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Clap" />
      <img src="https://img.shields.io/badge/Arboard-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Arboard" />
    </td>
  </tr>
  <tr>
    <td><b>Async & Discord</b></td>
    <td>
      <img src="https://img.shields.io/badge/Tokio-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Tokio" />
      <img src="https://img.shields.io/badge/Serenity-302642?style=flat-square&logo=discord&logoColor=C4B5FD" alt="Serenity" />
      <img src="https://img.shields.io/badge/Poise-302642?style=flat-square&logo=discord&logoColor=C4B5FD" alt="Poise" />
    </td>
  </tr>
  <tr>
    <td><b>Data & Serialization</b></td>
    <td>
      <img src="https://img.shields.io/badge/SQLx-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="SQLx" />
      <img src="https://img.shields.io/badge/Serde-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Serde" />
      <img src="https://img.shields.io/badge/serde__json-302642?style=flat-square&logo=json&logoColor=C4B5FD" alt="serde_json" />
      <img src="https://img.shields.io/badge/Chrono-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Chrono" />
    </td>
  </tr>
  <tr>
    <td><b>Errors & Logging</b></td>
    <td>
      <img src="https://img.shields.io/badge/Anyhow-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Anyhow" />
      <img src="https://img.shields.io/badge/Thiserror-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Thiserror" />
      <img src="https://img.shields.io/badge/Tracing-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Tracing" />
      <img src="https://img.shields.io/badge/Dotenvy-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Dotenvy" />
    </td>
  </tr>
  <tr>
    <td><b>Databases & Backend</b></td>
    <td>
      <img src="https://skillicons.dev/icons?i=sqlite,postgres,supabase&theme=dark&perline=3" height="42" alt="SQLite, PostgreSQL, Supabase" />
      <br/>
      <img src="https://img.shields.io/badge/pgvector-302642?style=flat-square" alt="pgvector" />
    </td>
  </tr>
  <tr>
    <td><b>Machine Learning</b></td>
    <td>
      <img src="https://img.shields.io/badge/Burn-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Burn" />
    </td>
  </tr>
  <tr>
    <td><b>Cryptography</b></td>
    <td>
      <img src="https://img.shields.io/badge/XChaCha20--Poly1305-302642?style=flat-square" alt="XChaCha20-Poly1305" />
      <img src="https://img.shields.io/badge/PBKDF2--HMAC--SHA256-302642?style=flat-square" alt="PBKDF2-HMAC-SHA256" />
      <img src="https://img.shields.io/badge/SHA--2-302642?style=flat-square" alt="SHA-2" />
      <img src="https://img.shields.io/badge/Zeroize-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="Zeroize" />
    </td>
  </tr>
  <tr>
    <td><b>Interoperability & APIs</b></td>
    <td>
      <img src="https://img.shields.io/badge/C%20ABI%20%2F%20FFI-302642?style=flat-square&logo=c&logoColor=C4B5FD" alt="C ABI / FFI" />
      <img src="https://img.shields.io/badge/Discord%20API-302642?style=flat-square&logo=discord&logoColor=C4B5FD" alt="Discord API" />
      <img src="https://img.shields.io/badge/REST%20APIs-302642?style=flat-square" alt="REST APIs" />
    </td>
  </tr>
  <tr>
    <td><b>Frontend · Previous experience</b></td>
    <td>
      <img src="https://skillicons.dev/icons?i=react,svelte,vite&theme=dark&perline=3" height="42" alt="React, Svelte, Vite" />
    </td>
  </tr>
  <tr>
    <td><b>Testing</b></td>
    <td>
      <img src="https://img.shields.io/badge/assert__cmd-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="assert_cmd" />
      <img src="https://img.shields.io/badge/predicates-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="predicates" />
      <img src="https://img.shields.io/badge/tempfile-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="tempfile" />
      <img src="https://img.shields.io/badge/serial__test-302642?style=flat-square&logo=rust&logoColor=C4B5FD" alt="serial_test" />
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
  <img src="./languages.svg" alt="GitHub language distribution by repository code size" />
</p>

### Code changes by quarter · GitHub

<!--START_SECTION:github-loc-->
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
