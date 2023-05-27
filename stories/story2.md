Sure, here's an example of how you might use Node.js's built-in fs (file system) module to read a text file asynchronously.

```javascript
const fs = require("fs").promises;

async function readFileAsync(filePath) {
	try {
		const data = await fs.readFile(filePath, "utf8");
		console.log(data);
	} catch (err) {
		console.error(`Error reading file from disk: ${err}`);
	}
}

// Replace './test.txt' with the path to the file you want to read
readFileAsync("./test.txt");
```

This code does the following:

- Import the fs module and use promises to get Promise-based version of fs functions.
- Define an asynchronous function readFileAsync() that reads a file from a specified path.
- Use the await keyword to wait for the fs.readFile() method to finish before logging the file data.
- Catch and log any errors that occur during file reading.

In this code, replace **'./test.txt'** with the path to the file you want to read. When you run this script, it will log the contents of the specified file to the console.
