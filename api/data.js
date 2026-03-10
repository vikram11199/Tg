import fs from "fs";
import path from "path";

export default function handler(req, res) {

try {

let q = (req.query.q || "").toLowerCase().replace("@","");

const filePath = path.join(process.cwd(),"tg.csv");

const data = fs.readFileSync(filePath,"utf8");

const lines = data.split(/\r?\n/);

let result = [];

for(let i=0;i<lines.length;i+=2){

let line1 = lines[i]?.trim();
let line2 = lines[i+1]?.trim();

if(!line1 || !line2) continue;

let p1 = line1.split("|");
let p2 = line2.split("|");

if(p1.length < 4) continue;

let name = (p1[1] || "").toLowerCase();
let telegram_id = p1[2] || "";
let mobile = p1[3] || "";
let username = (p2[0] || "").toLowerCase();

if(
name.includes(q) ||
telegram_id.includes(q) ||
mobile.includes(q) ||
username.includes(q)
){

result.push({
name: p1[1],
telegram_id: p1[2],
mobile: p1[3],
username: p2[0]
});

}

}

res.status(200).json(result.slice(0,10));

}catch(e){

res.status(500).json({error:e.toString()});

}

  }
