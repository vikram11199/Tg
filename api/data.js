import fs from "fs";

export default function handler(req, res) {

const file = fs.readFileSync("tg.csv","utf8");

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

}
