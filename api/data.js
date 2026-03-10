import fs from "fs";

export default function handler(req, res) {

const q = (req.query.q || "").toLowerCase().replace("@","");

const file = fs.readFileSync("tg.csv","utf8");

const lines = file.split("\n");

let result = [];

lines.forEach(line => {

const p = line.split("|");

if(p.length >= 5){

const name = (p[1]||"").toLowerCase();
const telegram_id = p[2]||"";
const mobile = p[3]||"";
const username = (p[4]||"").toLowerCase();

if(
username.includes(q) ||
telegram_id.includes(q)
){

result.push({
name:p[1],
telegram_id:p[2],
mobile:p[3],
username:p[4]
});

}

}

});

res.json(result.slice(0,10));

}
