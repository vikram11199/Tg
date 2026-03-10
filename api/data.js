import fs from "fs";
import path from "path";

export default function handler(req, res) {

try {

const q = (req.query.q || "").toLowerCase().replace("@","");

const filePath = path.join(process.cwd(),"tg.csv");

const data = fs.readFileSync(filePath,"utf8");

const lines = data.split(/\r?\n/);

let result = [];

for(let i=0;i<lines.length;i+=2){

const a = lines[i];
const b = lines[i+1];

if(!a || !b) continue;

const p1 = a.split("|");
const p2 = b.split("|");

if(p1.length < 4) continue;

const name = (p1[1] || "").toLowerCase();
const telegram_id = p1[2] || "";
const mobile = p1[3] || "";
const username = (p2[0] || "").toLowerCase();

if(
name.includes(q) ||
telegram_id.includes(q) ||
mobile.includes(q) ||
username.includes(q)
){

result.push({
name: p1[1],
telegram_id: telegram_id,
mobile: mobile,
username: p2[0]
});

}

}

res.status(200).json(result.slice(0,20));

}catch(e){

res.status(500).json({error:e.toString()});

}

}
