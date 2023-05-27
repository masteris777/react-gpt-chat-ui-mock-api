const express = require("express");
const cors = require("cors");
const app = express();
const bodyParser = require("body-parser");
const fs = require("fs/promises");

app.use(bodyParser.json());
app.use(cors()); // Add CORS middleware

function convertToBase64Chunk(str) {
	return `${Buffer.from(str).toString("base64")}\n`;
}

app.post("/api/summaries", async (req, res) => {
	console.log("got summary request");
	const { messages } = req.body;
	if (!messages || !messages[0]) {
		console.log("no messages");
		return res.status(400).json({ error: "Message is required" });
	}

	res.json({ summary: messages[0].text.substring(0, 20) });
});

app.post("/api/models/:model/conversations", async (req, res) => {
	const { messages } = req.body;
	if (!messages || !messages[0]) {
		console.log("no messages");
		return res.status(400).json({ error: "Message is required" });
	}
	const file = `./stories/story${
		messages[messages.length - 1].text.length % 4
	}.md`;

	const story = await fs.readFile(file, "utf8");
	const words = story.split(" ");
	let canceled = false;

	// Send response in a streaming manner
	res.writeHead(200, {
		"Content-Type": "text/plain",
		"Transfer-Encoding": "chunked",
		Connection: "keep-alive",
	});

	// Stream words one by one
	const intervalId = setInterval(() => {
		if (words.length > 0 && !canceled) {
			res.write(convertToBase64Chunk(words.shift() + " "));
		} else {
			res.end();
			clearInterval(intervalId);
		}
	}, 100);

	// Listen for cancellation
	req.on("end", () => {
		console.log("end");
		canceled = true;
	});
});

app.listen(3001, () => {
	console.log("Server listening on port 3001");
});
