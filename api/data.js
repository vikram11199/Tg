import fs from "fs";
import path from "path";

export default function handler(req, res) {

try {

let q = (req.query.q || "").toLowerCase().replace("@","");

const filePath = path.join(process.cwd(),"tg.csv");

const data = fs.readFileSync(filePath,"utf8");

const lines = data.split(/\r?\n/);

let result = [];

for(let i=0;i<lines.length;i++){

let a = lines[i]?.trim();
let b = lines[i+1]?.trim();

if(!a || !b) continue;

if(a.includes("|") && !b.startsWith("0|") && !b.startsWith("1|")){

let p1 = a.split("|");
let p2 = b.split("|");

if(p1.length >=4){

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
telegram_id: telegram_id,
mobile: mobile,
username: p2[0]
});

}

}

}

}

res.status(200).json(result.slice(0,10));

}catch(e){

res.status(500).json({error:e.toString()});

}

}
