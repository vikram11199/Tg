import fs from "fs";
import path from "path";

export default function handler(req, res) {

try {

const q = (req.query.q || "").toLowerCase().replace("@","");

const filePath = path.join(process.cwd(), "tg.csv");

const file = fs.readFileSync(filePath, "utf8");

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

res.status(200).json(result.slice(0,10));

} catch(e){

res.status(500).json({error:"server crashed"});

}

}
