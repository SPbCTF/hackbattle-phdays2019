const express = require("express");
const bodyParser = require("body-parser");
const fs = require("fs");

const app = express();
app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

app.get("/app.js", (req, res) => {
  res.send(fs.readFileSync(__filename));
});

app.get("/flag", (req, res) => {
  const body = req.body;

  let oops = {};
  for (let attr in body) {
    if (attr !== "secret") {
      oops[attr] = body[attr];
    }
  }

  if (oops.secret === "spbctf_ftw") {
    console.log("Somebody got flag!");
    console.log("Payload: ", body);
    res.status(200).json({
      flag: process.env["flag"]
    });
    return;
  }

  res.status(401).json(":(");
});

app.listen(31337, () => console.log("Started at :31337"));
