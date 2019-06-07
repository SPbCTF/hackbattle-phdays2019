Чтобы скомпилировать таск, нужно установить [Rust](https://www.rust-lang.org/tools/install).

После этого выполнить установку `wasm-pack`:

```
cargo install wasm-pack
```

Скомпилировать командой:

```
wasm-pack build --target web --no-typescript --out-name riddle
```

`.wasm` и `.js` будут расположены в директории `pkg`.