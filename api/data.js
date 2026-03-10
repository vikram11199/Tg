import fs from "fs";
import path from "path";

export default function handler(req, res) {
  try {

    const q = (req.query.q || "").toLowerCase().replace("@", "");

    const filePath = path.join(process.cwd(), "tg.csv");
    const data = fs.readFileSync(filePath, "utf8");

    const lines = data.split(/\r?\n/);

    let result = [];

    for (let i = 0; i < lines.length; i++) {

      const line = lines[i]?.trim();
      if (!line) continue;

      const p1 = line.split("|");

      // record line: index|name|telegramid|mobile
      if (p1.length === 4 && !isNaN(p1[0])) {

        const next = lines[i + 1]?.trim();
        if (!next) continue;

        const p2 = next.split("|");

        const name = (p1[1] || "").toLowerCase();
        const telegram_id = p1[2] || "";
        const mobile = p1[3] || "";
        const username = (p2[0] || "").toLowerCase();

        if (
          name.includes(q) ||
          telegram_id.includes(q) ||
          mobile.includes(q) ||
          username.includes(q)
        ) {
          result.push({
            name: p1[1],
            telegram_id: telegram_id,
            mobile: mobile,
            username: p2[0]
          });
        }

      }

    }

    res.status(200).json(result.slice(0, 10));

  } catch (e) {
    res.status(500).json({ error: e.toString() });
  }
}
