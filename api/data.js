import fs from "fs";
import path from "path";

export default function handler(req, res) {

try {

const filePath = path.join(process.cwd(), "tg.csv");

const file = fs.readFileSync(filePath, "utf8");

const lines = file.split("\n");

let result = [];

lines.forEach(line => {

const parts = line.split("|");

if(parts.length > 5){

result.push({
id: parts[0],
name: parts[1],
telegram_id: parts[4],
username: parts[5]
});

}

});

res.status(200).json(result);

} catch (e) {

res.status(500).json({error:"file read error"});

}

}
