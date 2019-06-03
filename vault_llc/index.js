const express = require("express");
const bodyParser = require("body-parser");
const session = require("express-session");

class Storage {
  constructor() {
    this._vault = {};
  }

  get(key) {
    console.log("get ", key);
    if (key === "flag" && this._vault["level"] != "spbctf_security_1337") {
      return "nope";
    }
    return this._vault[key];
  }

  set(key, value) {
    console.log("set ", key, value);
    if (key === "level" || key === "flag") {
      return "nope";
    }
    return (this._vault[key] = value);
  }

  setMultiple(...args) {
    console.log("setm ", args);
    let key = null,
      value = null;
    let queue = [];

    for (let curr of args) {
      if (typeof curr === "object") {
        queue.push(...curr);
      } else {
        if (curr === "level" || curr === "flag") {
          return "nope";
        }

        queue.push(curr);
      }
    }

    if (queue.length % 2 !== 0) return;

    for (let i = 0; i < queue.length; i += 2) {
      key = queue[i];
      value = queue[i + 1];

      if (key === "flag") {
        return "nope";
      }

      this._vault[key] = value;
    }

    return queue;
  }
}

const startServer = async port => {
  const app = express();
  app.use(bodyParser.json({ extended: true }));
  app.use(
    session({ secret: "battles", resave: false, saveUninitialized: true })
  );

  let storages = {};

  app.use((req, res, next) => {
    if (!storages[req.sessionID]) {
      storages[req.sessionID] = new Storage();
      storages[req.sessionID]._vault["flag"] = process.env["flag"] || "FLAG";
      storages[req.sessionID]._vault["level"] = "0";
    }

    req.storage = storages[req.sessionID];
    return next();
  });

  app.get("/", (req, res) => {
    res.sendFile(__dirname + "/index.html");
  });

  app.get("/index.js", (req, res) => {
    res.sendFile(__dirname + "/index.js");
  });

  app.get("/set", (req, res) => {
    const { key, value } = req.query;

    if (!key || !value) {
      return res.status(400).json({ error: "Not all params" });
    }

    res.json({
      value: req.storage.set(key, value)
    });
  });

  app.get("/setm", (req, res) => {
    res.json({
      value: req.storage.setMultiple(...req.body)
    });
  });

  app.get("/get", (req, res) => {
    const { key } = req.query;

    if (!key) {
      return res.status(400).json({ error: "Not all params" });
    }

    res.json({
      value: req.storage.get(key)
    });
  });

  app.listen(port, () => console.log(`Started at :${port}`));
};

startServer(31337);
